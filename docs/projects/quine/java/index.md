---
authors:
- Karl Marx
date: 2020-10-04
featured-image: quine-in-every-language.jpg
last-modified: 2020-10-04
layout: default
tags:
- java
- quine
title: Quine in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/java/how-to-implement-the-solution.md
- sources/programs/quine/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class Quine{public static void main(String[] args){char quote=34;String code="public class Quine{public static void main(String[] args){char quote=34;String code=;System.out.println(code.substring(0,84)+quote+code+quote+code.substring(84));}}";System.out.println(code.substring(0,84)+quote+code+quote+code.substring(84));}}

```

{% endraw %}

Quine in [Java](https://sampleprograms.io/languages/java) was written by:

- Karl Marx

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).