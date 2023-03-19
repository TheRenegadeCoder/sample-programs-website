---

title: Longest Common Subsequence in Mathematica
layout: default
date: 2022-04-28
last-modified: 2023-03-19

---

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Longest Common Subsequence option longestCommonSubsequence1 is just a Mathematica built-in
   (note that Mathematica LongestCommonSubsequence searches only for contiguous subsequences): *)

longestCommonSubsequence1 = LongestCommonSequence;

(* If that is considered cheating, then option longestCommonSubsequence2 implements it directly: *)

longestCommonSubsequence2 = Function[{l, r},
   (* if either list is empty, the LCS is also empty *)
   If[Length[l] == 0 \[Or] Length[r] == 0, {},
    (* if first element of both lists match, recurse after removing that element *)
    If[First[l] == First[r],
     Prepend[longestCommonSubsequence2[Rest[l], Rest[r]], First[l]],
     (* recurse by computing LCS of removing either first element from the left or from the right list *)
     Module[{ll = longestCommonSubsequence2[Rest[l], r], rr = longestCommonSubsequence2[l, Rest[r]]},
      (* pick whichever produces the longest LCS *)
      If[Length[ll] > Length[rr], ll, rr]]]]];

(* The outer function provides the 'user interface' (e.g., the string parsing): *)

longestCommonSubsequenceMain = Function[{left, right},
   Module[{e = "Usage: please provide two lists in the format \"1,2,3,4,5\""},
    Catch[
     StringRiffle[
      longestCommonSubsequence2 @@
       Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct two arguments to longestCommonSubsequence: left list, right list *)
        {
         If[StringLength[left] > 0, StringSplit[left, ", "], Throw[e]],
         If[StringLength[right] > 0, StringSplit[right, ", "], 
          Throw[e]]
         },
        {-1} (* at each leaf *)],
       ", "]]]];


(* Valid Tests *)

Print /@ Apply[longestCommonSubsequenceMain] /@ {
    {"1, 4, 5, 3, 15, 6", "1, 7, 4, 5, 11, 6"},
    {"1, 4, 8, 6, 9, 3, 15, 11, 6", "1, 7, 4, 5, 8, 11, 6"}
    };


(* Invalid Tests *)

longestCommonSubsequenceMain["3", ""]
```

{% endraw %}

[Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).