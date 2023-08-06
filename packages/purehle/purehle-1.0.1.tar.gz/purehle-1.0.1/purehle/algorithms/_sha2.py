from __future__ import annotations

from purehash import sha256, sha512
from purehash._util import padding, unpack

from purehle._common import HLE


class SHA256(HLE):
    def with_length(self, length: int) -> tuple[bytes, sha256]:
        message_length: int = length + len(self.original)
        padding_ = padding(message_length, 64, 8, False)

        hash_: sha256 = sha256()
        (
            hash_._a,
            hash_._b,
            hash_._c,
            hash_._d,
            hash_._e,
            hash_._f,
            hash_._g,
            hash_._h,
        ) = unpack(4, False, self.digest)
        hash_._blocks_processed = (message_length + len(padding_)) // 64

        return padding_, hash_


class SHA512(HLE):
    def with_length(self, length: int) -> tuple[bytes, sha512]:
        message_length: int = length + len(self.original)
        padding_ = padding(message_length, 128, 16, False)

        hash_: sha512 = sha512()
        (
            hash_._a,
            hash_._b,
            hash_._c,
            hash_._d,
            hash_._e,
            hash_._f,
            hash_._g,
            hash_._h,
        ) = unpack(8, False, self.digest)
        hash_._blocks_processed = (message_length + len(padding_)) // 128

        return padding_, hash_
