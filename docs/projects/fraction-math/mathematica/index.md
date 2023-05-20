---
title: Fraction Math in Mathematica
layout: default
date: 2023-01-21
featured-image: fraction-math-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Most the required behavior is already provided by the ToExpression built-in.
   It would be easy to simply print these out in a loop; however, in the spirit of
   keeping the mathematical operation separate from its presentation I opted to
   return the result as a list explicitly: *)

fractionMath = Function[{l, o, r},
   ToExpression[(* simply evaluate the string as Mathematica input *)
    (* format the three arguments as a single string, parenthesizing the operands for precedence *)
    StringTemplate["(``) `` (``)"][l, o, r]]];

(* The outer function provides the 'user interface': *)

fractionMathMain = l \[Function]
   Catch[
    Replace[{(* output formatting according to literal requirement *)
        (* False/True to be shown as 0/1 *)
        False -> 0, True -> 1,
        (* fractions to be displayed in-line *)
        x_Rational :> StringTemplate["``/``"][Numerator[x], Denominator[x]]
        }]@*
      fractionMath @@
     (* check input has no empty strings *)
     (If[# != "", #, Throw["Usage: ./fraction-math operand1 operator operand2"]] & /@ l)];


(* Valid Tests *)

Print /@ fractionMathMain /@ {
    {"2/3", "+", "4/5"},
    {"2/3", "*", "4/5"},
    {"2/3", "-", "4/5"},
    {"2/3", "/", "4/5"},
    {"2/3", "==", "4/5"},
    {"2/3", ">", "4/5"},
    {"2/3", "<", "4/5"},
    {"2/3", ">=", "4/5"},
    {"2/3", "<=", "4/5"},
    {"2/3", "!=", "4/5"}};


(* Invalid Tests *)

fractionMathMain[{"", "+", "4/5"}]
```

{% endraw %}

[Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).