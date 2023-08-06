# NP3

A fast python library to load mp3 data into [NumPy](https://numpy.org) arrays.

It is based on lieff's [minimp3](https://github.com/lieff/minimp3)

## Installation

`pip install np3`

## Usage

```python3
import np3

mp3 = np3.MP3(path="/my/mp3/file")

# or

with open("/path/to/file.mp3") as mp3_fh:
    mp3 = np3.MP3(file=mp3_fh)

# or

data: bytes = obtain_mp3_data()
mp3 = np3.MP3(data=data)

print(f"Channels: {mp3.channels}")
print(f"Sampling rate: {mp3.hz} Hz")

length = len(mp3.samples[0]) / mp3.hz
print(f"Length: {length:.1f} seconds")
```

## Threaded performance

[GIL](https://docs.python.org/3/glossary.html#term-GIL) is released before
decoding starts. On multi core machines this brings additional performance
when decoding in separate threads. While decoding a single file does not
parallelise, other python threads can continue working while the file is
being processed. Where multiple files need decoding this performance gain
becomes particularly significant.

```python3
from concurrent.futures import ThreadPoolExecutor

files = ["/path/to/file1.mp3", "/path/to/file2.mp3", ...]

with ThreadPoolExecutor() as executor:
    mp3s = executor.map(
        lambda p: np3.MP3(path=p),
        files,
    )
```
