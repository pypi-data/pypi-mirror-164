from array import array
from numpy import int16
from numpy.typing import NDArray

Buffer = bytearray | array | memoryview | bytes | NDArray

class StreamDecoder:

    def decode(self, input: Buffer) -> NDArray[int16]: ...
    def flush(self) -> NDArray[int16]: ...
    def reset(self) -> None: ...

    @property
    def channels(self) -> int | None: ...

    @property
    def hz(self) -> int | None: ...