---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-10
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-10
layout: default
tags:
- ada
- duplicate-character-counter
title: Duplicate Character Counter in Ada
title1: Duplicate Character
title2: Counter in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/ada/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](/projects/duplicate-character-counter) in [Ada](/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
pragma Ada_2022;

with Ada.Text_IO;             use Ada.Text_IO;
with Ada.Command_Line;        use Ada.Command_Line;
with Ada.Characters.Handling; use Ada.Characters.Handling;

with Ada.Containers.Hashed_Maps;

procedure Duplicate_Character_Counter is

   function Hash (C : Character) return Ada.Containers.Hash_Type
   is (Ada.Containers.Hash_Type (Character'Pos (C)));

   function Equivalent (L, R : Character) return Boolean
   is (L = R);

   package Char_Count_Map is new
     Ada.Containers.Hashed_Maps
       (Key_Type        => Character,
        Element_Type    => Natural,
        Hash            => Hash,
        Equivalent_Keys => Equivalent);

   use Char_Count_Map;

   function Count (Input : String) return Map is
      M : Map;
   begin
      for C of Input loop
         if Is_Alphanumeric (C) then
            if M.Contains (C) then
               M.Replace (C, M.Element (C) + 1);
            else
               M.Insert (C, 1);
            end if;
         end if;
      end loop;

      return M;
   end Count;

   procedure Print_Duplicates (Input : String; M : Map) is
      Seen  : array (Character) of Boolean := [others => False];
      Found : Boolean := False;
   begin
      for C of Input loop
         if Is_Alphanumeric (C)
           and then M.Contains (C)
           and then M.Element (C) > 1
           and then not Seen (C)
         then
            Put_Line (C & ":" & Natural'Image (M.Element (C)));
            Seen (C) := True;
            Found := True;
         end if;
      end loop;

      if not Found then
         Put_Line ("No duplicate characters");
      end if;
   end Print_Duplicates;

   Input : constant String :=
     (if Argument_Count = 1 then Argument (1) else "");

begin
   if Input = "" then
      Put_Line ("Usage: please provide a string");
      Set_Exit_Status (Failure);
      return;
   end if;

   declare
      M : constant Map := Count (Input);
   begin
      Print_Duplicates (Input, M);
   end;

end Duplicate_Character_Counter;

```

{% endraw %}

Duplicate Character Counter in [Ada](/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).