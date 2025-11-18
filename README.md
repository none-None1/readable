# The Readable esolang
The Readable esolang is, unlike its name, very unreadable because it uses the `−` (U+2212) and `-` (U+002D) characters, which look exactly the same in some fonts.

## Commands
You can read more on [Esolang wiki](https://esolangs.org/wiki/Readable).

## This repo includes:
* `main.py`: The main interpreter.
* `conv.py`: The tool that converts between U+2212 and `=`.
* `pseudogen.py`: Converts "pseudocode" into Readable code.
* Examples, both standard version and version with `=` instead of U+2212.
  * `hw_(readable).rdb`: Hello, world!
  * `cat_(readable).rdb`: Cat program
  * `apb_(readable).rdb`: A+B Problem
  * `apb_with_mem_(readable).rdb`: A+B Problem with memory usage
  * `tm_(readable).rdb`: Truth Machine
  * `xkcd_(readable).rdb`: XKCD Random number
  * `looping_counter_(readable).rdb`: Looping counter
  * `df_(readable).rdb`: Deadfish interpreter

### non-standard behavior of the interpreter
* `=` is also accepted as an alternative of U+2212.
* Malformed code causes undefined behavior.
* Negative numbers are supported.
