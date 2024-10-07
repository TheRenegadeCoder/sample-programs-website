---
authors:
- rzuckerm
date: 2024-10-07
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-07
layout: default
tags:
- baklava
- solidity
title: Baklava in Solidity
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/solidity/how-to-implement-the-solution.md
- sources/programs/baklava/solidity/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Solidity](https://sampleprograms.io/languages/solidity) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8;

contract Baklava {
    function main (string memory) public pure returns (string memory) {
        string memory output = '';
        for (int i = -10; i <= 10; i++) {
            int numSpaces = (i >= 0) ? i : -i;
            output = string.concat(output, strRepeat(numSpaces, ' '));
            output = string.concat(output, strRepeat(21 - 2 * numSpaces, '*'));
            output = string.concat(output, '\n');
        }

        return output;
    }

    function strRepeat(int n, string memory s) private pure returns (string memory) {
        string memory r = '';
        for (int i = 0; i < n; i++) {
            r = string.concat(r, s);
        }

        return r;
    }
}

```

{% endraw %}

Baklava in [Solidity](https://sampleprograms.io/languages/solidity) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).