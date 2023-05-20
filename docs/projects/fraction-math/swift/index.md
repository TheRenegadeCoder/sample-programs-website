---
title: Fraction Math in Swift
layout: default
date: 2020-10-01
featured-image: fraction-math-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
// for System.exit()
import Foundation


/*
    Implementation of the Euclid's Algorithm.
    Used to simplify the fractions during initialization
*/
func gcd(_ a: Int, _ b:Int) -> Int {
    var a = a >= 0 ? a : -a
    var b = b
    var tmp = 0
    while b != 0 {
        tmp = b
        b = a % b
        a = tmp
    }
    return a
}

/*
    Used for Type conversion Bool => Int
*/
extension Bool {
    var intValue: Int {
        return self ? 1 : 0
    }    
}

struct IntFraction {
    var numerator, denominator: Int

    init(_ num:Int, _ denom:Int) {
        guard denom != 0 else {
            print("Error: Denominator cannot be 0")
            exit(0)
        }

        var num = num
        if denom < 0 {
            num = -num
        }
        let gcd_ = gcd(num, denom) 
        numerator = num / gcd_
        denominator = denom / gcd_
    }

    init?(fromString str:String) {
        let parts = str.components(separatedBy: "/")
        guard parts.count == 2, let num = Int(parts[0]), let denom = Int(parts[1]) else {
            return nil
        }

        self.init(num, denom)
    }


    static func +(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator + rhs.numerator*lhs.denominator
        let bottom = lhs.denominator*rhs.denominator
        return IntFraction(top, bottom)
    }

    static func -(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator - rhs.numerator*lhs.denominator
        let bottom = lhs.denominator*rhs.denominator
        return IntFraction(top, bottom)
    }

    static func *(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        return IntFraction(lhs.numerator*rhs.numerator, lhs.denominator*rhs.denominator)
    }

    static func /(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator
        let bottom = lhs.denominator*rhs.numerator
        return IntFraction(top, bottom);
    }

    static func ==(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res == 0
    }

    static func >(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res > 0
    }

    static func <(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res < 0
    }

    static func >=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs < rhs)
    }

    static func <=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs > rhs)
    }

    static func !=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs == rhs)
    }
}


/*
    Check validity of command line arguments
*/
guard CommandLine.argc == 4 else {
    print("Usage: \(CommandLine.arguments[0]) operand1 operator operand2")
    exit(0)
}
guard let operand1 = IntFraction(fromString: CommandLine.arguments[1]), let operand2 = IntFraction(fromString: CommandLine.arguments[3]) else {
    print("Invalid operand. Usage: a/b => 3/4")
    exit(0)
}

let op = CommandLine.arguments[2]
switch op {
case "+":
    let res = operand1 + operand2
    print("\(res.numerator)/\(res.denominator)")
case "-":
    let res = operand1 - operand2
    print("\(res.numerator)/\(res.denominator)")
case "*":
    let res = operand1 * operand2
    print("\(res.numerator)/\(res.denominator)")
case "/":
    let res = operand1 / operand2
    print("\(res.numerator)/\(res.denominator)")
case "==":
    let res = operand1 == operand2
    print("\(res.intValue)")
case ">":
    let res = operand1 > operand2
    print("\(res.intValue)")
case "<":
    let res = operand1 < operand2
    print("\(res.intValue)")
case ">=":
    let res = operand1 >= operand2
    print("\(res.intValue)")
case "<=":
    let res = operand1 <= operand2
    print("\(res.intValue)")
case "!=":
    let res = operand1 != operand2
    print("\(res.intValue)")
default:
    print("No matching operation for symbol: '\(op)'")
    exit(0)
}
```

{% endraw %}

[Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Zapnuk

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2020 17:31:54. The solution was first committed on Oct 01 2020 17:07:28. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).