from purehash import sha1

from purehle._util import random_tests
from purehle.algorithms._sha1 import SHA1


def test_sha1():
    random_tests(sha1, SHA1, (55, 56, 57, 63, 64, 65))
