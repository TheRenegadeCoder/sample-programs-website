---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-21
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- pascal
- remove-all-whitespace
title: Remove All Whitespace in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/pascal/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program RemoveAllWhitespace;

{$mode objfpc}{$H+}

uses
   SysUtils;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a string');
   Halt(1);
end;

function RemoveWhitespace(const S: string): string;
var
   builder: TStringBuilder;
   ch: char;
begin
   builder := TStringBuilder.Create;
   try
      for ch in S do
         case ch of
            ' ', #9, #10, #13: Continue;
            else
               builder.Append(ch);
         end;

      Result := builder.ToString;
   finally
      builder.Free;
   end;
end;

var
   Input: string;
   Output: string;
begin
   if ParamCount <> 1 then
      ShowUsage;

   Input := ParamStr(1);
   if Input = '' then
      ShowUsage;

   Output := RemoveWhitespace(Input);
   Writeln(Output);
end.

```

{% endraw %}

Remove All Whitespace in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).