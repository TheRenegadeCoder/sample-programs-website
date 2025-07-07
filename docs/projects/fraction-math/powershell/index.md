---
authors:
- rzuckerm
date: 2025-07-07
featured-image: fraction-math-in-every-language.jpg
last-modified: 2025-07-07
layout: default
tags:
- fraction-math
- powershell
title: Fraction Math in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/powershell/how-to-implement-the-solution.md
- sources/programs/fraction-math/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: ./fraction-math operand1 operator operand2"
    Exit 1
}

class Fraction : IComparable {
    [int]$Num
    [int]$Den

    Fraction([int]$n, [int]$d) {
        if ($d -lt 0) {
            $n = -$n
            $d = -$d
        }

        $g = [Fraction]::Gcd($n, $d)
        $this.Num = [Math]::Floor($n / $g)
        $this.Den = [Math]::Floor($d / $g)
    }

    static [int] Gcd([int]$a, [int]$b) {
        if (-not $a) {
            return $b
        }

        while ($b) {
            $a, $b = $b, ($a % $b)
        }

        return $a
    }

    static [Fraction] Parse([string]$str) {
        $parts = $str.Split('/')
        $d = 1
        $n = [int]::Parse($parts[0])
        if ($parts.Length -eq 2) {
            $d = [int]::Parse($parts[1])
        } elseif ($parts.Length -gt 2) {
            throw "Invalid format"
        }

        return [Fraction]::new($n, $d)
    }

    [string] ToString() {
        return "$($this.Num)/$($this.Den)"
    }

    [bool] Equals([object]$other) {
        return $this.Num -eq $other.Num -and $this.Den -eq $other.Den
    }

    # n1/d1 OP n2/d2 = n1*d2 OP n2*d1
    [int] CompareTo([object]$other) {
        return $this.Num * $other.Den - $other.Num * $this.Den
    }

    # n1/d1 +/- n2/d2 = (n1*d2 +/- n2*d1) / (d1*d2)
    static [Fraction] op_Addition([Fraction]$lhs, [Fraction]$rhs) {
        return [Fraction]::new($lhs.Num * $rhs.Den + $rhs.Num * $lhs.Den, $lhs.Den * $rhs.Den)
    }

    static [Fraction] op_Subtraction([Fraction]$lhs, [Fraction]$rhs) {
        return [Fraction]::new($lhs.Num * $rhs.Den - $rhs.Num * $lhs.Den, $lhs.Den * $rhs.Den)
    }

    # n1/d1 * n2/d2 = (n1*n2) / (d1*d2)
    static [Fraction] op_Multiply([Fraction]$lhs, [Fraction]$rhs) {
        return [Fraction]::new($lhs.Num * $rhs.Num, $lhs.Den * $rhs.Den)
    }

    # (n1/d1) / (n2/d2) = (n1*d2) / (n2*d1)
    static [Fraction] op_Division([Fraction]$lhs, [Fraction]$rhs) {
        return [Fraction]::new($lhs.Num * $rhs.Den, $rhs.Num * $lhs.Den)
    }
}

function Invoke-FractionMath([Fraction]$frac1, [string]$op, [Fraction]$frac2) {
    switch ($op) {
        "+" { return $frac1 + $frac2 }
        "-" { return $frac1 - $frac2 }
        "*" { return $frac1 * $frac2 }
        "/" { return $frac1 / $frac2 }
        "==" { return $frac1 -eq $frac2 }
        "!=" { return $frac1 -ne $frac2 }
        ">" { return $frac1 -gt $frac2 }
        ">=" { return $frac1 -ge $frac2 }
        "<" { return $frac1 -lt $frac2 }
        "<=" { return $frac1 -le $frac2 }
        default { throw "Invalid operation" }
    }
}

if ($args.Length -lt 3) {
    Show-Usage
}

try {
    $frac1 = [Fraction]::Parse($args[0])
    $frac2 = [Fraction]::Parse($args[2])
} catch {
    Show-Usage
}

$op = $args[1]
$result = Invoke-FractionMath $frac1 $op $frac2
if ($result -is [bool]) {
    Write-Output ([int]$result)
} else {
    Write-Output "$result"
}

```

{% endraw %}

Fraction Math in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).