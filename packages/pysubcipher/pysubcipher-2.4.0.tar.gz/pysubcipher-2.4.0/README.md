![PyPiVersion]
![SupportedVersions]
![License]

[PyPiVersion]: https://img.shields.io/pypi/v/pysubcipher
[SupportedVersions]: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-orange
[License]: https://img.shields.io/badge/license-MIT-yellow

# Installation
Built and tested on Python 3.10 and above.<br>
No requirements other than the module itself.
```py
pip install pysubcipher
```
```py
python3 -m pip install pysubcipher
```
# Example Usage
### Encrypting and decrypting a short string of text
```py
def encrypt(self, s: str, /) -> bytes:
    ...
def decrypt(self, s: bytes, /) -> bytes:
    ...
```
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'e41BF3d8ebD5c0F34D2ce0caC5FCD2fbFAc576aB91bFAc576aB91E38cD3Da83deCEa8eeafc5AD23FC63Bacc983cBBFe02D4eAb46DeCaabd4E5Dda1E38cD3Da83deCEa8eeaDa487daD01Afe0abFAc576aB91F557edbaBe4e6052F0B41C11184'
b'Hello, World!'
```
# SubstitutionCipher
```py
def __init__(self, min_key_length: int = 10, max_key_length: int = 20, *, seed: int | float | str | bytes | bytearray | None = os.urandom(1024), charset: str = HEXDIGITS) -> None:
    ...
```
```py
"""A simple substitution cipher encryption tool to encode strings of text.

Args:
    min_key_length (int): The minimum length of a cipher key
    max_key_length (int): The maximum length of a cipher key
    seed (int | float | str | bytes | bytearray | None, optional): The seed that cipher keys will be generated with. Defaults to os.urandom(1024).
    charset (str, optional): The character set that cipher keys will be generated with. Defaults to HEXDIGITS.
"""
```
# Using built-in character sets
- BASE_2
- HEXDIGITS
- OCTDIGITS
- ALPHANUMERIC

### Base 2 Example
```py
from pysubcipher import SubstitutionCipher, BASE_2

subcipher = SubstitutionCipher(charset = BASE_2)

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'100001111110110000010100001011011110101010100010110111101010101001111001011010110111000110100100000011110100010010001000001001111001011000001111001111101010110111101010101001111101101101001111001001010'
b'Hello, World!'
```
# Using a custom character set
Character sets are provided as strings of text, and will be used to generate cipher keys.

**Note: An exception will be raised if the character set does not meet the minimum uniqueness requirement.**
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher(charset = "abcde1234")

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'accddb422a4bcc32bdaa2dd3b1beda34ecc32ed12134ecc32ed121cab4341d13d4b1dd32dbd1edebc2aac1b3cde1b1cedace3c1bcdacab4341d13d4b12ed3dcae1c2dbe4312ee34ecc32ed121bc4ab14112b2bb4a23e4c44c34bcdc12243e4'
b'Hello, World!'
```
# Saving keys to a file
Saving keys can be useful if you intend on using the same cipher keys in different instances of your program.

```py
"""Saves the current cipher keys to a file

Args:
    file (str): The path to the file
    truncate (bool, optional): If True, the file will be truncated prematurely before storing the keys. Defaults to False.
"""
```
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.save_keys("cipher_keys.dat")
```
# Loading saved keys from a file
```py
"""Loads cipher keys into the instance

Args:
    file (str): The path to the file where the keys are stored

Raises:
    InvalidKeysError: Raised if the cipher keys are not valid.
"""
```
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.load_keys("cipher_keys.dat")
```
# Setting a custom seed
```py
def set_seed(self, seed: int | float | str | bytes | bytearray | None, /) -> None:
    ...
```
If you don't intend on storing cipher keys in a file, you can always use a set seed so the cipher keys are the same every time you run your program.
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.set_seed("my_amazing_seed")
```
# Regenerating cipher keys
```py
def regenerate_keys(self, seed: int | float | str | bytes | bytearray | None | None = None, /) -> None:
    ...
```
```py
"""Regenerates encryption and decryption keys.

Args:
    seed (int | float | str | bytes | bytearray | None, optional): The seed to generate cipher keys with. Defaults to os.urandom(1024).
"""
```
# Encrypting and decrypting files
```py
class FileSubstitutionCipher(SubstitutionCipher):
    def __init__(self, min_key_length: int = 10, max_key_length: int = 20, *, seed: int | float | str | bytes | bytearray | None = os.urandom(1024), charset: str = HEXDIGITS) -> None:
```
```py
"""A simple substitution cipher encryption tool to encrypt file's and their contents.

Args:
    min_key_length (int): The minimum length of a cipher key.
    max_key_length (int): The maximum length of a cipher key.
    seed (int | float | str | bytes | bytearray | None, optional): The seed that cipher keys will be generated with. Defaults to os.urandom(1024).
    charset (str, optional): The character set that cipher keys will be generated with. Defaults to HEXDIGITS.
"""
```
### Encrypting
```py
def encrypt(self, filepath: str, /, *, write: bool = False) -> bytes | None:
    ...
```
```py
"""Encrypts the contents of a file and returns the encrypted contents or None

Args:
    filepath (str): The path to the file that will be encrypted
    write (bool, optional): Whether the program will write to that file, overriding it's original contents. Defaults to False.

Returns:
    bytes | None: Returns the encrypted contents if write is False, otherwise returns None
"""
```

### Decrypting
```py
def decrypt(self, filepath: str, /, *, write: bool = False) -> bytes | None:
    ...
```
```py
"""Decrypts the contents of a file and returns the decrypted contents or None

Args:
    filepath (str): The path to the file that will be decrypted
    write (bool, optional): Whether the program will write to that file, overriding it's original contents. Defaults to False.

Returns:
    bytes | None: Returns the decrypted contents if write is False, otherwise returns None
"""
```

### Example Usage
```py
from pysubcipher import FileSubstitutionCipher

filepath: str = "my_file.txt"

subcipher = FileSubstitutionCipher()

# Override the file's contents with the encrypted contents
subcipher.encrypt(filepath, write = True)

# Get the decrypted contents without modifying the file
decrypted_file_contents = subcipher.decrypt(filepath) # write is defaulted to False
print(decrypted_file_contents)
```

### Output
`my_file.txt`
```py
b'D2d3F1Db7eEdE28A34Df31975e98a7Bfb0cfd21c89DB168FACbe7eDE9bb98f5cfADFff093771B08093b8daC56e1A3Df0DF8Bedeebf1268FACbe7eDE9bb95CF51C2C9c06Dc9C8f5cfADFff093768FACbe7eDE9bb914734bB8AAaAD8ef71B08093b8daC56e1A3D5CF51C2C9c06Dc9C2baB2eB530Cd88322A731F9d1DC00Ddfe814734bB8AAaAD8ef68FACbe7eDE9bb9322A731F9d1DC00Ddfe814734bB8AAaAD8eff0DF8Bedeebf12'
```
`Console Output`
```py
b'Super secret contents'
```

# Exceptions and error handling
## `InvalidCharacterError`
```py
def __init__(self, character: str, /) -> None:
    ...
```
Raised if an invalid token is present within a string of text while encrypting or decrypting a value.

## `EncryptedStringInvalidError`
```py
def __init__(self, token: str) -> None:
    ...
```
Raised while decrypting a string of text if the encrypted string is not valid or does not match any decryption keys.

## `InvalidKeysError`
```py
def __init__(self) -> None:
    ...
```
Raised inside of the `load_keys()` function of the `SubstitutionCipher` class if the cipher keys fail validation.