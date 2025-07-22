---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- longest-common-subsequence
- pascal
title: Longest Common Subsequence in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/pascal/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program LongestCommonSubsequence;

{$mode objfpc}{$H+}

uses
   Generics.Collections,
   SysUtils;

type
   TIntegerList = specialize TList<integer>;

procedure ShowUsage;
begin
   Writeln('Usage: please provide two lists in the format "1, 2, 3, 4, 5"');
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

function LongestCommonSubsequence(const A, B: TIntegerList): TIntegerList;
var
   PreviousRow, CurrentRow: array of integer;
   i, j: integer;
begin
   if B.Count > A.Count then
      Exit(LongestCommonSubsequence(B, A));

   SetLength(PreviousRow, B.Count + 1);
   SetLength(CurrentRow, B.Count + 1);

   // Build the DP table
   for i := 1 to A.Count do
   begin
      for j := 1 to B.Count do
         if A[i - 1] = B[j - 1] then
            CurrentRow[j] := PreviousRow[j - 1] + 1
         else
         if CurrentRow[j - 1] > PreviousRow[j] then
            CurrentRow[j] := CurrentRow[j - 1]
         else
            CurrentRow[j] := PreviousRow[j];

      PreviousRow := CurrentRow;
      SetLength(CurrentRow, B.Count + 1);
   end;

   // Reconstruct the LCS from the DP table
   Result := TIntegerList.Create;
   i := A.Count;
   j := B.Count;

   while (i > 0) and (j > 0) do
      if A[i - 1] = B[j - 1] then
      begin
         // If they match, append
         Result.Add(A[i - 1]);
         Dec(i);
         Dec(j);
      end
      else if PreviousRow[j] > CurrentRow[j - 1] then
         // Move up if the top cell has a greater value
         Dec(i)
      else
         // Move left if the left cell has a greater value
         Dec(j);

   Result.Reverse;
end;


var
   ListA, ListB, LCSResult: TIntegerList;
   i: integer;
begin
   if ParamCount <> 2 then
      ShowUsage;

   try
      try
         ListA := ParseIntegerList(ParamStr(1));
         ListB := ParseIntegerList(ParamStr(2));

         if (ListA.Count = 0) or (ListB.Count = 0) then
            ShowUsage;

         LCSResult := LongestCommonSubsequence(ListA, ListB);

         if LCSResult.Count = 0 then
            Writeln('No common subsequence.')
         else
            Writeln(FormatIntegerList(LCSResult));
      except
         on E: Exception do
            ShowUsage;
      end;
   finally
      ListA.Free;
      ListB.Free;
      LCSResult.Free;
   end;
end.

```

{% endraw %}

Longest Common Subsequence in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).