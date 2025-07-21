---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-21
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- pascal
- sleep-sort
title: Sleep Sort in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/pascal/how-to-implement-the-solution.md
- sources/programs/sleep-sort/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program SleepSort;

{$mode objfpc}{$H+}

uses
  {$ifdef unix}
  cthreads,
  {$endif}
  Classes,
  Generics.Collections,
  SysUtils,
  syncobjs;

type
  TIntegerList = specialize TList<integer>;

var
  Results: TIntegerList;
  Lock: TCriticalSection;

type
  TSleepSortThread = class(TThread)
  private
    FValue: integer;
  protected
    procedure Execute; override;
  public
    constructor Create(AValue: integer);
  end;

constructor TSleepSortThread.Create(AValue: integer);
begin
  inherited Create(False);
  FreeOnTerminate := False;
  FValue := AValue;
end;

procedure TSleepSortThread.Execute;
begin
  Sleep(FValue * 10);
  Lock.Acquire;
  try
    Results.Add(FValue);
  finally
    Lock.Release;
  end;
end;

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
begin
  Result := '';
  for i := 0 to List.Count - 1 do
  begin
    if i > 0 then
      Result += ', ';
    Result += IntToStr(List[i]);
  end;
end;

var
  Numbers: TIntegerList;
  Threads: array of TSleepSortThread;
  i: integer;
begin
  if ParamCount <> 1 then
    ShowUsage;

  Numbers := ParseIntegerList(ParamStr(1));
  Results := TIntegerList.Create;
  Lock := TCriticalSection.Create;

  try
    SetLength(Threads, Numbers.Count);

    for i := 0 to Numbers.Count - 1 do
      Threads[i] := TSleepSortThread.Create(Numbers[i]);

    for i := 0 to High(Threads) do
    begin
      Threads[i].WaitFor;
      Threads[i].Free;
    end;

    Writeln(FormatIntegerList(Results));
  finally
    Numbers.Free;
    Results.Free;
    Lock.Free;
  end;
end.


```

{% endraw %}

Sleep Sort in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).