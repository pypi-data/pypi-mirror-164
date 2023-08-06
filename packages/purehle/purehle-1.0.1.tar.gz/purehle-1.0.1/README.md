# PureHLE

Pure Python hash length extension.

## Installation

```
pip install purehle
```

## Usage

Information used in the examples:

- Hash of key + `DE`: `2ecdde3959051d913f61b14579ea136d`
- Length of key: 3
- Data to append: `F`

### CLI

```
> purehle -d 2ecdde3959051d913f61b14579ea136d -o DE -l 3 -a F

Using hash type MD5.
Hash (hex): d542ef0939e3c366f3eca18d4fa0bc77
Hash (bytes): b'\xd5B\xef\t9\xe3\xc3f\xf3\xec\xa1\x8dO\xa0\xbcw'
Data (hex): 4445800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000280000000000000046
Data (bytes): b'DE\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00F'
```

### Module

```python
import purehle

hle = purehle.MD5(bytes.fromhex("2ecdde3959051d913f61b14579ea136d"), b"DE")
padding, m = hle.with_length(3)
m.update(b"F")
data = hle.original + padding + b"F"

data  # b"DE\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00F"
m.hexdigest() # d542ef0939e3c366f3eca18d4fa0bc77
```

## Supported Hash Algorithms

- MD5 (`MD%`)
- SHA-1 (`SHA1`)
- SHA-256 (`SHA256`)
- SHA-512 (`SHA512`)

