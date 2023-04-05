---

title: Binary Search in Mathematica
layout: default
date: 2022-04-28
last-modified: 2023-04-04

---

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Binary search option binarySearch1 uses the built-in, modified to
return Null in case the element is not found: *)

Needs["Combinatorica`"]

binarySearch1 = If[IntegerQ[#], #, Null] & @*
Combinatorica`BinarySearch;

(* If that is considered cheating, then option binarySearch2 implements it
using 'primitives': *)

binarySearch2 = Function[{l, n},
   NestWhile[ (* keep subdividing the search interval *)
    Apply[(* convert the single two-element list argument to two arguments *)
     Function[{i, j},(* subdivide the given interval into a smaller one containing the item sought *)
      Module[{m = Floor[(i + j)/2], me},(* use some definite element as the midpoint to test *)
       me = l[[m]];
       Which[
        (* Did we find the element we're searching for? *)
        me == n, m,
        (* Element is before the midpoint?  Then either keep searching, or give up *)
        n < me, If[i < m, {i, m - 1}, Null],
        (* Element is after the midpoint?  Then either keep searching, or give up *)
        n > me, If[m < j, {m + 1, j}, Null]]]]],
    {1, Length[l]} (* begin by considering the entire list to search within *),
    ListQ (* while we are still searching *)]];

(* The outer function does the string parsing: *)

binarySearchMain = Function[{l, i},
   Module[{e = "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"},
    Catch[
     If[
      (* convert position to "true" or Null to "false" *)
      IntegerQ[binarySearch2 @@ Map[
         (* convert string to integer, or throw *)
         s \[Function] If[StringMatchQ[s, DigitCharacter ..],
           FromDigits[s],
           Throw[e]],
         (* construct two arguments to binary search: list of search array, item to search; as strings *)
         {StringSplit[If[StringLength[l] > 0, l, Throw[e]], ", "], i},
         {-1} (* at each leaf *)]],
      "true", "false"]]]];

(* Valid Tests *)
Print /@ Apply[binarySearchMain] /@ {
    {"1, 4, 5, 11, 12", "4"},
    {"1, 3, 5, 7", "1"},
    {"1, 3, 5, 7", "7"},
    {"5", "5"},
    {"5", "7"},
    {"1, 3, 5, 6", "7"}};

(* Invalid Tests *)
binarySearchMain["1, 2, 3, 4",""]
binarySearchMain["", "5"]

(* Not checking the 'list is unsorted' invalid test. *)
```

{% endraw %}

[Binary Search](https://sampleprograms.io/projects/binary-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).