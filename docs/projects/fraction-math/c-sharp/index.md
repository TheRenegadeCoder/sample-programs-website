---
authors:
- Alexander Ruban
- Ștefan-Iulian Alecu
date: 2024-11-13
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- fraction-math
title: Fraction Math in C#
title1: Fraction
title2: Math in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/c-sharp/how-to-implement-the-solution.md
- sources/programs/fraction-math/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (
    args is not [var leftRaw, var op, var rightRaw]
    || !Fraction.TryParse(leftRaw, out var a)
    || !Fraction.TryParse(rightRaw, out var b)
)
{
    Console.Error.WriteLine("Usage: ./fraction-math operand1 operator operand2");
    return;
}

Console.WriteLine(
    op switch
    {
        "+" => (a + b).ToString(),
        "-" => (a - b).ToString(),
        "*" => (a * b).ToString(),
        "/" => (a / b).ToString(),
        "==" => (a == b ? 1 : 0),
        "!=" => (a != b ? 1 : 0),
        ">" => (a > b ? 1 : 0),
        "<" => (a < b ? 1 : 0),
        ">=" => (a >= b ? 1 : 0),
        "<=" => (a <= b ? 1 : 0),
        _ => "Error: Invalid operator",
    }
);

public readonly record struct Fraction(long N, long D) : IComparable<Fraction>
{
    public override string ToString() => $"{N}/{D}";

    public static Fraction Create(long n, long d)
    {
        if (d == 0)
            throw new DivideByZeroException();

        long g = Gcd(n, d);
        return new(n / g * Math.Sign(d), Math.Abs(d / g));
    }

    static long Gcd(long a, long b)
    {
        a = Math.Abs(a);
        b = Math.Abs(b);

        while (b != 0)
            (a, b) = (b, a % b);

        return a == 0 ? 1 : a;
    }

    public static bool TryParse(ReadOnlySpan<char> s, out Fraction f)
    {
        f = default;

        int i = s.IndexOf('/');
        return i >= 0
            && long.TryParse(s[..i], out long n)
            && long.TryParse(s[(i + 1)..], out long d)
            && d != 0
            && (f = Create(n, d)) == f;
    }

    public static Fraction operator +(Fraction a, Fraction b) =>
        Create(a.N * b.D + b.N * a.D, a.D * b.D);

    public static Fraction operator -(Fraction a, Fraction b) =>
        Create(a.N * b.D - b.N * a.D, a.D * b.D);

    public static Fraction operator *(Fraction a, Fraction b) => Create(a.N * b.N, a.D * b.D);

    public static Fraction operator /(Fraction a, Fraction b) => Create(a.N * b.D, a.D * b.N);

    public static bool operator <(Fraction a, Fraction b) => a.N * b.D < b.N * a.D;

    public static bool operator >=(Fraction a, Fraction b) => !(a < b);

    public static bool operator >(Fraction a, Fraction b) => b < a;

    public static bool operator <=(Fraction a, Fraction b) => !(b < a);

    public int CompareTo(Fraction other) => (N * other.D).CompareTo(other.N * D);
}

```

{% endraw %}

Fraction Math in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Alexander Ruban
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).