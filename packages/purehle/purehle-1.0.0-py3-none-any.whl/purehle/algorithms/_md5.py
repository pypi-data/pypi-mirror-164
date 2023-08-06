from __future__ import annotations

from purehash import md5
from purehash._util import padding, unpack

from purehle._common import HLE


class MD5(HLE):
    def with_length(self, length: int) -> tuple[bytes, md5]:
        message_length: int = length + len(self.original)
        padding_ = padding(message_length, 64, 8, True)

        hash_: md5 = md5()
        hash_._a, hash_._b, hash_._c, hash_._d = unpack(4, True, self.digest)
        hash_._blocks_processed = (message_length + len(padding_)) // 64

        return padding_, hash_
