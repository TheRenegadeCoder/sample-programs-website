## High-Level Overview

This sample program implements Baklava using two main loops:

1.  Display the top 10 lines:

    - Display `n` spaces.
    - Display `21 - 2*n` asterisks.
    - Display a newline.

    where `n` equals 1, 2, ..., 10.

2.  Display the bottom 11 lines:

    - Display 21 asterisks.
    - Display a newline.

    then:

    - Display `10 - floor(m / 2)` spaces.
    - Display `m` asterisks.
    - Display a newline.

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

The `>` instruction pops the two top stack items. If the second stack item is
greater than the top stack item, 1 pushed; otherwise, 0 is pushed.

Greater than example:

- Stack (before): ..., 5, 4
- Stack (after): ..., 1

Not greater than example:

- Stack (before): ..., 3, 4
- Stack (after): ..., 0

The data pointer (DP), controls the flow of the program. The program starts
at `(0, 0)`, and DP points to the right. When DP hits an edge or black cell
it rotates clockwise. The program terminates when there is nowhere to go.

### Display `n` Spaces

![Space Loop 1](/assets/images/projects/baklava/piet/space-loop1.png)

#### First Space Loop Initialization

`n = 10`:

```
( 0,  0): push 2  # 2
( 2,  0): push 5  # 2, 5
( 4,  0): *       # 10 (n)
```

`k = n`:

```
( 5,  0): dup     # 10 (n), 10 (k)
```

#### First Space Loop

Output `" "`:

```
( 6,  0): push 4  # n, k, 4
(10,  0): dup     # n, k, 4, 4
(11,  0): *       # n, k, 16
(12,  0): dup     # n, k, 16, 16
(13,  0): +       # n, k, 32
(14,  0): outc    # n, k
```

`k = k - 1`:

```
(15,  0): push 1  # n, k, 1
(16,  0): -       # n, k - 1
```

If `(k - 1) > 0`, DP points down; otherwise, DP still points right.

```
(17,  0): dup     # n, k - 1, k - 1
(18,  0): push 1  # n, k - 1, k - 1, 1
(19,  0): !       # n, k - 1, k - 1, 0
(20,  0): >       # n, k - 1, (k - 1) > 0
(21,  0): DP+     # n, k - 1
```

For the case where `(k - 1) > 0`, a bunch of no-ops (the white cells) are
executed, and the program goes back to `(6, 0)`. Otherwise, the program
continues on to the next instruction at `(22, 0)`.

### Display `21 - 2 * n` Asterisks

![Asterisk Loop 1](/assets/images/projects/baklava/piet/asterisk-loop1.png)

#### First Asterisk Loop Initialization

Drop `k - 1`:

```
(22,  0): pop     # n
```

`m = 21 - 2 * n`:

```
(23,  0): dup     # n, n
(24,  0): push 1  # n, n, 1
(25,  0): !       # n, n, 0
(26,  0): push 1  # n, n, 0, 1
(27,  0): -       # n, n, -1
(28,  0): *       # n, -n
(29,  0): dup     # n, -n, -n
(30,  0): +       # n, -2 * n
(31,  0): push 3  # n, -2 * n, 3
(32,  1): push 7  # n, -2 * n, 3, 7
(34,  0): *       # n, -2 * n, 21
(35,  0): +       # n, 21 - 2 * n (m)
```

#### First Asterisk Loop

Output `"*"`:

```
(36,  0): push 3  # n, m, 3
(39,  0): dup     # n, m, 3, 3
(40,  0): +       # n, m, 6
(41,  0): dup     # n, m, 6, 6
(42,  0): dup     # n, m, 6, 6, 6
(43,  0): *       # n, m, 6, 36
(44,  0): +       # n, m, 42
(45,  0): outc    # n, m
```

`m = m - 1`:

```
(46,  0): push 1  # n, m, 1
(47,  0): -       # n, m - 1
```

If `(k - 1) > 0`, DP points down; otherwise, DP still points right.

```
(48,  0): dup     # n, m - 1, m - 1
(49,  0): push 1  # n, m - 1, m - 1 , 1
(50,  0): !       # n, m - 1, m - 1 , 0
(51,  0): >       # n, m - 1, (m - 1) > 0
(52,  0): DP+     # n, m - 1
```

For the case where `(m - 1) > 0`, a bunch of no-ops (the white cells) are
executed, and the program goes back to `(36, 0)`. Otherwise, the program
continues on to the next instruction at `(53, 0)`.

### First Display Newline

![Display Newline 1](/assets/images/projects/baklava/piet/newline1.png)

Drop `m - 1`:

```
(53,  0): pop     # n

Output `"\n"`:

```
(54,  0): push 2  # n, 2
(55,  1): push 5  # n, 2, 5
(53,  3): *       # n, 10
(52,  3): outc    # n
```

## Further Reading

If you'd like to learn more about the Piet language, see the [Official Site][3].

## Credits

The painting used in this image is called [Victory Boogie-Woogie][1],
painted by [Piet Mondrian][2] in 1944 in expectation of victory in World War
II.

## Thanks

Thanks to `alope107` for introducing me to the Piet esoteric language and
for helping me fix a termination issue in this program.

[1]: https://www.piet-mondrian.org/victory-boogie-woogie.jsp
[2]: https://en.wikipedia.org/wiki/Piet_Mondrian
[3]: https://www.dangermouse.net/esoteric/piet.html
