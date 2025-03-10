This program can encode text to base64-encoded text, and it can decode
base64-encoded text into normal text.

Base64 is a popular method of encoding strings and other data. It can encode
images, text, JSON, and almost any other format as well.

It is also often URL-safe.

Base64 works by splitting the data into 6-bit segments, which are then mapped
to a character in the table.

For example, let's use the string `six`.

This would be split into `1110011 1101001 1111000`. However, these are 8-bit
groups. Base64 needs 6-bit groups. So this turns into `111001 111010 011111
000` (in decimal: `57 58 31`).

Then, we take an index from a character table. Character 57 is `c`, so we add that.

Once we've added all the characters, we're done!

You can read more about base64 on [Wikipedia](https://en.wikipedia.org/wiki/Base64).
