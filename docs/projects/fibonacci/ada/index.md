---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-10
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-10
layout: default
tags:
- ada
- fibonacci
title: Fibonacci in Ada
title1: Fibonacci
title2: in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/ada/how-to-implement-the-solution.md
- sources/programs/fibonacci/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](/projects/fibonacci) in [Ada](/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO;       use Ada.Text_IO;
with Ada.Command_Line;  use Ada.Command_Line;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;

procedure Fibonacci is

   procedure Print_Usage is
   begin
      Put_Line
        ("Usage: please input the count of fibonacci numbers to output");
   end Print_Usage;

   function Img (N : Natural) return String
   is (Trim (Natural'Image (N), Ada.Strings.Left));

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

      if N = 0 then
         return;
      end if;

      declare
         A, B : Natural := 1;
         Next : Natural;
      begin
         for I in 1 .. N loop
            Put_Line (Img (I) & ": " & Img (A));

            Next := A + B;
            A := B;
            B := Next;
         end loop;
      end;
   end;

end Fibonacci;

```

{% endraw %}

Fibonacci in [Ada](/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).