---
authors:
- Jeremy Grifski
- Maximillian Naza
- rzuckerm
date: 2018-05-29
featured-image: hello-world-in-solidity.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- solidity
title: Hello World in Solidity
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Solidity](https://sampleprograms.io/languages/solidity) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solidity
pragma solidity ^0.4.22;

contract helloWorld {
function renderHelloWorld () public pure returns (string) {
		return 'helloWorld';
	}
}
```

{% endraw %}

Hello World in [Solidity](https://sampleprograms.io/languages/solidity) was written by:

- Maximillian Naza

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
