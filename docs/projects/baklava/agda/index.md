---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- agda
- baklava
title: Baklava in Agda
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/agda/how-to-implement-the-solution.md
- sources/programs/baklava/agda/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Agda](https://sampleprograms.io/languages/agda) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```agda
-- Reference: https://rosettacode.org/wiki/FizzBuzz
module Baklava where

open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit using (⊤)
open import Agda.Builtin.String using (String)
open import Data.Bool using (if_then_else_)
open import Data.List using (List; []; _∷_; map)
open import Data.Nat using (ℕ; _<ᵇ_; _∸_; _*_; zero; suc)
open import Data.Nat.Show using (show)
open import Data.String using (unlines; replicate; _++_)

postulate putStrLn : String → IO ⊤
{-# FOREIGN GHC import qualified Data.Text as T #-}
{-# COMPILE GHC putStrLn = putStrLn . T.unpack #-}

range : (a b : ℕ) → List ℕ
range a zero    = []
range a (suc n) = a ∷ range (suc a) n

baklava-line : (n : ℕ) → String
baklava-line n = (replicate num-spaces ' ') ++ (replicate num-stars '*')
    where
        num-spaces = if n <ᵇ 10 then 10 ∸ n else n ∸ 10
        num-stars = 21 ∸ 2 * num-spaces

baklava : String
baklava = (unlines (map baklava-line (range 0 21)))

main : IO ⊤
main = putStrLn baklava

```

{% endraw %}

Baklava in [Agda](https://sampleprograms.io/languages/agda) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).