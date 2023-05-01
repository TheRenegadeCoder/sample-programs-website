## Introduction

Piet is an [esoteric programming language][4]. Esoteric programming languages
make it difficult to implement even the simplest task, and this was my first
foray into such languages. If that wasn't difficult enough, Piet is a
graphical language, so you can't just pop into a text editor to create a
program. Instead, you have to use an [online editor][6] to even create a
program. To make things even more interesting, Piet uses a rotating color
palette, where the color of the next instruction depends upon the previous
color. Finally, it is a stack-based language, so programming in it is akin to
programming an old [Hewlett-Packard calculator][5]. If you'd like to learn
more about the Piet language, see the [Official Site][3].

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

## Detailed Description

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

### Output Top 10 Lines (A thru G)

#### Space Loop Initialization (A)

`n = 10`:

```
( 0,  0): push 2  # 2
( 2,  0): push 5  # 2, 5
( 4,  0): mult    # 10 (n)
```

`k = n`:

```
( 5,  0): dup     # 10 (n), 10 (k)
```

#### Space Loop (B)

Output `" "`:

```
( 6,  0): push 4  # n, k, 4
(10,  0): dup     # n, k, 4, 4
(11,  0): mult    # n, k, 16
(12,  0): dup     # n, k, 16, 16
(13,  0): add     # n, k, 32
(14,  0): outc    # n, k
```

`k = k - 1`:

```
(15,  0): push 1  # n, k, 1
(16,  0): sub     # n, k - 1
```

Check whether the `k` is greater than `0` and branch accordingly:

```
(17,  0): dup     # n, k, k
(18,  0): push 1  # n, k, k, 1
(19,  0): not     # n, k, k, 0
(20,  0): gt      # n, k, 1 if k > 0 else 0
(21,  0): DP+     # n, k
```

If `k` is greater than 0, DP rotates clockwise, so a bunch of no-ops are
executed, and the program goes back to the beginning of B. Otherwise, DP is
unchanged, so the program continues on to the beginning of C.

#### Asterisk Loop Initialization (C)

Drop `k`:

```
(22,  0): pop     # n
```

`m = 21 - 2 * n`:

```
(23,  0): dup     # n, n
(24,  0): push 1  # n, n, 1
(25,  0): not     # n, n, 0
(26,  0): push 1  # n, n, 0, 1
(27,  0): sub     # n, n, -1
(28,  0): mult    # n, -n
(29,  0): dup     # n, -n, -n
(30,  0): add     # n, -2 * n
(31,  0): push 3  # n, -2 * n, 3
(32,  1): push 7  # n, -2 * n, 3, 7
(34,  0): mult    # n, -2 * n, 21
(35,  0): add     # n, 21 - 2 * n (m)
```

#### Asterisk Loop (D)

Output `"*"`:

```
(36,  0): push 3  # n, m, 3
(39,  0): dup     # n, m, 3, 3
(40,  0): add     # n, m, 6
(41,  0): dup     # n, m, 6, 6
(42,  0): dup     # n, m, 6, 6, 6
(43,  0): mult    # n, m, 6, 36
(44,  0): add     # n, m, 42
(45,  0): outc    # n, m
```

`m = m - 1`:

```
(46,  0): push 1  # n, m, 1
(47,  0): sub     # n, m - 1
```

Check whether `m` is greater than `0` and branch accordingly:

```
(48,  0): dup     # n, m, m
(49,  0): push 1  # n, m, m , 1
(50,  0): not     # n, m, m , 0
(51,  0): gt      # n, m, 1 if m > 0 else 0
(52,  0): DP+     # n, m
```

If `m` is greater than `0`, DP rotates clockwise, so a bunch of no-ops are
executed, and the program goes back to the beginning of C. Otherwise, DP is
unchanged, so the program continues on to the beginning of D.

#### Output Newline (E)

Drop `m`:

```
(53,  0): pop     # n
```

Output `"\n"`:

```
(54,  0): push 2  # n, 2
(55,  1): push 5  # n, 2, 5
(53,  3): mult    # n, 10
(52,  3): outc    # n
```

#### Check If Last Line (F)

`n = n - 1`:

```
(51,  3): push 1  # n, 1
(50,  3): sub     # n - 1
```

Check if `n` is greater than `0` and branch accordingly:

```
(49,  3): dup     # n, n
(48,  3): push 1  # n, n, 1
(47,  3): not     # n, n, 0
(46,  3): gt      # n, 1 if n > 0 else 0 (q)
(45,  3): not     # n, 1 - q
(44,  3): dup     # n, 1 - q, 1 - q
(43,  3): dup     # n, 1 - q, 1 - q, 1 - q
(42,  3): add     # n, 1 - q, 2 * (1 - q)
(41,  3): add     # n, 3 * (1 - q)
(40,  3): DP+     # n
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
(39, 3): dup     # n, k
```

The program then executes a bunch of no-ops and goes back to the beginning of B.

### Output Bottom 11 Lines (H thru M)

#### Asterisk Loop Initialization (H)

## Credits

The image for this article is based on a painting by [Piet Mondrian][2] called
[Victory Boogie-Woogie][1]. He painted this in 1944 in expectation of victory
in World War II.

## Thanks

Thanks to `alope107` for introducing me to the Piet esoteric language and
for helping me fix a termination issue with this program (in other words,
I couldn't get the thing to stop running!).

[1]: https://www.piet-mondrian.org/victory-boogie-woogie.jsp
[2]: https://en.wikipedia.org/wiki/Piet_Mondrian
[3]: https://www.dangermouse.net/esoteric/piet.html
[4]: https://en.wikipedia.org/wiki/Esoteric_programming_language
[5]: https://en.wikipedia.org/wiki/HP_calculators
[6]: https://piet.bubbler.one/
