---
authors:
- Zia
date: 2025-01-18
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-18
layout: default
tags:
- fizz-buzz
- haxe
title: Fizz Buzz in Haxe
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/haxe/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/haxe/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Haxe](https://sampleprograms.io/languages/haxe) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haxe
class FizzBuzz {
	static public function main():Void {
		for (i in 1...101) {
			var div3 = (i % 3 == 0);
			var div5 = (i % 5 == 0);
			Sys.println(div3 ? (div5 ? "FizzBuzz" : "Fizz") : (div5 ? "Buzz" : '$i'));
		}
	}
}

```

{% endraw %}

Fizz Buzz in [Haxe](https://sampleprograms.io/languages/haxe) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).