from __future__ import annotations

from purehash import sha1
from purehash._util import padding, unpack

from purehle._common import HLE


class SHA1(HLE):
    def with_length(self, length: int) -> tuple[bytes, sha1]:
        message_length: int = length + len(self.original)
        padding_ = padding(message_length, 64, 8, False)

        hash_: sha1 = sha1()
        hash_._a, hash_._b, hash_._c, hash_._d, hash_._e = unpack(4, False, self.digest)
        hash_._blocks_processed = (message_length + len(padding_)) // 64

        return padding_, hash_
