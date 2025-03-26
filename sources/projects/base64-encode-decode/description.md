### Introduction

Base64 is a popular method of encoding strings and other data. It can encode
images, text, JSON, and almost any other format as well. It is also URL-safe.

In this project you will be encoding normal text to Base64-encoded text and
decoding Base64-encoded text into normal text.

### Base64 Alphabet

From [Base64 Table from Wikipedia][1], this is the Base64 Alphabet:

| Index | Binary  | Char || Index | Binary  | Char || Index | Binary  | Char || Index | Binary  | Char |
| :---: | :-----: | :--: || :---: | :-----: | :--: || :---: | :-----: | :--: || :---: | :-----: | :--: |
|     0 | 000000  | A    ||    16 | 010000  | Q    ||    32 | 100000  | g    ||    48 | 110000  | w    |
|     1 | 000001  | B    ||    17 | 010001  | R    ||    33 | 100001  | h    ||    49 | 110001  | x    |
|     2 | 000010  | C    ||    18 | 010010  | S    ||    34 | 100010  | i    ||    50 | 110010  | y    |
|     3 | 000011  | D    ||    19 | 010011  | T    ||    35 | 100011  | j    ||    51 | 110011  | z    |
|     4 | 000100  | E    ||    20 | 010100  | U    ||    36 | 100100  | k    ||    52 | 110100  | 0    |
|     5 | 000101  | F    ||    21 | 010101  | V    ||    37 | 100101  | l    ||    53 | 110101  | 1    |
|     6 | 000110  | G    ||    22 | 010110  | W    ||    38 | 100110  | m    ||    54 | 110110  | 2    |
|     7 | 000111  | H    ||    23 | 010111  | X    ||    39 | 100111  | n    ||    55 | 110111  | 3    |
|     8 | 001000  | I    ||    24 | 011000  | Y    ||    40 | 101000  | o    ||    56 | 111000  | 4    |
|     9 | 001001  | J    ||    25 | 011001  | Z    ||    41 | 101001  | p    ||    57 | 111001  | 5    |
|    10 | 001010  | K    ||    26 | 011010  | a    ||    42 | 101010  | q    ||    58 | 111010  | 6    |
|    11 | 001011  | L    ||    27 | 011011  | b    ||    43 | 101011  | r    ||    59 | 111011  | 7    |
|    12 | 001100  | M    ||    28 | 011100  | c    ||    44 | 101100  | s    ||    60 | 111100  | 8    |
|    13 | 001101  | N    ||    29 | 011101  | d    ||    45 | 101101  | t    ||    61 | 111101  | 9    |
|    14 | 001110  | O    ||    30 | 011110  | e    ||    46 | 101110  | u    ||    62 | 111110  | +    |
|    15 | 001111  | P    ||    31 | 011111  | f    ||    47 | 101111  | v    ||    63 | 111111  | /    |
|       |         |      ||       |         |      ||       |         |      ||       | Padding | =    |

This alphabet is used for both encode and decode.

### Encode

Base64 encode works as follows:

- Split the data up into 3-byte chunks (let's ignore the case where the last chunk
  smaller than 3 bytes; that will be discussed later):
- For each 3-byte chunk:
  - Convert each byte to 8-bit binary, 24 bits in total.
  - Divide the 24-bit value into 4 groups of 6 bits.
  - Use each 6-bit group as an index into the above table to get Base64 characters.

For example, let's use the string `kitten`. The 3-byte chunks are `kit` and `ten`. Let's
focus on the first chunk: `kit`. Using 8-bit ASCII:

- `k` = `107` (`01101011`)
- `i` = `105` (`01101001`)
- `t` = `116` (`01110100`)

So, the 24-bit group is this:

```
01101011 01101001 01110100
```

Dividing this in 6-bit groups gives this:

```
011010 110110 100101 110100
```

Since it's easier to work with this as decimal, the table indices are these:

```
26 54 37 52
```

