---
title: Roman Numeral in Php
layout: default
date: 2019-10-14
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2019-10-14

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

/**
 * Roman numeral string to Decimal value.
 * @param string $romans String to convert.
 * @return int The decimal value.
 * @throws Exception on invalid roman string.
 */
function roman_to_decimal($romans)
{
    // conversion table
    $roman_values = array("I" => 1, "V" => 5, "X" => 10,
        "L" => 50, "C" => 100, "D" => 500, "M" => 1000);

    $total = 0;
    $previous = 0;

    // parse from end to start of string
    for ($i = strlen($romans) - 1; $i >= 0; --$i) {

        // check if the character is a roman numeral
        $numeral = strtoupper($romans[$i]);
        if (!array_key_exists($numeral, $roman_values)) {
            throw new Exception("invalid string of roman numerals");
        }

        // convert to decimal and add/subtract from total.
        $value = $roman_values[$numeral];
        if ($value >= $previous) {
            $total += $value;

        } else {
            $total -= $value;
        }

        // keep track of last value
        $previous = $value;
    }

    return $total;
}

try {

    // Check argument count
    if ($argc < 2) {
        echo "Usage: please provide a string of roman numerals\n";
        exit(1);
    }

    // Convert the string
    echo roman_to_decimal($argv[1]), "\n";
    exit(0);

} catch (Exception $e) {
    echo "Error: ", $e->getMessage(), "\n";
    exit(1);
}
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Juan D Frias
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Oct 14 2019 11:54:09. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).