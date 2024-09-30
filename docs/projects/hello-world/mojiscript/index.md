---
authors:
- Noah Nichols
- Patrick Biffle
date: 2018-10-15
featured-image: hello-world-in-every-language.jpg
last-modified: 2018-10-17
layout: default
tags:
- hello-world
- mojiscript
title: Hello World in Mojiscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/mojiscript/how-to-implement-the-solution.md
- sources/programs/hello-world/mojiscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Mojiscript](https://sampleprograms.io/languages/mojiscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mojiscript
import log from 'mojiscript/console/log'
import pipe from 'mojiscript/core/pipe'
import run from 'mojiscript/core/run'

const state = 'Hello, World!'

const main = pipe ([
  log
])

run ({ state, main })
```

{% endraw %}

Hello World in [Mojiscript](https://sampleprograms.io/languages/mojiscript) was written by:

- Noah Nichols
- Patrick Biffle

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).