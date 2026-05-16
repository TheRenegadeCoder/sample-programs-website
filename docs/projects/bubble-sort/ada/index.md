---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-09
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-05-09
layout: default
tags:
- ada
- bubble-sort
title: Bubble Sort in Ada
title1: Bubble Sort
title2: in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/ada/how-to-implement-the-solution.md
- sources/programs/bubble-sort/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Ada](https://sampleprograms.io/languages/ada)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO;       use Ada.Text_IO;
with Ada.Command_Line;  use Ada.Command_Line;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;
with Ada.Containers.Vectors;

procedure Bubble_Sort is

   Parse_Error : exception;

   package Int_Vec is new
     Ada.Containers.Vectors (Index_Type => Natural, Element_Type => Integer);

   use Int_Vec;

   procedure Bubble_Sort (V : in out Vector) is
   begin
      if Natural (Length (V)) <= 1 then
         return;
      end if;

      for I in reverse First_Index (V) + 1 .. Last_Index (V) loop
         for J in First_Index (V) .. I - 1 loop
            if Element (V, J) > Element (V, J + 1) then
               Swap (V, J, J + 1);
            end if;
         end loop;
      end loop;
   end Bubble_Sort;

   function Parse_Int (S : String) return Integer is
      Clean : constant String := Trim (S, Ada.Strings.Both);
   begin
      if Clean'Length = 0 then
         raise Parse_Error;
      end if;

      return Integer'Value (Clean);
   exception
      when others =>
         raise Parse_Error;
   end Parse_Int;

   function Parse_List (S : String) return Vector is
      V     : Vector;
      Start : Positive := S'First;
      Count : Natural := 0;
   begin
      if S'Length = 0 then
         raise Parse_Error;
      end if;

      for I in S'Range loop
         if S (I) = ',' then
            if Start > I - 1 then
               raise Parse_Error; -- empty element like ",,"

            end if;

            Append (V, Parse_Int (S (Start .. I - 1)));
            Count := Count + 1;
            Start := I + 1;
         end if;
      end loop;

      -- last element
      if Start > S'Last then
         raise Parse_Error;
      end if;

      Append (V, Parse_Int (S (Start .. S'Last)));
      Count := Count + 1;

      if Count < 2 then
         raise Parse_Error;
      end if;

      return V;
   end Parse_List;

   procedure Print_Usage is
   begin
      Put_Line
        ("Usage: please provide a list of at least two integers to sort in the format ""1, 2, 3, 4, 5""");
   end Print_Usage;

   procedure Print_Vector (V : Vector) is
      function Img (X : Integer) return String
      is (Trim (Integer'Image (X), Ada.Strings.Left));
   begin
      for I in First_Index (V) .. Last_Index (V) loop
         Put (Img (Element (V, I)));

         if I /= Last_Index (V) then
            Put (", ");
         end if;
      end loop;

      New_Line;
   end Print_Vector;

begin
   if Argument_Count /= 1 then
      Print_Usage;
      Set_Exit_Status (Failure);
      return;
   end if;

   declare
      V : Vector;
   begin
      V := Parse_List (Argument (1));
      Bubble_Sort (V);
      Print_Vector (V);

   exception
      when Parse_Error | Constraint_Error =>
         Print_Usage;
         Set_Exit_Status (Failure);
   end;

end Bubble_Sort;

```

{% endraw %}

Bubble Sort in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).