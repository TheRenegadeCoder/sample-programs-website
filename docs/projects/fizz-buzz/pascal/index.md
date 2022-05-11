---

title: Fizz Buzz in Pascal
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Pascal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).