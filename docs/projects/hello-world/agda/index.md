---
authors:
- rzuckerm
date: 2023-11-10
featured-image: hello-world-in-every-language.jpg
last-modified: 2023-11-10
layout: default
tags:
- agda
- hello-world
title: Hello World in Agda
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/agda/how-to-implement-the-solution.md
- sources/programs/hello-world/agda/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Agda](https://sampleprograms.io/languages/agda) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```agda
module HelloWorld where

open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit using (⊤)
open import Agda.Builtin.String using (String)

postulate putStrLn : String → IO ⊤
{-# FOREIGN GHC import qualified Data.Text as T #-}
{-# COMPILE GHC putStrLn = putStrLn . T.unpack #-}

main : IO ⊤
main = putStrLn "Hello, World!"

```

{% endraw %}

Hello World in [Agda](https://sampleprograms.io/languages/agda) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).