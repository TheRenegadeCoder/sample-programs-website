---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-09
layout: default
tags:
- ada
- capitalize
title: Capitalize in Ada
title1: Capitalize
title2: in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/ada/how-to-implement-the-solution.md
- sources/programs/capitalize/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](/projects/capitalize) in [Ada](/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO;      use Ada.Text_IO;
with Ada.Command_Line; use Ada.Command_Line;
with Ada.Characters.Handling;

procedure Capitalize is

   use Ada.Characters.Handling;

   function Capitalize (S : String) return String is
      Result : String := S;
   begin
      Result (Result'First) := To_Upper (Result (Result'First));
      return Result;
   end Capitalize;

begin
   if Argument_Count /= 1 or else Argument (1)'Length = 0 then
      Put_Line ("Usage: please provide a string");
      Set_Exit_Status (Failure);
      return;
   end if;

   Put_Line (Capitalize (Argument (1)));

end Capitalize;

```

{% endraw %}

Capitalize in [Ada](/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).