---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: file-input-output-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- file-input-output
- pascal
title: File Input Output in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/pascal/how-to-implement-the-solution.md
- sources/programs/file-input-output/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program FileIO;

{$mode objfpc}{$H+}

uses
   SysUtils;

const
   DefaultFileName = 'output.txt';

function WriteToFile(const FileName: string): integer;
var
   F: TextFile;
begin
   Result := 1; // failure by default
   try
      AssignFile(F, FileName);
      Rewrite(F);

      try
         Writeln(F, 'A line of text');
         Writeln(F, 'Another line of text');
         Result := 0; // success
      finally
         CloseFile(F);
      end;
   except
      on E: Exception do
      begin
         Writeln('Error writing to file "', FileName, '": ', E.Message);
      end;
   end;
end;

function ReadFromFile(const FileName: string): integer;
var
   F: TextFile;
   Line: string;
   LinesRead: integer;
begin
   Result := 1; // failure by default
   LinesRead := 0;
   try
      AssignFile(F, FileName);
      Reset(F);

      try
         while not EOF(F) do
         begin
            ReadLn(F, Line);
            Writeln(Line);
            Inc(LinesRead);
         end;
         if LinesRead = 0 then
            Writeln('(File "', FileName, '" is empty)');
         Result := 0; // success
      finally
         CloseFile(F);
      end;
   except
      on E: Exception do
      begin
         Writeln('Error reading from file "', FileName, '": ', E.Message);
      end;
   end;
end;

var
   FileName: string;
begin
   FileName := DefaultFileName;

   if WriteToFile(FileName) <> 0 then
   begin
      ExitCode := 1;
      Exit;
   end;

   if ReadFromFile(FileName) <> 0 then
   begin
      ExitCode := 1;
      Exit;
   end;

   ExitCode := 0;
end.


```

{% endraw %}

File Input Output in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).