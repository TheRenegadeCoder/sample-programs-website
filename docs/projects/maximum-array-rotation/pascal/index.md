---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-21
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- maximum-array-rotation
- pascal
title: Maximum Array Rotation in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/pascal/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program MaximumArrayRotation;

{$mode objfpc}{$H+}

uses
   Classes,
   Generics.Collections,
   SysUtils;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a list of integers (e.g. "8, 3, 1, 2")');
   Halt(1);
end;

type
   TIntegerList = specialize TList<integer>;

function ParseIntegerList(const S: string): TIntegerList;
var
   Tokens: TStringArray;
   Token: string;
   Value: integer;
begin
   if S.Trim = '' then
      ShowUsage;

   Tokens := S.Split([',']);
   if Length(Tokens) = 0 then
      ShowUsage;

   Result := TIntegerList.Create;
   for Token in Tokens do
   begin
      if not TryStrToInt(Trim(Token), Value) then
      begin
         Result.Free;
         ShowUsage;
      end;
      Result.Add(Value);
   end;
end;

function MaximumRotationSum(const Numbers: TIntegerList): integer;
var
   N, i, TotalSum, CurrentWeightedSum, MaxWeightedSum: integer;
begin
   N := Numbers.Count;
   if N = 0 then
      ShowUsage;

   TotalSum := 0;
   CurrentWeightedSum := 0;
   for i := 0 to N - 1 do
   begin
      TotalSum += Numbers[i];
      CurrentWeightedSum += Numbers[i] * i;
   end;

   MaxWeightedSum := CurrentWeightedSum;

   for i := 1 to N - 1 do
   begin
      CurrentWeightedSum := CurrentWeightedSum + TotalSum - N * Numbers[N - i];
      if MaxWeightedSum < CurrentWeightedSum then
         MaxWeightedSum := CurrentWeightedSum;
   end;

   Result := MaxWeightedSum;
end;

var
   InputList: TIntegerList;
begin
   if ParamCount <> 1 then
      ShowUsage;

   InputList := ParseIntegerList(ParamStr(1));
   try
      Writeln(MaximumRotationSum(InputList));
   finally
      InputList.Free;
   end;
end.

```

{% endraw %}

Maximum Array Rotation in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).