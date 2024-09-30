---
authors:
- rzuckerm
date: 2024-02-05
featured-image: fraction-math-in-every-language.jpg
last-modified: 2024-02-05
layout: default
tags:
- beef
- fraction-math
title: Fraction Math in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/beef/how-to-implement-the-solution.md
- sources/programs/fraction-math/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;

namespace FractionMath;

struct Fraction : IParseable<Fraction>
{
    int32 mNum;
    int32 mDen;

    public this(int32 num, int32 den)
    {
        Runtime.Assert(den != 0);
        mNum = num;
        mDen = den;
        reduce();
    }

    public void reduce() mut
    {
        if (mDen < 0)
        {
            mNum = -mNum;
            mDen = -mDen;
        }

        int32 g = gcd(mNum, mDen);
        mNum /= g;
        mDen /= g;
    }

    public static int32 gcd(int32 num, int32 den)
    {
        Runtime.Assert(den != 0);
        int32 a = num >= 0 ? num : -num;
        int32 b = den >= 0 ? den : -den;
        while (b != 0)
        {
            (a, b) = (b, a % b);
        }

        return a;
    }

    public static Result<Fraction> Parse(StringView str)
    {
        int32[] arr = scope int32[2] (0, 1);
        int index = 0;
        for (StringView part in str.Split('/', 2))
        {
            StringView trimmedStr = scope String(part);
            trimmedStr.Trim();

            // T.Parse ignores single quotes since they are treat as digit separators -- e.g. 1'000
            if (trimmedStr.Contains('\''))
            {
                return .Err;
            }

            switch (Int32.Parse(trimmedStr))
            {
                case .Ok(out arr[index]):
                case .Err:
                    return .Err;
            }

            index++;
        }

        return .Ok(Fraction(arr[0], arr[1]));
    }

    public static Fraction operator +(Fraction lhs, Fraction rhs)
    {
        // n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2)
        return .(lhs.mNum * rhs.mDen + rhs.mNum * lhs.mDen, lhs.mDen * rhs.mDen);
    }

    public static Fraction operator -(Fraction lhs, Fraction rhs)
    {
        // n1/d1 - n2/d2 = (n1*d2 - n2*d1) / (d1*d2)
        return .(lhs.mNum * rhs.mDen - rhs.mNum * lhs.mDen, lhs.mDen * rhs.mDen);
    }

    public static Fraction operator *(Fraction lhs, Fraction rhs)
    {
        // n1/d1 * n2/d2 = (n1*n2) / (d1*d2)
        return .(lhs.mNum * rhs.mNum, lhs.mDen * rhs.mDen);
    }

    public static Fraction operator /(Fraction lhs, Fraction rhs)
    {
        // (n1/d1) / (n2/d2) = (n1*d2) / (d1*n2)
        return .(lhs.mNum * rhs.mDen, lhs.mDen * rhs.mNum);
    }

    public static int operator <=>(Fraction lhs, Fraction rhs)
    {
        // (n1/d1) <=> (n2/d2) = n1*d2 <=> d1*n2
        return (lhs.mNum * rhs.mDen) <=> (lhs.mDen * rhs.mNum);
    }

    public override void ToString(String str)
    {
        str.Clear();
        str.AppendF($"{mNum}/{mDen}");
    }
}

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: ./fraction-math operand1 operator operand2");
        Environment.Exit(0);
    }

    public enum FractionResult
    {
        case Frac(Fraction f);
        case Bool(bool b);

        public override void ToString(String str)
        {
            switch (this)
            {
                case .Frac(let f):
                    f.ToString(str);

                case .Bool(let b):
                    ((b) ? 1 : 0).ToString(str);
            }
        }
    }

    public static Result<FractionResult> FractionMath(Fraction f1, Fraction f2, String op)
    {
        switch (op)
        {
            case "+":  return .Ok(.Frac(f1 + f2));
            case "-":  return .Ok(.Frac(f1 - f2));
            case "*":  return .Ok(.Frac(f1 * f2));
            case "/":  return .Ok(.Frac(f1 / f2));
            case ">":  return .Ok(.Bool(f1 > f2));
            case ">=": return .Ok(.Bool(f1 >= f2));
            case "<":  return .Ok(.Bool(f1 < f2));
            case "<=": return .Ok(.Bool(f1 <= f2));
            case "==": return .Ok(.Bool(f1 == f2));
            case "!=": return .Ok(.Bool(f1 != f2));
            default:   return .Err;
        }
    }

    public static int Main(String[] args)
    {
        if (args.Count < 3)
        {
            Usage();
        }

        Fraction f1 = ?;
        switch (Fraction.Parse(args[0]))
        {
            case .Ok(out f1):
            case .Err:
                Usage();
        }

        String op = scope String(args[1]);

        Fraction f2 = ?;
        switch (Fraction.Parse(args[2]))
        {
            case .Ok(out f2):
            case .Err:
                Usage();
        }

        switch (FractionMath(f1, f2, op))
        {
            case .Ok(let res):
                Console.WriteLine(res);

            case .Err:
                Usage();
        }

        return 0;
    }
}

```

{% endraw %}

Fraction Math in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).