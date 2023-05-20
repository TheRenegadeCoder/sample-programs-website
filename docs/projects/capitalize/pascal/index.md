---
title: Capitalize in Pascal
layout: default
date: 2020-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-17

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program Capitalise(input, output, stdErr);
(* Accept a String from commandline, convert first character to upper case
   Pascal Strings begins with 1, not 0
*)
var
buf: string;
begin
  buf := paramStr(1);
  if buf = ''  then
    writeln('Usage: please provide a string')
  else
    buf[1] := UpCase(buf[1]);
    writeln(buf);
end.
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 18 2020 11:48:50. The solution was first committed on Oct 17 2020 08:09:13. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).