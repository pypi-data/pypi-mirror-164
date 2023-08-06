from purehash import md5

from purehle._util import random_tests
from purehle.algorithms._md5 import MD5


def test_md5():
    random_tests(md5, MD5, (55, 56, 57, 63, 64, 65))
