---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-11
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- ada
- longest-word
title: Longest Word in Ada
title1: Longest
title2: Word in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/ada/how-to-implement-the-solution.md
- sources/programs/longest-word/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](/projects/longest-word) in [Ada](/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
pragma Ada_2022;

with Ada.Text_IO;      use Ada.Text_IO;
with Ada.Command_Line; use Ada.Command_Line;

procedure Longest_Word is
   function Is_Separator (Ch : Character) return Boolean
   is (Ch = ' ' or else Ch = ASCII.LF or else Ch = ASCII.HT);

   function Longest_Word (S : String) return Natural is
      Max_Len : Natural := 0;
      Curr    : Natural := 0;
   begin
      for Ch of S loop
         if Is_Separator (Ch) then
            Max_Len := Natural'Max (Max_Len, Curr);
            Curr := 0;
         else
            Curr := @ + 1;
         end if;
      end loop;

      return Natural'Max (Max_Len, Curr);
   end Longest_Word;

   procedure Print_Usage is
   begin
      Put_Line ("Usage: please provide a string");
   end Print_Usage;

begin
   if Argument_Count /= 1 then
      Print_Usage;
      return;
   end if;

   declare
      Input : constant String := Argument (1);
   begin
      if Input'Length = 0 then
         Print_Usage;
         return;
      end if;

      Put_Line (Natural'Image (Longest_Word (Input)));
   end;

end Longest_Word;

```

{% endraw %}

Longest Word in [Ada](/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).