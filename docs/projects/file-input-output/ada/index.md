---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-10
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-10
layout: default
tags:
- ada
- file-input-output
title: File Input Output in Ada
title1: File Input
title2: Output in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/ada/how-to-implement-the-solution.md
- sources/programs/file-input-output/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Ada](https://sampleprograms.io/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Exceptions;

procedure File_IO is

   File_Name : constant String := "output.txt";

   procedure Write_File is
      F : File_Type;
   begin
      Create (F, Out_File, File_Name);

      Put_Line (F, "Hello from Ada!");
      Put_Line (F, "This is a second line.");
      Put_Line (F, "File I/O is working.");

      Close (F);

   exception
      when Name_Error =>
         Put_Line ("Error: invalid file name");
      when Use_Error =>
         Put_Line ("Error: cannot create file");
   end Write_File;

   procedure Read_File is
      F : File_Type;
   begin
      Open (F, In_File, File_Name);

      while not End_Of_File (F) loop
         declare
            Line : constant String := Get_Line (F);
         begin
            Put_Line (Line);
         end;
      end loop;

      Close (F);

   exception
      when Name_Error =>
         Put_Line ("Error: file not found");
      when End_Error =>
         null;
   end Read_File;

begin
   Write_File;
   Read_File;
end File_IO;

```

{% endraw %}

File Input Output in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).