---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-10
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-05-10
layout: default
tags:
- ada
- even-odd
title: Even Odd in Ada
title1: Even Odd
title2: in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/ada/how-to-implement-the-solution.md
- sources/programs/even-odd/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Ada](https://sampleprograms.io/languages/ada)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO;      use Ada.Text_IO;
with Ada.Command_Line; use Ada.Command_Line;

procedure Even_Odd is

   procedure Print_Usage is
   begin
      Put_Line ("Usage: please input a number");
   end Print_Usage;

begin
   if Argument_Count /= 1 then
      Print_Usage;
      return;
   end if;

   declare
      Value : Integer;
   begin
      Value := Integer'Value (Argument (1));
      Put_Line (if Value rem 2 = 0 then "Even" else "Odd");

   exception
      when Constraint_Error =>
         Print_Usage;
   end;

end Even_Odd;

```

{% endraw %}

Even Odd in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).