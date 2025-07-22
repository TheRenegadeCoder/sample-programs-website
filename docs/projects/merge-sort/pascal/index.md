---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: merge-sort-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- merge-sort
- pascal
title: Merge Sort in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/pascal/how-to-implement-the-solution.md
- sources/programs/merge-sort/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program MergeSort;

{$mode objfpc}{$H+}

uses
   Classes,
   Generics.Collections,
   StrUtils,
   SysUtils;

type
   TIntegerList = specialize TList<integer>;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
   Halt(1);
end;

function ParseIntegerList(const S: string): TIntegerList;
var
   Tokens: TStringArray;
   Token: string;
   Value: integer;
begin
   if S.Trim = '' then
      ShowUsage;

   Tokens := S.Split([',']);
   if Length(Tokens) < 2 then
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

function FormatIntegerList(const List: TIntegerList): string;
var
   i: integer;
   Builder: TStringBuilder;
begin
   Builder := TStringBuilder.Create;
   try
      for i := 0 to List.Count - 1 do
      begin
         if i > 0 then
            Builder.Append(', ');
         Builder.Append(IntToStr(List[i]));
      end;
      Result := Builder.ToString;
   finally
      Builder.Free;
   end;
end;

procedure Merge(List: TIntegerList; Temp: TIntegerList; Left, Mid, Right: integer);
var
   i, j: integer;
begin
   Temp.Clear;
   i := Left;
   j := Mid + 1;

   // Merge two sorted halves [Left..Mid] and [Mid+1..Right] into Temp.
   while (i <= Mid) and (j <= Right) do
      if List[i] <= List[j] then
      begin
         Temp.Add(List[i]);
         Inc(i);
      end
      else
      begin
         Temp.Add(List[j]);
         Inc(j);
      end;

   // Copy any remaining elements from left half.
   while i <= Mid do
   begin
      Temp.Add(List[i]);
      Inc(i);
   end;

   // Copy any remaining elements from right half.
   while j <= Right do
   begin
      Temp.Add(List[j]);
      Inc(j);
   end;

   // Copy merged result back into original list.
   for i := 0 to Temp.Count - 1 do
      List[Left + i] := Temp[i];
end;

procedure MergeSort(List: TIntegerList);
var
   TempBuffer: TIntegerList;
   Length, Width, i, Left, Mid, Right: integer;

   function Min(const A, B: integer): integer; inline;
   begin
      Result := B;
      if A < B then
         Result := A;
   end;

begin
   Length := List.Count;

   // Nothing to sort if list has 0 or 1 elements.
   if Length <= 1 then Exit;

   TempBuffer := TIntegerList.Create;
   try
      // Bottom-up merge sort: iteratively merge sorted subarrays of increasing size
      Width := 1;
      while Width < Length do
      begin
         i := 0;
         while i < Length do
         begin
            Left := i;
            Mid := i + Width - 1;
            if Mid >= Length then break;  // No right half to merge

            Right := Mid + Width;
            if Right >= Length then
               Right := Length - 1;

            // Merge two sorted halves [Left..Mid] and [Mid+1..Right]
            Merge(List, TempBuffer, Left, Mid, Right);

            // Move to next pair of subarrays
            Inc(i, 2 * Width);
         end;
         Width := Width * 2;
      end;
   finally
      TempBuffer.Free;
   end;
end;

var
   Numbers: TIntegerList;
begin
   if ParamCount <> 1 then
      ShowUsage;

   Numbers := ParseIntegerList(ParamStr(1));
   try
      MergeSort(Numbers);
      Writeln(FormatIntegerList(Numbers));
   finally
      Numbers.Free;
   end;
end.

```

{% endraw %}

Merge Sort in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).