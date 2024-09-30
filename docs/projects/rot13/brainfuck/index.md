---
authors:
- Jatin Pandey
date: 2023-12-18
featured-image: rot13-in-every-language.jpg
last-modified: 2023-12-18
layout: default
tags:
- brainfuck
- rot13
title: Rot13 in Brainfuck
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/brainfuck/how-to-implement-the-solution.md
- sources/programs/rot13/brainfuck/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Brainfuck](https://sampleprograms.io/languages/brainfuck) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```brainfuck
+>
+[
    ,[
        <[-]>
        [
            >+>+<<-
        ]>
        [<+>-]
        +>>++++++++
        [<-------->-]
        <-
        [<[-]>>>+[<+<+>>-]<[>+<-]<[<++>
            >>+[<+<->>-]<[>+<-]]>[<]<
        ]>>[-]<<<
        [[-]<[>>+>+<<<-]>>[<<+>>-]>>++++++++
        [
            <-------->-
        ]<->>++++[<++++++++>-]<-<
        [>>>+<<[>+>[-]<<-]>[<+>-]>[<<<<<+>>>>++++[<++++++++
            >-]>-]<<-<-
        ]>[<<<<[-]>>>>[<<<<->>>>-]]<<++++[<<++++++++>>-]<<-[>>+>+<<<-]>>
        [<<+>>-]+>>+++++[<----->-]<-
        [<[-]>>>+[<+<->>-]<[>+<-]<[<++>>>+[<+<+>>-]<[>+<-]]>[<]
        <]>>[-]<<<[[-]<<[>>+>+<<<-]>>[<<+>>-]+>------------[<[-]>>>+[<+<->>-]<[>+<-]<[<
            ++>>>+[<+<+>>-]<[>+<-]]>[<]<]>>[-]<<<<<------------->>[[-]+++++[<<+++++>>-]<<+>
        >]<[>++++[<<++++++++>>-]<-]>]<[-]++++++++[<++++++++>-]<+>]<.[-]+>>+<
    ]>[[-]<]<
]
<[
    [-]
    [Display error message
     Source: https://copy.sh/brainfuck/text.html
    ]
    >[-]<
    -[--->+<]>.
    +[--->+<]>+.
    ++[->+++<]>++.
    ++++++.
    --.
    +++[->+++<]>++.
    [-->+<]>+++.
    [-->+++++++<]>.
    ----.
    -------.
    ----.
    --[--->+<]>--.
    ++++[->+++<]>.
    --[--->+<]>-.
    [-->+++++++<]>.
    ++.
    ---.
    +++++++.
    [------>+<]>.
    -----.
    +.
    --[--->+<]>-.
    [->+++<]>+.
    -[->+++<]>.
    ---[->++++<]>-.
    +.
    --.
    ---------.
    +++++.
    -------.
    -[--->+<]>--.
    ---[->++++<]>.
    -----.
    [--->+<]>-----.
    +[->+++<]>++.
    +++++++++.
    -----------.
    -[--->+<]>----.
    +++++++.
    ---------.
    ++++.
    [-]
]

```

{% endraw %}

Rot13 in [Brainfuck](https://sampleprograms.io/languages/brainfuck) was written by:

- Jatin Pandey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).