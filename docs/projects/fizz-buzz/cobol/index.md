---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-04-19
layout: default
tags:
- cobol
- fizz-buzz
title: Fizz Buzz in COBOL
title1: Fizz Buzz
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/cobol/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. fizz-buzz.

data division.
working-storage section.

01 counter     pic 9(3).
01 counter-out pic z(3).

procedure division.

main.
    perform varying counter from 1 by 1 until counter > 100

        evaluate true
            when function mod(counter, 15) = 0
                display "FizzBuzz"

            when function mod(counter, 3) = 0
                display "Fizz"

            when function mod(counter, 5) = 0
                display "Buzz"

            when other
                move counter to counter-out
                display function trim(counter-out)
        end-evaluate

    end-perform

    stop run.

```

{% endraw %}

Fizz Buzz in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).