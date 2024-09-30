---
authors:
- Jeremy Grifski
date: 2023-10-23
featured-image: baklava-in-every-language.jpg
last-modified: 2023-10-23
layout: default
tags:
- baklava
- pascal
title: Baklava in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/pascal/how-to-implement-the-solution.md
- sources/programs/baklava/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program Baklava;

var
  n, i, j, k, space: integer;
begin
  n := 11;
  space := n - 1;
  for i := 1 to n do
  begin
    for j := 1 to space do
      write(' ');
    space := space - 1;
    for k := 1 to (2 * i - 1) do
      write('*');
    writeln;
  end;
  space := 1;
  for i := (n - 1) downto 1 do
  begin
    for j := 1 to space do
      write(' ');
    space := space + 1;
    for k := (2 * i - 1) downto 1 do
      write('*');
    writeln;
  end;
end.

```

{% endraw %}

Baklava in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).