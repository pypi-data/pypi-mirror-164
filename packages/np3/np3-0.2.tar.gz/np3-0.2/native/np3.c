#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"
#include <stdbool.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

#define MINIMP3_IMPLEMENTATION
#include "minimp3.h"

#define ALLOC_STEP 2621440
#define MIN_STREAM_DECODE 32768
#define DECODE_BLOCK 2621440


typedef struct {
    PyObject_HEAD
    mp3dec_t mp3d;
    unsigned char unprocessed_data[DECODE_BLOCK];
    size_t unprocessed_len;
    int channels;
    int hz;
    bool flushed;
} StreamDecoderObj;

typedef struct {
    mp3d_sample_t *samples;
    int len;
    size_t allocated;
} DecodedData;

typedef struct {
    PyObject *exception;
    // NB: String litrals only! No memory management here!
    char *exception_str;
} NP3Error;

void
decoded_data_init(DecodedData *data)
{
    data->len = 0;
    data->samples = (mp3d_sample_t*) malloc(ALLOC_STEP * sizeof(mp3d_sample_t));
    data->allocated = ALLOC_STEP;
}

void
decoded_data_grow(DecodedData *data)
{
    data->samples = (mp3d_sample_t*) realloc (
        data->samples,
        (data->allocated + ALLOC_STEP) * sizeof(mp3d_sample_t)
    );
    data->allocated += ALLOC_STEP;
}

void
decoded_data_compact(DecodedData *data)
{
    data->samples = (mp3d_sample_t*) realloc (
        data->samples,
        (data->len) * sizeof(mp3d_sample_t)
    );
    data->allocated = data->len;
}

void
decoded_data_free(DecodedData *data)
{
    free(data->samples);
}

void
np3_error_init(NP3Error *error)
{
    error->exception = NULL;
    error->exception_str = NULL;
}

static PyObject *
StreamDecoder_reset(StreamDecoderObj *self, PyObject *Py_UNUSED(ignored))
{
    mp3dec_init(&self->mp3d);
    self->unprocessed_len = 0;
    self->channels = 0;
    self->hz = 0;
    self->flushed = false;

    Py_RETURN_NONE;
}

static PyObject *
StreamDecoder_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    StreamDecoderObj *self;
    self = (StreamDecoderObj *) type->tp_alloc(type, 0);
    if (self != NULL)
    {
        StreamDecoder_reset(self, Py_None);
    }
    return (PyObject *) self;
}

static PyObject *
StreamDecoder_getchannels(StreamDecoderObj *self, void *closure)
{
    if (self->channels == 0)
    {
        Py_RETURN_NONE;
    }

    return Py_BuildValue("i", self->channels);
}

static PyObject *
StreamDecoder_gethz(StreamDecoderObj *self, void *closure)
{
    if (self->hz == 0)
    {
        Py_RETURN_NONE;
    }
    return Py_BuildValue("i", self->hz);
}

size_t
refill_unprocessed(
    StreamDecoderObj *self,
    const char *input,
    size_t input_len)
{
    size_t consumed = sizeof(self->unprocessed_data) - self->unprocessed_len;
    if (consumed > input_len)
    {
        consumed = input_len;
    }
    memcpy(
        self->unprocessed_data + self->unprocessed_len,
        input,
        consumed
    );
    self->unprocessed_len += consumed;

    return consumed;
}

NP3Error
decode_unprocessed(
    StreamDecoderObj *self,
    DecodedData *decoded_data,
    bool flush
)
{
    size_t pos = 0;
    size_t samples_free;
    size_t nsamples;
    mp3dec_frame_info_t info;
    NP3Error error;
    size_t min_data_left = MIN_STREAM_DECODE;

    np3_error_init(&error);

    if (flush)
    {
        min_data_left = 0;
    }

    if (self->unprocessed_len <= min_data_left)
    {
        return error;
    }

    while(pos < self->unprocessed_len - min_data_left)
    {
        samples_free = decoded_data->allocated - decoded_data->len;
        if (samples_free < MINIMP3_MAX_SAMPLES_PER_FRAME)
        {
            decoded_data_grow(decoded_data);
        }

        nsamples = mp3dec_decode_frame(
            &self->mp3d,
            (const unsigned char*)(self->unprocessed_data + pos),
            self->unprocessed_len - pos,
            decoded_data->samples + decoded_data->len,
            &info
        );
        nsamples *= info.channels;
        decoded_data->len += nsamples;
        pos += info.frame_bytes;

        if (info.frame_bytes == 0)
        {
            error.exception = PyExc_RuntimeError;
            error.exception_str = "Unexpected insufficient data error. "
                                  "Further processing is impossible";
            return error;
        }

        if (self->channels == 0)
        {
            self->channels = info.channels;
            self->hz = info.hz;
        }
    }

    if (pos > 0 && self->unprocessed_len > pos)
    {
        memmove(
            self->unprocessed_data,
            self->unprocessed_data + pos,
            self->unprocessed_len - pos
        );
    }
    self->unprocessed_len -= pos;

    return error;
}

void
capsule_ndarray_cleanup(PyObject *capsule)
{
    void *samples = PyCapsule_GetPointer(capsule, NULL);
    free(samples);
}

