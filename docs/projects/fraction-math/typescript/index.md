---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- fraction-math
- typescript
title: Fraction Math in TypeScript
title1: Fraction Math
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/typescript/how-to-implement-the-solution.md
- sources/programs/fraction-math/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
"use strict";

const USAGE = "Usage: ./fraction-math operand1 operator operand2";

class Fraction {
  private n: number;
  private d: number;

  constructor(numerator: number, denominator: number) {
    if (denominator === 0) {
      throw new Error("Division by zero");
    }

    const sign = denominator < 0 ? -1 : 1;
    const common = Fraction.gcd(numerator, denominator);

    this.n = (numerator / common) * sign;
    this.d = (denominator / common) * sign;
  }

  static gcd(a: number, b: number): number {
    let x = Math.abs(a);
    let y = Math.abs(b);

    while (y !== 0) {
      const tmp = x % y;
      x = y;
      y = tmp;
    }

    return x;
  }

  static parse(str: string): Fraction {
    const parts = str.split("/");

    const n = parseInt(parts[0], 10);
    const d = parts[1] !== undefined ? parseInt(parts[1], 10) : 1;

    if (isNaN(n) || isNaN(d)) {
      throw new Error("Invalid fraction format");
    }

    return new Fraction(n, d);
  }

  add(o: Fraction): Fraction {
    return new Fraction(this.n * o.d + o.n * this.d, this.d * o.d);
  }

  sub(o: Fraction): Fraction {
    return new Fraction(this.n * o.d - o.n * this.d, this.d * o.d);
  }

  mul(o: Fraction): Fraction {
    return new Fraction(this.n * o.n, this.d * o.d);
  }

  div(o: Fraction): Fraction {
    return new Fraction(this.n * o.d, this.d * o.n);
  }

  compare(o: Fraction): number {
    const diff = this.n * o.d - o.n * this.d;

    if (diff === 0) return 0;
    return diff > 0 ? 1 : -1;
  }

  toString(): string {
    return `${this.n}/${this.d}`;
  }
}

const operators: {
  [key: string]: (a: Fraction, b: Fraction) => Fraction | number;
} = {
  "+": (a, b) => a.add(b),
  "-": (a, b) => a.sub(b),
  "*": (a, b) => a.mul(b),
  "/": (a, b) => a.div(b),

  "==": (a, b) => (a.compare(b) === 0 ? 1 : 0),
  "!=": (a, b) => (a.compare(b) !== 0 ? 1 : 0),
  ">": (a, b) => (a.compare(b) > 0 ? 1 : 0),
  "<": (a, b) => (a.compare(b) < 0 ? 1 : 0),
  ">=": (a, b) => (a.compare(b) >= 0 ? 1 : 0),
  "<=": (a, b) => (a.compare(b) <= 0 ? 1 : 0),
};

function run(): void {
  const [, , rawA, op, rawB] = process.argv;

  if (!rawA || !rawB || !op || !(op in operators)) {
    console.error(USAGE);
    process.exit(1);
  }

  try {
    const f1 = Fraction.parse(rawA);
    const f2 = Fraction.parse(rawB);

    const result = operators[op](f1, f2);

    console.log(result.toString());
  } catch {
    console.error(USAGE);
    process.exit(1);
  }
}

run();

```

{% endraw %}

Fraction Math in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).