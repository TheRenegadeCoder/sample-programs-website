---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- pascal
- roman-numeral
title: Roman Numeral in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/pascal/how-to-implement-the-solution.md
- sources/programs/roman-numeral/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program RomanNumeral;

{$mode objfpc}{$H+}

uses
   SysUtils;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a string of roman numerals');
   Halt(1);
end;

function RomanToInt(const S: string): int64;
const
   RomanChars: array[0..6] of char = ('I', 'V', 'X', 'L', 'C', 'D', 'M');
   RomanValues: array[0..6] of integer = (1, 5, 10, 50, 100, 500, 1000);
var
   Value: array[char] of integer;
   i, len: integer;
   ch: char;
   Answer, PreviousValue, CurrentValue: int64;
begin
   FillChar(Value, SizeOf(Value), 0);

   for i := Low(RomanChars) to High(RomanChars) do
      Value[RomanChars[i]] := RomanValues[i];

   Answer := 0;
   PreviousValue := 0;
   len := Length(S);

   if len = 0 then
      Exit(0);

   for i := len downto 1 do
   begin
      ch := S[i];
      CurrentValue := Value[ch];
      if CurrentValue = 0 then
         raise Exception.Create('Error: invalid string of roman numerals');

      if CurrentValue < PreviousValue then
         Dec(Answer, CurrentValue)
      else
      begin
         Inc(Answer, CurrentValue);
         PreviousValue := CurrentValue;
      end;
   end;

   Result := Answer;
end;

var
   Input: string;
   Number: int64;
begin
   if ParamCount <> 1 then
      ShowUsage;

   Input := AnsiUpperCase(Trim(ParamStr(1)));

   try
      Number := RomanToInt(Input);
      Writeln(Number);
   except
      on E: Exception do
      begin
         Writeln(E.Message);
         Halt(1);
      end;
   end;
end.

```

{% endraw %}

Roman Numeral in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).