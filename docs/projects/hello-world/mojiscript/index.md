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