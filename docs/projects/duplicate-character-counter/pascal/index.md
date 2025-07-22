---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-22
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-07-22
layout: default
tags:
- duplicate-character-counter
- pascal
title: Duplicate Character Counter in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/pascal/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program DuplicateCharacterCounter;

{$mode objfpc}{$H+}

uses
   Classes,
   Generics.Collections,
   SysUtils;

type
   TCountDictionary = specialize TDictionary<char, integer>;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a string');
   Halt(1);
end;

function IsAlphanumeric(c: char): boolean;
begin
  Result := CharInSet(c, ['0'..'9', 'A'..'Z', 'a'..'z']);
end;

procedure CountDuplicates(const Str: string);
var
  Counts: TCountDictionary;
  Outputted: TCountDictionary;
  Character: char;
  CurrentCount: integer;
  HasDuplicates: boolean;
begin
  Counts := TCountDictionary.Create;
  Outputted := TCountDictionary.Create;
  try
    // Count all alphanumeric characters
    for Character in Str do
      if IsAlphanumeric(Character) then
      begin
        if not Counts.TryGetValue(Character, CurrentCount) then
          Counts.Add(Character, 1)
        else
          Counts[Character] := CurrentCount + 1;
      end;

    HasDuplicates := False;

    // Output duplicates in order of first appearance
    for Character in Str do
      if Counts.TryGetValue(Character, CurrentCount) and (CurrentCount > 1) and
         not Outputted.ContainsKey(Character) then
      begin
        Writeln(Character, ': ', CurrentCount);
        Outputted.Add(Character, 1);
        HasDuplicates := True;
      end;

    if not HasDuplicates then
      Writeln('No duplicate characters');
  finally
    Counts.Free;
    Outputted.Free;
  end;
end;

var
  InputStr: string;
begin
  if ParamCount <> 1 then
    ShowUsage;

  InputStr := Trim(ParamStr(1));
  if InputStr = '' then
    ShowUsage;

  CountDuplicates(InputStr);
end.



```

{% endraw %}

Duplicate Character Counter in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).