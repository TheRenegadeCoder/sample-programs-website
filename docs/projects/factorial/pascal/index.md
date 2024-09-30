---
authors:
- Mr Anand Somashekhara Rao Somavarapete
date: 2023-10-05
featured-image: factorial-in-every-language.jpg
last-modified: 2023-10-05
layout: default
tags:
- factorial
- pascal
title: Factorial in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/pascal/how-to-implement-the-solution.md
- sources/programs/factorial/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program factorial_calculate(input, output, stdErr);
(* Read a number from Commandline, Return it's factorial value
Cardinal, int-64 and qWord are the relevant data type to store long int in pascal.
With Cardinal data type, maximum factorial that can be computed is 34, 4926277576697053184
With int-64   data type, maximum factorial that can be computed is 44, 2673996885588443136
With qWord    data type, maximum factorial that can be computed is 65, 9223372036854775808
*)
var
 buf: String;
(* input_value, factorial, check:qWord;*)
i, check: integer;
input_value, factorial_value: qWord;
begin    
  buf:= paramStr(1);
  Val(buf, input_value, check);  
  if check <> 0
  then
    writeln('Usage: please input a non-negative integer')
  else
    if input_value < 0
      then
        writeln('Usage: please input a non-negative integer')
      else
      begin
        if (input_value = 0) then 
          writeln('1')
        else
          begin
            factorial_value := 1;
            for i := 1 to input_value do 
              begin
              factorial_value := factorial_value * i;
              end;
            writeln(factorial_value);
          end;

      end;
end.

```

{% endraw %}

Factorial in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Mr Anand Somashekhara Rao Somavarapete

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).