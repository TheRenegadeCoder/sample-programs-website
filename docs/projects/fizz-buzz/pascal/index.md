---
title: Fizz Buzz in Pascal
layout: default
date: 2018-10-11
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-11

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program FizzBuzz(output);
var
   i : integer;
begin
   for i := 1 to 100 do
      if i mod 15 = 0 then
         writeln('FizzBuzz')
      else if i mod 3 = 0 then
         writeln('Fizz')
      else if i mod 5 = 0 then
         writeln('Buzz')
      else
         writeln(i)
end.
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Eduardo Rodríguez

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).