Looking these indices up in the table results a Base64 string of `a2l0`.
Following the same procedure for `ten` (left as an exercise for the reader),
the Base64 string is `dGVu`. Together, `kitten` encodes to `a2l0dGVu`.

For the case when the last chunk is not 3 bytes long, extend the last
bits with zeros until it is 6 bits long, and add padding characters until
the last Base64 string is 4 bytes long.

For example, let's consider the case where the last chunk is `k`:

- From the above example, `k` is `01101011`.
- Dividing this into 6-bit groups results in `011010 11`.
- Extending the last group results in `011010 110000`.
- Converting this to decimal results in `26 48`.
- Looking up those values in the table results in `aw`.
- Since this is only 2 bytes long, 2 padding characters are added: `aw==`.

For the final encode example, let's consider the case when the last chunk is
`ki`:

- From the above example, `ki` is `01101011 01101001`.
- Dividing this into 6-bit groups results in `011010 110110 1001`.
- Extending the last group results in `011010 110110 100100`.
- Convert this to decimal results in `26 54 36`.
- Looking up those values in the table results in `a2k`.
- Since this is only 3 bytes long, 1 padding character is added: `a2k=`.

### Decode

Before dividing into the algorithm for how to decode a Base64 string, let's
talk about some rules for what constitutes a valid Base64 string:

- Its length must be evenly divisible by 4.
- Only the last 4-byte chunk may have padding characters.
- The number of padding characters must be either 1 or 2.
- Each byte in the Base64 string must be in the table or be a padding
  character.

Assuming the Base64 string is valid, and ignoring the case where the last
4-byte chunk has padding characters, decode works as follows:

- Divide the Base64 string into 4-byte chunks.
- For each 4-byte chunk:
  - Look up each byte in the table to get the corresponding index.
  - Convert the indices into 4 groups of 6-bit values, 24 bits in total.
  - Divide the 24 bits into 3 8-bit bytes.

Let's use the Base64 string `a2l0dGVu`. The 4-byte chunks are `a2l0` and
`dGVu`. Let's focus on the first chunk: `a2l0`.

Looking up each byte in the table results in this:

- `a` is index `26` (`011010`)
- `2` is index `54` (`110110`)
- `l` is index `37` (`100101`)
- `0` is index `52` (`110100`)

Converting the binary indices to 8-bit groups results in this:

```
01101011 01101001 01110100
```

Convert this back to ASCII results in this:

- `01101011` (`107`) = `k`
- `01101001` (`105`) = `i`
- `01110100` (`116`) = `t`

Following the same procedure for `dGVu` (left as an exercise for the reader),
decodes to `ten`. Together, `a2l0dGVu` encodes to `kitten`.

For the case when the last chunk has pad characters, decode any complete
8-bit chunk, and ignore any chunk that is shorter than 8 bits.

For example, let's consider the case where the last chunk is `aw==`. Looking
up the non-pad characters results in this:

- `a` is index `26` (`011010`)
- `w` is index `48` (`110000`)

Dividing this into 8-byte groups results in this:

```
01101011 0000
```

Ignoring the last 4 bits results in this:

- `01101011` (`107`) = `k`

Therefore, this decodes to `k`.

For the final decode example, let's consider the case where the last chunk
is `a2k=`. Looking up the non-pad characters results in this:

- `a` is index `26` (`011010`)
- `2` is index `54` (`110110`)
- `k` is index `36` (`100100`)

Dividing this into 8-byte groups results in this:

```
01101011 01101001 00
```

Ignoring the last 2 bits results in this:

- `01101011` (107) = `k`
- `01101001` (105) = `i`

Therefore, this decodes to `ki`.

### Further Reading

You can read more about Base64 in [Wikipedia][2].

[1]: https://en.wikipedia.org/wiki/Base64#Base64_table_from_RFC_4648
[2]: https://en.wikipedia.org/wiki/Base64
