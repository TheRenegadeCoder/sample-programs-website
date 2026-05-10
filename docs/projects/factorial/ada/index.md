---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-10
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-10
layout: default
tags:
- ada
- factorial
title: Factorial in Ada
title1: Factorial
title2: in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/ada/how-to-implement-the-solution.md
- sources/programs/factorial/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Ada](https://sampleprograms.io/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO;      use Ada.Text_IO;
with Ada.Command_Line; use Ada.Command_Line;

procedure Factorial is

   procedure Print_Usage is
   begin
      Put_Line ("Usage: please input a non-negative integer");
   end Print_Usage;

   function Fact (N : Natural) return Natural is
      Result : Natural := 1;
   begin
      for I in 2 .. N loop
         Result := Result * I;
      end loop;
      return Result;
   end Fact;

   Max_Allowed : constant Natural := 12; -- Fact (13) > Natural'Last

begin
   if Argument_Count /= 1 then
      Print_Usage;
      return;
   end if;

   declare
      N : Natural;
   begin
      begin
         N := Natural'Value (Argument (1));
      exception
         when Constraint_Error =>
            Print_Usage;
            return;
      end;

      if N > Max_Allowed then
         Print_Usage;
         return;
      end if;

      Put_Line (Natural'Image (Fact (N)));

   end;

end Factorial;

```

{% endraw %}

Factorial in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).