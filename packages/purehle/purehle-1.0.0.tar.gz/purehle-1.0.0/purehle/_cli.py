from __future__ import annotations

from argparse import ArgumentParser
from sys import stderr
from typing import Type

from purehash._common import Hash

from purehle import MD5, SHA1, SHA256, SHA512
from purehle._common import HLE

DIGEST_LENGTHS: dict[int, tuple[Type[HLE], ...]] = {
    16: (MD5,),
    20: (SHA1,),
    32: (SHA256,),
    64: (SHA512,),
}


def encode(string: str, encoding: str) -> bytes:
    if encoding.lower() == "hex":
        return bytes.fromhex(string)
    else:
        return string.encode(encoding)


def cli() -> None:
    parser = ArgumentParser()

    parser.add_argument(
        "-d", "--digest", type=bytes.fromhex, required=True, metavar="HEX"
    )
    parser.add_argument("-o", "--original", default="", metavar="STRING")
    parser.add_argument("-l", "--length", type=int, required=True, metavar="INT")
    parser.add_argument("-a", "--append", default="", metavar="STRING")
    parser.add_argument("-t", "--type", metavar="STRING")
    parser.add_argument("-e", "--encoding", default="utf-8", metavar="STRING")

    arguments = parser.parse_args()

    if len(arguments.digest) not in DIGEST_LENGTHS:
        raise ValueError(f"Digest length {len(arguments.digest)} not supported.")

    hles: tuple[Type[HLE], ...] = DIGEST_LENGTHS[len(arguments.digest)]
    hle: Type[HLE]
    if arguments.type is None:
        hle = hles[0]
        print(f"Using hash type {hle.__name__}.", file=stderr)
        if len(hles) == 2:
            print(
                f"{hles[1].__name__} is also available and can be used with -t.",
                file=stderr,
            )
        elif len(hles) > 2:
            print(
                f"""{", ".join(i.__name__ for i in hles[1:-1])} and {hles[-1].__name__} are also available and can be used with -t.""",
                file=stderr,
            )
    else:
        for hle in hles:
            if hle.__name__.upper() == arguments.type.upper():
                break
        else:
            raise ValueError(
                f"Hash type {arguments.type} does not exist for digest length {len(arguments.digest)}."
            )

    original: bytes = encode(arguments.original, arguments.encoding)
    append: bytes = encode(arguments.append, arguments.encoding)

    padding: bytes
    hash_: Hash
    padding, hash_ = hle(arguments.digest, original).with_length(arguments.length)

    hash_.update(append)
    print(f"Hash (hex): {hash_.hexdigest()}")
    print(f"Hash (bytes): {hash_.digest()!r}")

    data: bytes = original + padding + append
    print(f"Data (hex): {data.hex()}")
    print(f"Data (bytes): {data!r}")
