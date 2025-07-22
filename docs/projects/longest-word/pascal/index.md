---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- longest-word
- pascal
title: Longest Word in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/pascal/how-to-implement-the-solution.md
- sources/programs/longest-word/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program LongestWord;

{$mode objfpc}{$H+}

uses
   SysUtils;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a string');
   Halt(1);
end;

function FindLongestWordLength(const input: string): integer;
var
   i, currentLength, longestLength: integer;
begin
   currentLength := 0;
   longestLength := 0;

   for i := 1 to Length(input) do
      if input[i] in [' ', #9, #10, #13] then
      begin
         // Update longestLength if we encountered the end of a word
         if currentLength > longestLength then
            longestLength := currentLength;

         // Reset for the next word
         currentLength := 0;
      end
      else
         // Increase the length of the current word
         Inc(currentLength);

   // Final check for the last word in the string (if no trailing space)
   if currentLength > longestLength then
      longestLength := currentLength;

   Result := longestLength;
end;

var
   input: string;
   Result: integer;
begin
   if ParamCount <> 1 then
      ShowUsage;

   input := ParamStr(1);

   if Trim(input) = '' then
      ShowUsage;

   Result := FindLongestWordLength(input);
   Writeln(Result);
end.

```

{% endraw %}

Longest Word in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).