---
authors:
- Fredrick Karau
date: 2025-10-31
featured-image: merge-sort-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- haxe
- merge-sort
title: Merge Sort in Haxe
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/haxe/how-to-implement-the-solution.md
- sources/programs/merge-sort/haxe/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Haxe](https://sampleprograms.io/languages/haxe) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haxe
package;
import Sys;
class MergeSort {
    static function main() {
        var args = Sys.args();

        if(args.length != 1) {
            usage();
            return;
        }


        var input = args[0];

        var parts = input.split(",");
        var numbers = [];

        
        try {
            for (p in parts) {
                var trimmed = StringTools.trim(p);
                if (trimmed == "") throw "Invalid";
                numbers.push(Std.parseInt(trimmed));
            }
        } catch (e:Dynamic) {
            usage();
            return;
        }
        if(numbers.length < 2) {
            usage();
            return;
        }

        var sorted = mergeSort(numbers);
        trace(sorted.join(", "));
    }
    static function mergeSort(arr:Array<Int>):Array<Int> {
        if (arr.length <= 1) return arr;

        var mid = Std.int(arr.length / 2);
        var left = mergeSort(arr.slice(0, mid));
        var right = mergeSort(arr.slice(mid, arr.length));

        return merge(left, right);
}


    static function merge(left:Array<Int>, right:Array<Int>):Array<Int> {
        var result:Array<Int> = [];
        var i = 0;
        var j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result.push(left[i]);
                i++;
            } else {
                result.push(right[j]);
                j++;
            }
             }

        while (i < left.length) {
            result.push(left[i]);
            i++;
        }

        while (j < right.length) {
            result.push(right[j]);
            j++;
        }

        return result;
    }

    static function usage() {
        trace('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
    }
}
```

{% endraw %}

Merge Sort in [Haxe](https://sampleprograms.io/languages/haxe) was written by:

- Fredrick Karau

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).