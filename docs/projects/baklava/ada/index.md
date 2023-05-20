---
title: Baklava in Ada
layout: default
date: 2021-10-29
featured-image: baklava-in-every-language.jpg
last-modified: 2021-10-29

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ada](https://sampleprograms.io/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO; use Ada.Text_IO;

procedure Baklava is
  M : Integer := 11;
begin
   for I in 1 .. 11 loop
      for J in 1 .. (M-1) loop
        Put(" ");
      end loop;
      for K in 1 .. (2*I - 1) loop
        Put("*");
      end loop;
      M := M -1;
      Put_Line("");
   end loop;
   M:=2;
   for I in reverse 1 .. 10 loop
      for J in 1 .. (M-1) loop
        Put(" ");
      end loop;
      for K in 1 .. (2*I - 1) loop
        Put("*");
      end loop;
      M := M + 1;
      Put_Line("");
   end loop;
end Baklava;
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Gagan Agarwal

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).