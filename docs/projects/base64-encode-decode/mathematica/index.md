---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-30
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-04-30
layout: default
tags:
- base64-encode-decode
- mathematica
title: Base64 Encode Decode in Mathematica
title1: Base64 Encode Decode
title2: in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/mathematica/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
ClearAll[base64Main];

NonEmptyStringQ = StringQ[#] && StringTrim[#] =!= "" &;

ValidBase64Q[s_String] :=
  StringLength[s] > 0 &&
  Mod[StringLength[s], 4] == 0 &&
  StringMatchQ[s, RegularExpression["^[A-Za-z0-9+/]*={0,2}$"]];

base64Main["encode", s_String?NonEmptyStringQ] :=
  StringTrim[ExportString[s, "Base64"]];

base64Main["decode", s_String?ValidBase64Q]  :=
  StringTrim[ImportString[s, "Base64"]];

base64Main[___] := "Usage: please provide a mode and a string to encode/decode";

validCases = {
  {"encode", "hello world"},
  {"encode", "They swam along the boat at incredible speeds."},
  {"encode", "1234567890"},
  {"encode", "xyz!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"},
  {"encode", "!  }gggIIT55;qqs!!Gjjb??=~~2$$+;;i::x..4kk,ppnoo"},
  {"decode", "aGVsbG8gd29ybGQ="},
  {"decode", "VGhleSBzd2FtIGFsb25nIHRoZSBib2F0IGF0IGluY3JlZGlibGUgc3BlZWRzLg=="},
  {"decode", "MTIzNDU2Nzg5MA=="},
  {"decode", "eHl6ISMkJSYoKSorLC0uLzo7PD0+P0BbXF1eX2B7fH1+"},
  {"decode", "ISAgfWdnZ0lJVDU1O3FxcyEhR2pqYj8/PX5+MiQkKzs7aTo6eC4uNGtrLHBwbm9v"}
};

invalidCases = {
  {},
  {""},
  {"encode"},
  {"encode", ""},
  {"decode"},
  {"decode", ""},
  {"blue", "Oh look a Pascal triangle"},
  {"decode", "hello+world"},
  {"decode", "hello world="},
  {"decode", "MTIzNDU2Nzg5M==="},
  {"decode", "MTIzNDU2=Nzg5M=="}
};

runTest[{a___}] := Print[base64Main[a]];
Scan[runTest, Join[validCases, invalidCases]];
```

{% endraw %}

Base64 Encode Decode in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).