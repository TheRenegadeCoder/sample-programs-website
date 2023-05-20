---
title: Remove All Whitespace in Mathematica
layout: default
date: 2023-01-16
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-01-16

---

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual function operating on Mathematica strings is trivial: *)

removeAllWhitespace = StringDelete[WhitespaceCharacter];

(* The outer function provides the 'user interface': *)

removeAllWhitespaceMain = s \[Function]
   Catch[
    removeAllWhitespace[
     If[
      StringQ[s] \[And] \[Not] StringMatchQ[s, ""],
      s,
      Throw["Usage: please provide a string"]]]];


(* Valid Tests *)

Print /@ removeAllWhitespaceMain /@ {
    "RemoveAllWhitespace",
    " RemoveAllWhitespace",
    "RemoveAllWhitespace ",
    "Remove All Whitespace",
    "\tRemove\tAll\tWhitespace\t",
    "\nRemove\nAll\nWhitespace\n",
    "\rRemove\rAll\rWhitespace\r"
    };


(* Invalid Tests *)

removeAllWhitespaceMain[""]
```

{% endraw %}

[Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).