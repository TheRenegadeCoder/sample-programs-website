---
authors:
- Maximillian Naza
date: 2025-01-18
featured-image: fraction-math-in-every-language.jpg
last-modified: 2025-01-18
layout: default
tags:
- c
- fraction-math
title: Fraction Math in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/c/how-to-implement-the-solution.md
- sources/programs/fraction-math/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int numerator;
    int denominator;
} Fraction;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

Fraction simplify(Fraction f) {
    int g = gcd(abs(f.numerator), abs(f.denominator));
    f.numerator /= g;
    f.denominator /= g;
    if (f.denominator < 0) {
        f.numerator = -f.numerator;
        f.denominator = -f.denominator;
    }
    return f;
}

Fraction parse_fraction(const char* str) {
    Fraction f;
    sscanf(str, "%d/%d", &f.numerator, &f.denominator);
    return simplify(f);
}

Fraction add(Fraction a, Fraction b) {
    Fraction result = {
        a.numerator * b.denominator + b.numerator * a.denominator,
        a.denominator * b.denominator
    };
    return simplify(result);
}

Fraction subtract(Fraction a, Fraction b) {
    Fraction result = {
        a.numerator * b.denominator - b.numerator * a.denominator,
        a.denominator * b.denominator
    };
    return simplify(result);
}

Fraction multiply(Fraction a, Fraction b) {
    Fraction result = {
        a.numerator * b.numerator,
        a.denominator * b.denominator
    };
    return simplify(result);
}

Fraction divide(Fraction a, Fraction b) {
    Fraction result = {
        a.numerator * b.denominator,
        a.denominator * b.numerator
    };
    return simplify(result);
}

int compare(Fraction a, Fraction b) {
    int lhs = a.numerator * b.denominator;
    int rhs = b.numerator * a.denominator;
    if (lhs < rhs) return -1;
    if (lhs > rhs) return 1;
    return 0;
}

void print_fraction(Fraction f) {
    printf("%d/%d\n", f.numerator, f.denominator);
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        printf("Usage: ./fraction-math operand1 operator operand2\n");
        return 1;
    }

    Fraction a = parse_fraction(argv[1]);
    Fraction b = parse_fraction(argv[3]);
    char* op = argv[2];

    Fraction result;
    int cmp;

    if (strcmp(op, "+") == 0) {
        result = add(a, b);
        print_fraction(result);
    } else if (strcmp(op, "-") == 0) {
        result = subtract(a, b);
        print_fraction(result);
    } else if (strcmp(op, "*") == 0) {
        result = multiply(a, b);
        print_fraction(result);
    } else if (strcmp(op, "/") == 0) {
        result = divide(a, b);
        print_fraction(result);
    } else if (strcmp(op, "==") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp == 0);
    } else if (strcmp(op, ">") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp > 0);
    } else if (strcmp(op, "<") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp < 0);
    } else if (strcmp(op, ">=") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp >= 0);
    } else if (strcmp(op, "<=") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp <= 0);
    } else if (strcmp(op, "!=") == 0) {
        cmp = compare(a, b);
        printf("%d\n", cmp != 0);
    } else {
        printf("Invalid operator\n");
        return 1;
    }

    return 0;
}

```

{% endraw %}

Fraction Math in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).