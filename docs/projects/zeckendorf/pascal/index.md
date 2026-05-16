---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-11
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-11
layout: default
tags:
- pascal
- zeckendorf
title: Zeckendorf in Pascal
title1: Zeckendorf
title2: in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/pascal/how-to-implement-the-solution.md
- sources/programs/zeckendorf/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program Zeckendorf;

{$mode objfpc}{$H+}{$J-}{$modeswitch advancedrecords}

uses
  SysUtils;

const
  MAX_FIB_COUNT = {$IFDEF CPU64}92{$ELSE}46{$ENDIF};

type
  TNatural = {$IFDEF CPU64}UInt64{$ELSE}UInt32{$ENDIF};

  TZeckendorf = record
  private
    FFibonacciTable: array[0..MAX_FIB_COUNT - 1] of TNatural;
    FActualCount: Integer;
    FInitialized: Boolean;
    procedure Initialize;
  public
    procedure DecomposeAndPrint(ANumber: TNatural);
  end;

procedure TZeckendorf.Initialize;
var
  A, B, Next: TNatural;
begin
  if FInitialized then Exit;
  
  FFibonacciTable[0] := 1;
  FFibonacciTable[1] := 2;
  FActualCount := 2;
  A := 1;
  B := 2;

  while (High(TNatural) - A >= B) and (FActualCount < MAX_FIB_COUNT) do
  begin
    Next := A + B;
    FFibonacciTable[FActualCount] := Next;
    Inc(FActualCount);
    A := B;
    B := Next;
  end;
  FInitialized := True;
end;

procedure TZeckendorf.DecomposeAndPrint(ANumber: TNatural);
var
  I: Integer;
  IsFirstTerm: Boolean;
begin
  Initialize;

  if ANumber = 0 then Exit;

  IsFirstTerm := True;
  for I := FActualCount - 1 downto 0 do
  begin
    if FFibonacciTable[I] <= ANumber then
    begin
      if not IsFirstTerm then Write(', ') else IsFirstTerm := False;
      Write(FFibonacciTable[I]);
      Dec(ANumber, FFibonacciTable[I]);
    end;
    if ANumber = 0 then Break;
  end;
  WriteLn;
end;

procedure ShowUsage;
begin
  WriteLn('Usage: please input a non-negative integer');
  Halt(1);
end;

var
  InputVal: TNatural;
  Code: Integer;
  Z: TZeckendorf;
begin
  if (ParamCount <> 1) then ShowUsage;

  Val(ParamStr(1), InputVal, Code);
  if (Code <> 0) or (Pos('-', ParamStr(1)) > 0) then ShowUsage;

  if InputVal = 0 then
    WriteLn
  else
    Z.DecomposeAndPrint(InputVal);
end.
```

{% endraw %}

Zeckendorf in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).