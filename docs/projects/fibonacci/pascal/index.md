---
title: Fibonacci in Pascal
layout: default
date: 2021-10-24
featured-image: fibonacci-in-every-language.jpg
last-modified: 2021-10-24

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program Fibonacci(input, output, stdErr);
(*Read count of fibonnaci numbers into a string

*)
var
  buf: String;
  count, check, first,second,result, i : integer;

begin
  (*Variable initialisation must be inside begin-end block*)
  first := 0;
  second := 1;
  result := 0;

  begin   
   buf:= paramStr(1);
   Val(buf, count, check);  
   (*If input is valid integer, check will be 0, else will be 1*)
   if (check <> 0)
   then
   begin
    writeln('Usage: please input the count of fibonacci numbers to output');
   end
   else
    for i := 1 to count do
    begin
    
    result := first + second;
    first := second;
    second := result;
    writeln(i, ': ', first);
    end;
   end;
end.
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- manasmithamn

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).