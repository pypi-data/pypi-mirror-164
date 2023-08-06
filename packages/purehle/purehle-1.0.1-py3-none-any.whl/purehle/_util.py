from __future__ import annotations

from copy import deepcopy
from random import choice, getrandbits
from typing import Type

from purehash._common import Hash

from purehle._common import HLE


def random_tests(
    hash_: Type[Hash], hle: Type[HLE], problem_lengths: tuple[int, ...]
) -> None:
    lengths: tuple[int, ...] = (0, 1) + problem_lengths

    for _ in range(16):
        key: bytes = bytes(getrandbits(8) for _ in range(choice(lengths)))
        original: bytes = bytes(getrandbits(8) for _ in range(choice(lengths)))

        hash__: Hash = hash_(key + original)
        digest: bytes = hash__.digest()

        hle_: HLE = hle(digest, original)

        offset_: int
        for offset_ in (2, 1, 0):
            padding: bytes
            m2: Hash
            padding, m2 = hle_.with_length(len(key) + offset_)

            m1: Hash = deepcopy(hash__)
            m1.update(padding)

            append: bytes = bytes(getrandbits(8) for _ in range(choice(lengths)))
            m1.update(append)
            m2.update(append)

            assert (offset_ == 0) == (m1.digest() == m2.digest())
            assert (offset_ == 0) == (m1.hexdigest() == m2.hexdigest())
