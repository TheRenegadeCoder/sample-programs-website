---
authors:
- Jeremy Grifski
- rzuckerm
date: 2022-04-28
featured-image: hello-world-in-solidity.jpg
last-modified: 2023-12-16
layout: default
tags:
- hello-world
- solidity
title: Hello World in Solidity
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/solidity/how-to-implement-the-solution.md
- sources/programs/hello-world/solidity/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Solidity](https://sampleprograms.io/languages/solidity) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8;

contract HelloWorld {
    function main (string memory) public pure returns (string memory) {
        return 'Hello, World!\n';
    }
}

```

{% endraw %}

Hello World in [Solidity](https://sampleprograms.io/languages/solidity) was written by:

- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

While the format of Solidity looks a bit different from the more popular
programming languages today, what's happening behind is fairly straightforward.

First we import the version of Solidity we'd like to use. Then we create a
function and specify we'd only like to return a string. And, voila!


## How to Run the Solution

If you want to run the solution, remix provides an [IDE][5] you can visit to write
and execute the smart contract. Every piece of code written in Solidity, or any
blockchain programming language, is considered a smart contract.

[5]: https://remix-project.org/
