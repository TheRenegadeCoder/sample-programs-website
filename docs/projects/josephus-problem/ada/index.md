---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-11
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- ada
- josephus-problem
title: Josephus Problem in Ada
title1: Josephus
title2: Problem in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/ada/how-to-implement-the-solution.md
- sources/programs/josephus-problem/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Ada](https://sampleprograms.io/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
pragma Ada_2022;
with Ada.Text_IO;       use Ada.Text_IO;
with Ada.Command_Line;  use Ada.Command_Line;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;

procedure Josephus is

   subtype Population is Positive;
   subtype Step_Size is Positive;

   function Survivor_Index
     (Count : Population; Skip : Step_Size) return Positive
   is
      Result : Natural := 0;
   begin
      for I in 2 .. Count loop
         Result := (@ + Skip) mod I;
      end loop;

      return Result + 1;
   end Survivor_Index;

   procedure Print_Usage is
   begin
      Put_Line
        ("Usage: please input the total number of people and number of people to skip.");
   end Print_Usage;

begin
   if Argument_Count /= 2 then
      Print_Usage;
      return;
   end if;

   declare
      Total : constant Population := Population'Value (Argument (1));
      Skip  : constant Step_Size := Step_Size'Value (Argument (2));
   begin
      Put_Line (Trim (Survivor_Index (Total, Skip)'Image, Ada.Strings.Left));
   end;

exception
   when Constraint_Error =>
      Print_Usage;
      Set_Exit_Status (Failure);
end Josephus;

```

{% endraw %}

Josephus Problem in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).