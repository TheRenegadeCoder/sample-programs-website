---
title: Baklava in Piet
layout: default
date: 2023-04-30
featured-image: baklava-in-piet.jpg
tags: [piet, baklava]
authors:
  - rzuckerm

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Piet](https://sampleprograms.io/languages/piet) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

![Baklava in Piet](/projects/baklava/piet/baklava.png)

[Baklava](https://sampleprograms.io/projects/baklava) in [Piet](https://sampleprograms.io/languages/piet) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

## Introduction

Piet is an [esoteric programming language][4]. Esoteric programming languages
make it difficult to implement even the simplest task, and this was my first
foray into such languages. If that wasn't difficult enough, Piet is a
graphical language, so you can't just pop into a text editor to create a
program. Instead, you have to use an [online editor][6] to even create a
program. To make things even more interesting, Piet uses a rotating color
palette, where the color of the next instruction depends upon the current
instruction. Finally, it is a stack-based language, so programming in it is
akin to programming an old [Hewlett-Packard calculator][5]. If you'd like to
learn more about the Piet language, see the [Official Site][3].

Without further ado, let's dive in the implementation!

## High-Level Overview

This sample program implements Baklava using two main loops:

1.  Output the top 10 lines:

    - Output `n` spaces.
    - Output `21 - 2*n` asterisks.
    - Output a newline.

    where `n` equals 1, 2, ..., 10.

2.  Output the bottom 11 lines:

    - Output 21 asterisks.
    - Output a newline.

    then:

    - Output `10 - floor(m / 2)` spaces.
    - Output `m` asterisks.
    - Output a newline.

    where `m` equals 19, 17, ..., 1.

If this is enough for you, then just jump to the [Credits section](#credits).
Otherwise, strap yourself in, and prepare for a very detailed description that
goes through what each codel (code element) does.

## Very Detailed Description

ASCII characters need to be encoded as numbers. The following numbers are
used:

- space: 32
- asterisk: 42
- newline: 10

Instructions are shown in the following format:

- X/Y coordinates of the program counter
- Instruction
- Stack contents

The direction pointer (DP), controls the flow of the program. The program
starts at `(0, 0)`, and DP points to the right. When DP hits an edge or black
cell, it rotates clockwise. The program terminates when there is nowhere to
go.

White cells are considered to be no-ops (do-nothing instructions).

The program is divided into a number parts which are detailed in subsequent
sections of this article. The parts are annotated with letters as follows:

![Annotated Baklava in Piet](/assets/images/projects/baklava/piet/baklava-annotated.png)

Click
<a href="/assets/images/projects/baklava/piet/baklava-annotated.png" target="_blank">here</a>
to open the diagram in a separate page so that you can refer back to it.

### Output Top 10 Lines (A thru G)

#### Space Loop Initialization (A)

`n = 10`:

```
( 0, 0): push 2  # 2
( 2, 0): push 5  # 2, 5
( 4, 0): mult    # 10 (n)
```

`k = n`:

```
( 5, 0): dup     # 10 (n), 10 (k)
```

#### Space Loop (B)

Output `" "`:

```
( 6, 0): push 4  # n, k, 4
(10, 0): dup     # n, k, 4, 4
(11, 0): mult    # n, k, 16
(12, 0): dup     # n, k, 16, 16
(13, 0): add     # n, k, 32
(14, 0): outc    # n, k
```

`k = k - 1`:

```
(15, 0): push 1  # n, k, 1
(16, 0): sub     # n, k - 1
```

Check whether the `k` is greater than `0` and branch accordingly:

```
(17, 0): dup     # n, k, k
(18, 0): push 1  # n, k, k, 1
(19, 0): not     # n, k, k, 0
(20, 0): gt      # n, k, 1 if k > 0 else 0
(21, 0): DP+     # n, k
```

If `k` is greater than `0`, DP rotates clockwise, so a bunch of no-ops are
executed, and the program goes back to the beginning of B. Otherwise, DP is
unchanged, so the program continues on to the beginning of C.

#### Asterisk Loop Initialization (C)

Drop `k`:

```
(22, 0): pop     # n
```

`m = 21 - 2 * n`:

```
(23, 0): dup     # n, n
(24, 0): push 1  # n, n, 1
(25, 0): not     # n, n, 0
(26, 0): push 1  # n, n, 0, 1
(27, 0): sub     # n, n, -1
(28, 0): mult    # n, -n
(29, 0): dup     # n, -n, -n
(30, 0): add     # n, -2 * n
(31, 0): push 3  # n, -2 * n, 3
(32, 1): push 7  # n, -2 * n, 3, 7
(34, 0): mult    # n, -2 * n, 21
(35, 0): add     # n, 21 - 2 * n (m)
```

#### Asterisk Loop (D)

Output `"*"`:

```
(36, 0): push 3  # n, m, 3
(39, 0): dup     # n, m, 3, 3
(40, 0): add     # n, m, 6
(41, 0): dup     # n, m, 6, 6
(42, 0): dup     # n, m, 6, 6, 6
(43, 0): mult    # n, m, 6, 36
(44, 0): add     # n, m, 42
(45, 0): outc    # n, m
```

`m = m - 1`:

```
(46, 0): push 1  # n, m, 1
(47, 0): sub     # n, m - 1
```

Check whether `m` is greater than `0` and branch accordingly:

```
(48, 0): dup     # n, m, m
(49, 0): push 1  # n, m, m , 1
(50, 0): not     # n, m, m , 0
(51, 0): gt      # n, m, 1 if m > 0 else 0
(52, 0): DP+     # n, m
```

If `m` is greater than `0`, DP rotates clockwise, so a bunch of no-ops are
executed, and the program goes back to the beginning of D. Otherwise, DP is
unchanged, so the program continues on to the beginning of E.

#### Output Newline (E)

Drop `m`:

```
(53, 0): pop     # n
```

Output `"\n"`:

```
(54, 0): push 2  # n, 2
(55, 1): push 5  # n, 2, 5
(53, 3): mult    # n, 10
(52, 3): outc    # n
```

#### Check If Last Line (F)

`n = n - 1`:

```
(51, 3): push 1  # n, 1
(50, 3): sub     # n - 1
```

Check if `n` is greater than `0` and branch accordingly:

```
(49, 3): dup     # n, n
(48, 3): push 1  # n, n, 1
(47, 3): not     # n, n, 0
(46, 3): gt      # n, 1 if n > 0 else 0 (q)
(45, 3): not     # n, 1 - q
(44, 3): dup     # n, 1 - q, 1 - q
(43, 3): dup     # n, 1 - q, 1 - q, 1 - q
(42, 3): add     # n, 1 - q, 2 * (1 - q)
(41, 3): add     # n, 3 * (1 - q)
(40, 3): DP+     # n
```

where:

```
3 * (1 - q) = 0 if n > 0 else 3
```

If `n` is greater than `0`, DP is unchanged, so the program goes to the
beginning of G. Otherwise, DP is rotated 3 steps clockwise, which is the same
as 1 step counter-clockwise, so the program goes to the beginning of H.

#### Set Up For Next Iteration (G)

`k = n`:

```
(39,  3): dup     # n, k
```

The program then executes a bunch of no-ops and goes back to the beginning of B.

### Output Bottom 11 Lines (H thru N)

#### Asterisk Loop Initialization (H)

Drop `n`:

```
(39, 4): pop     # empty
```

Skip through a bunch of no-ops. Then, rotate DP 3 steps clockwise (1 step
counter-clockwise):

```
( 4, 5): push 3  # 3
( 1, 5): DP+     # empty
```

Skip through a no-op. Then, set `m = 21`:

```
( 0, 7): push 3  # 3
( 0, 8): push 7  # 3, 7
( 5, 7): mult    # 21 (m)
```

`k = m`:

```
( 6, 7): dup     # m, k
```

#### Asterisk Loop (I)

Output `"*"`:

```
( 7, 7): push 3  # m, k, 3
(10, 7): dup     # m, k, 3, 3
(11, 7): add     # m, k, 6
(12, 7): dup     # m, k, 6, 6
(13, 7): dup     # m, k, 6, 6, 6
(14, 7): mult    # m, k, 6, 36
(15, 7): add     # m, k, 42
(16, 7): outc    # m, k
```

`k = k - 1`:

```
(17, 7): push 1  # m, k, 1
(18, 7): sub     # m, k - 1
```

Check if `k` is greater than `0` and branch accordingly:

```
(19, 7): dup     # m, k, k
(20, 7): push 1  # m, k, k, 1
(21, 7): not     # m, k, k, 0
(22, 7): gt      # m, k, 1 if k > 0 else 0
(23, 7): DP+     # m, k
```

If `k` is greater than `0`, DP rotates clockwise, so a bunch of no-ops are
executed, and the program goes back to the beginning of I. Otherwise, DP is
unchanged, so the program continues on to the beginning of J.

#### Output Newline and Check If Last Line (J)

Drop `k`:

```
(24, 7): pop     # m
```
Output `"\n"`:

```
(25, 7): push 2  # m, 2
(27, 7): push 5  # m, 2, 5
(29, 7): mult    # m, 10
(30, 7): outc    # m
```

`m = m - 2`:

```
(31, 7): push 2  # m, 2
(33, 7): sub     # m - 2
```

Check if `m` is greater than `0` and branch accordingly:

```
(34, 7): dup     # m, m
(35, 7): push 1  # m, m, 1
(36, 7): not     # m, m, 0
(37, 7): gt      # m, 1 if m > 0 else 0
(38, 7): not     # m, 0 if m > 0 else 1
(39, 7): DP+     # m
```

If `m` is greater than 0, DP is unchanged, so continue on to the beginning of
K. Otherwise, DP is rotated clockwise, so go to the beginning of N.

#### Space Loop Initialization (K)

`n = 10 - floor(m / 2)`:

```
(40, 7): dup     # m, m
(41, 7): push 2  # m, m, 2
(43, 7): div     # m, floor(m / 2)
(44, 7): push 1  # m, floor(m / 2), 1
(45, 7): not     # m, floor(m / 2), 0
(46, 7): push 1  # m, floor(m / 2), 0, 1
(47, 7): sub     # m, floor(m / 2), -1
(48, 7): mult    # m, -floor(m / 2)
(49, 7): push 2  # m, -floor(m / 2), 2
(51, 7): push 5  # m, -floor(m / 2), 2, 5
(53, 7): mult    # m, -floor(m / 2), 10
(54, 7): add     # m, 10 - floor(m / 2) (n)
```

#### Space Loop (L)

Output `" "`:

```
(55, 7): push 4  # m, n, 4
(59, 7): dup     # m, n, 4, 4
(60, 7): mult    # m, n, 16
(61, 7): dup     # m, n, 16, 16
(62, 7): add     # m, n, 32
(63, 7): outc    # m, n
```

`n = n - 1`:

```
(64, 7): push 1  # m, n, 1
(65, 7): sub     # m, n - 1
```

Check if `n` is greater than `0` and branch accordingly:

```
(66, 7): dup     # m, n, n
(67, 7): push 1  # m, n, n, 1
(68, 7): not     # m, n, n, 0
(69, 7): gt      # m, n, 1 if n > 0 else 0
(70, 7): DP+     # m, n
```

If `n` is greater than `0`, DP is rotated clockwise, so a bunch of no-ops
are executed, and the program goes back to the beginning of L. Otherwise,
DP is unchanged, and the program continues on to the beginning of M.

### Setup For Next Line (M)

Drop `n`:

```
(71, 7): pop     # m
```

`k = m`:

```
(71, 8): dup     # m, k
```

After that a bunch of no-ops are executed, and the program goes back to the
beginning of I.

#### Termination (N)

Drop `n`:

```
(40, 7): pop     # empty
```

After that the program will terminate since there is nowhere else to go. I
struggled with this, trying different shapes. Finally, the cross shape seemed
to do the trick.

## Credits

The image for this article is based on a painting by [Piet Mondrian][2] called
[Victory Boogie-Woogie][1]. He painted this in 1944 in expectation of victory
in World War II. I chose this painting because its shape matches the output
of the program. I copied it to the left and right just to fill in the empty
spaces, and I think it looks cool!

## Thanks

Thanks to `alope107` for introducing me to the Piet esoteric language and
for helping me fix a termination issue with this program (in other words,
I couldn't get the silly thing to stop running!).

[1]: https://www.piet-mondrian.org/victory-boogie-woogie.jsp
[2]: https://en.wikipedia.org/wiki/Piet_Mondrian
[3]: https://www.dangermouse.net/esoteric/piet.html
[4]: https://en.wikipedia.org/wiki/Esoteric_programming_language
[5]: https://en.wikipedia.org/wiki/HP_calculators
[6]: https://piet.bubbler.one/


## How to Run the Solution

Go to the [npiet interpreter site](https://www.bertnase.de/npiet/). On Linux,
download `.tar.gz` and extract the contents. Follow the instructions in the
`README` file. On Windows, download the `.zip` file and extract the contents.
Follow the instructions in the `README` file.

To run the code, use this:

```
npiet baklava.png
```

Alternatively, you can go to the
[Online Piet Editor and Interpreter site](https://piet.bubbler.one/),
import `baklava.png`, and execute it.
