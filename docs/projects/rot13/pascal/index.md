---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-21
featured-image: rot13-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- pascal
- rot13
title: Rot13 in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/pascal/how-to-implement-the-solution.md
- sources/programs/rot13/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program Rot13;

{$mode objfpc}{$H+}

uses
   SysUtils;

procedure ShowUsage;
begin
   Writeln('Usage: please provide a string to encrypt');
   Halt(1);
end;

function Rot13(const S: string): string;
var
   ch: char;
begin
   Result := '';
   for ch in S do
      case ch of
         'A'..'Z':
            Result += Chr(((Ord(ch) - Ord('A') + 13) mod 26) + Ord('A'));
         'a'..'z':
            Result += Chr(((Ord(ch) - Ord('a') + 13) mod 26) + Ord('a'));
         else
            Result += ch;
      end;
end;

var
   Input: string;
begin
   if ParamCount <> 1 then
      ShowUsage;

   Input := ParamStr(1);
   if Input = '' then
      ShowUsage;

   Writeln(Rot13(Input));
end.

```

{% endraw %}

Rot13 in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).