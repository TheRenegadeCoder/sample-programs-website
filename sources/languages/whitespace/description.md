According to [Wikipedia][1], Whitespace is an esoteric language developed by
Edwin Brady and Chris Morris in 2002 at the University of Durham. According to
the [Esolang Wiki][4], a post to Slashdot about the language was done on April
1, 2003. Most people assumed it was a joke. However, it was not.

Unlike other languages where whitespace characters are either ignored
or used as a separator between tokens, Whitespace uses these characters as
instructions. All instructions are made up of 3 whitespace characters:

- space (ASCII code 32)
- tab (ASCII code 9)
- linefeed (ASCII code 10), also called newline

Everything else is ignored, so non-whitespace characters can be used
as comments or to annotate the program. A common practice is to add a letter
indicating the whitespace character before that character:

- `S` for space
- `T` for tab
- `L` for linefeed

For example, here is the code to output the letter `H`:

```whitespace
S S S T	S S T	S S S L
T	L
T	L
S S 
```

[Wikipedia][1] indicates that Whitespace is an imperative, stack-based
language. It also has a "heap", which is actually just memory storage to an
arbitrary address. There are instructions for the following:

- Stack manipulation
- Arithmetic
- Heap access
- Flow control
- I/O

Numbers are of arbitrary length and are represented like this:

- Sign bit: space (`0`) for positive, tab (`1`) for negative
- Binary representation of the absolute value of the number, most-significant
  bit first: space for `0`, tab for `1`
- Terminated with a linefeed

For example, `100` (`110 0100`) would be represented as this:

| sign  | 1     | 1     | 0     | 0     | 1     | 0     | 0     | term     |
| ----  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | -------- |
| space | tab   | tab   | space | space | tab   | space | space | linefeed |

For further information on the Whitespace language, see the
[official tutorial][2]. Since creating a Whitespace program is very tedious,
you can use a [Whitespace assembler][3] instead.

[1]: https://en.wikipedia.org/wiki/Whitespace_(programming_language)
[2]: https://web.archive.org/web/20150618184706/http://compsoc.dur.ac.uk/whitespace/tutorial.php
[3]: https://github.com/rzuckerm/whitespace-asm
[4]: https://esolangs.org/wiki/Whitespace
