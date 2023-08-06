# PureHLE

Pure Python hash length extension.

## Installation

```
pip install purehle
```

## Usage

```python
import hashlib

import purehle

hle = purehle.MD5(hashlib.md5(b"ABCDE").digest(), b"DE")
padding, m = hle.with_length(3)
m.update(b"FG")
message = hle.original + padding + b"FG"

message  # b"DE\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00FG"
m.hexdigest() # 4bbc3725884dad7b4e1358c51959f0b0

hashlib.md5(b"ABC" + message).digest() == m.digest()
```

## Supported Hash Algorithms

- MD5 (`MD%`)
- SHA-1 (`SHA1`)
- SHA-256 (`SHA256`)
- SHA-512 (`SHA512`)

