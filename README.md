# The Readable esolang
The Readable esolang is, unlike its name, very unreadable because it uses the `−` (U+2212) and `-` (U+002D) characters, which look exactly the same in some fonts.

## Commands
You can read more on [Esolang wiki](https://esolangs.org/wiki/Readable).

## This repo includes:
* `main.py`: The main interpreter.
* `conv.py`: The tool that converts between U+2212 and `=`.
* `pseudogen.py`: Converts "pseudocode" into Readable code.
* Examples, both standard version and version with `=` instead of U+2212.

### non-standard behavior of the interpreter
* `=` is also accepted as an alternative of U+2212.
* Malformed code causes undefined behavior.
* Negative numbers are supported.
