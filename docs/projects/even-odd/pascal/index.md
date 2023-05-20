---
title: Even Odd in Pascal
layout: default
date: 2020-10-18
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-18

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program a1(input, output, stdErr);
(* Read Number from commandline, print  Even or Odd *)
var
 buf: String;
 a, check:integer;
begin    
  buf:= paramStr(1);
    Val(buf, a, check) ;
    if check <> 0
    then
    writeln('Usage: please input a number')
    else
    begin
        if( (a mod 2) = 0) then
            begin
            writeln('Even'); 
            end         
        else
            begin
            writeln('Odd'); 
            end
    end
end.
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).