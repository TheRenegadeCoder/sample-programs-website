---

title: Prime Number in Java
layout: default
date: 2022-04-28
last-modified: 2022-09-25

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
/** Prime number exception to handle errors. */
class PrimeNumberException extends Exception {}

/**
 * Prime number program.
 */
public class PrimeNumber {

    /**
     * Determine if an integer is a prime number.
     * @param number Non negative integer to check.
     * @return true if the number is prime, false otherwise.
     */
    public static boolean isPrime(int number) {
        if ((number % 2 == 0 && number != 2) || number == 1) {
            return false;
        }

        boolean foundFactor = false;
        for (int n = 3; n <= (int) Math.ceil(Math.sqrt(number)); ++n) {
            if ((number % n) == 0) {
                foundFactor = true;
                break;
            }
        }
        return !foundFactor;
    }

    /**
     * Main.
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        try {

            // Check argument
            if (args.length < 1 || args[0].indexOf('-') != -1) {
                throw new PrimeNumberException();
            }

            // Convert to int and check
            if (isPrime(Integer.valueOf(args[0]))) {
                System.out.println("Prime");

            } else {
                System.out.println("Composite");
            }

        } catch (NumberFormatException | PrimeNumberException e) {
            System.err.println("Usage: please input a non-negative integer");
        }
    }
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Java](https://sampleprograms.io/languages/java) was written by:

- Ewerton Queiroz
- Ganesh Naik
- Juan D Frias

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2020 14:54:28. The solution was first committed on Oct 10 2019 02:15:05. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).