PyObject*
make_ndarray(DecodedData *data)
{
    long int dims[1];
    PyObject *ndarray;
    PyObject *capsule;

    if (data->len == 0) {
        decoded_data_free(data);
        dims[0] = 0;
        return PyArray_EMPTY(1, dims, NPY_INT16, 0);
    }

    decoded_data_compact(data);

    dims[0] = data->len;
    ndarray = PyArray_SimpleNewFromData(1, dims, NPY_INT16, data->samples);
    if (ndarray == NULL) {
        decoded_data_free(data);
        return NULL;
    }

    capsule = PyCapsule_New(data->samples, NULL, capsule_ndarray_cleanup);
    if (capsule == NULL) {
        decoded_data_free(data);
        Py_XDECREF(ndarray);
        return NULL;
    }

    if (PyArray_SetBaseObject((PyArrayObject *) ndarray, capsule) == -1) {
        decoded_data_free(data);
        Py_XDECREF(capsule);
        Py_XDECREF(ndarray);
        return NULL;
    }

    return ndarray;
}

static PyObject *
StreamDecoder_decode(StreamDecoderObj *self, PyObject *args)
{
    Py_buffer input;

    if (self->flushed) {
        PyErr_SetString(
            PyExc_RuntimeError,
            "decode() called after flush(). Call reset() to reuse the decoder "
            "object"
        );
        return NULL;
    }

    if (! PyArg_ParseTuple(args, "y*:decode", &input)) {
        return NULL;
    }

    size_t input_pos = 0;
    DecodedData decoded_data;
    NP3Error error;

    Py_BEGIN_ALLOW_THREADS

    np3_error_init(&error);
    decoded_data_init(&decoded_data);

    while (input_pos < input.len) {
        input_pos += refill_unprocessed(
            self,
            input.buf + input_pos,
            input.len - input_pos
        );
        error = decode_unprocessed(self, &decoded_data, false);
        if (error.exception != NULL)
        {
            break;
        }
    }

    Py_END_ALLOW_THREADS

    PyBuffer_Release(&input);

    if (error.exception != NULL)
    {
        PyErr_SetString(error.exception, error.exception_str);
        decoded_data_free(&decoded_data);
        return NULL;
    }

    PyObject *ndarray = make_ndarray(&decoded_data);
    if (ndarray == NULL)
    {
        return NULL;
    }
    return Py_BuildValue("N", ndarray);
}

static PyObject *
StreamDecoder_flush(StreamDecoderObj *self, PyObject *Py_UNUSED(ignored))
{
    DecodedData decoded_data;
    NP3Error error;

    Py_BEGIN_ALLOW_THREADS

    decoded_data_init(&decoded_data);
    error = decode_unprocessed(self, &decoded_data, true);
    self->flushed = true;

    Py_END_ALLOW_THREADS

    if (error.exception != NULL)
    {
        PyErr_SetString(error.exception, error.exception_str);
        decoded_data_free(&decoded_data);
        return NULL;
    }

    PyObject *ndarray = make_ndarray(&decoded_data);
    if (ndarray == NULL)
    {
        return NULL;
    }
    return Py_BuildValue("N", ndarray);
}

static PyGetSetDef StreamDecoder_getsetters[] = {
    {"channels", (getter) StreamDecoder_getchannels, NULL,
     "Number of channels", NULL},
    {"hz", (getter) StreamDecoder_gethz, NULL,
     "Sampling rate", NULL},
    {NULL}  /* Sentinel */
};

static PyMethodDef StreamDecoder_methods[] = {
    {"decode", (PyCFunction) StreamDecoder_decode, METH_VARARGS,
    "Decode another block of data, returning NDarray[int16]."},
    {"flush", (PyCFunction) StreamDecoder_flush, METH_NOARGS,
    "Finish decoding what may be left from previous decode() calls."},
    {"reset", (PyCFunction) StreamDecoder_reset, METH_NOARGS,
    "Reset the internal state for a new stream."},
    {NULL}  /* Sentinel */
};

static PyTypeObject StreamDecoderType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "_native.StreamDecoder",
    .tp_doc = PyDoc_STR("Stream MP3 decoder"),
    .tp_basicsize = sizeof(StreamDecoderObj),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = StreamDecoder_new,
    .tp_getset = StreamDecoder_getsetters,
    .tp_methods = StreamDecoder_methods,
};

static struct PyModuleDef nativemodule = {
    PyModuleDef_HEAD_INIT,
    "_native",
    "Native extension for NumPy mp3 decoder. Use np3 module instead.",
    -1
};

PyMODINIT_FUNC
PyInit__native(void)
{
    PyObject *module;
    if (PyType_Ready(&StreamDecoderType) < 0)
    {
        return NULL;
    }

    import_array();
    module = PyModule_Create(&nativemodule);
    if (module == NULL)
    {
        return NULL;
    }

    Py_INCREF(&StreamDecoderType);
    if (PyModule_AddObject(
            module,
            "StreamDecoder", 
            (PyObject *) &StreamDecoderType
        ) < 0)
    {
        Py_DECREF(&StreamDecoderType);
        Py_DECREF(module);
        return NULL;
    }

    return module;
}
