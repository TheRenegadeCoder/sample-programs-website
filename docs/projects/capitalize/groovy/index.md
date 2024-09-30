---
authors:
- robin
- rzuckerm
date: 2019-07-01
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-07-25
layout: default
tags:
- capitalize
- groovy
title: Capitalize in Groovy
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/groovy/how-to-implement-the-solution.md
- sources/programs/capitalize/groovy/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class Capitalize {
  static void main(String... args) {
    if(args?.length >= 1 && args[0]?.length() >= 1) {
      println args[0]?.capitalize()
    }
    else {
      println "Usage: please provide a string"
    }
  }
}

```

{% endraw %}

Capitalize in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- robin
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).