---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- maximum-subarray
- pascal
title: Maximum Subarray in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/pascal/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
   Writeln('Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"');
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

function MaximumSubarraySum(const Numbers: TIntegerList): integer;
var
   CurrentSum, MaxSum, Number, i: integer;
begin
   if Numbers.Count = 0 then
      Exit(0);

   CurrentSum := Numbers[0];
   MaxSum := Numbers[0];

   for i := 1 to Numbers.Count - 1 do
   begin
      Number := Numbers[i];
      if (CurrentSum + Number) > Number then
         CurrentSum := CurrentSum + Number
      else
         CurrentSum := Number;

      if CurrentSum > MaxSum then
         MaxSum := CurrentSum;
   end;

   Result := MaxSum;
end;

var
   InputList: TIntegerList;
begin
   if ParamCount <> 1 then
      ShowUsage;

   InputList := ParseIntegerList(ParamStr(1));
   try
      Writeln(MaximumSubarraySum(InputList));
   finally
      InputList.Free;
   end;
end.

```

{% endraw %}

Maximum Subarray in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).