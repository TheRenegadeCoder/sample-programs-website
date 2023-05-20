---
title: Reverse String in Pascal
layout: default
date: 2020-10-19
featured-image: reverse-string-in-every-language.jpg
last-modified: 2020-10-19

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program reversestring(input, output, stdErr);
(*Accept a String from Command Line, Reverse it & Print it*)
var
  i, j: Integer;
   buf, result: String;
begin
  buf := paramStr(1);
  setlength(result,length(buf));
  i:=1; 
  j:=length(buf);
  while (i<=j) do
    begin
      result[i]:=buf[j-i+1];
      inc(i);
    end;
    writeln(result);
end.
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- rzuckerm
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 19 2020 00:27:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).