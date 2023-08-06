from __future__ import annotations

from purehash._common import Hash


class HLE:
    digest: bytes
    original: bytes
    append: bytes

    def __init__(self, digest: bytes, original: bytes) -> None:
        self.digest = digest
        self.original = original

    def with_length(self, length: int) -> tuple[bytes, Hash]:
        pass
