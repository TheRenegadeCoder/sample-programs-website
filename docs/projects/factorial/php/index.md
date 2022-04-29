---

title: Factorial in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Factorial in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Php
<?php
/**
 * by: Italo Sousa
 * its assumed that the file is running through command line
 * inputs are read from the same.
 * 
 * Max factorial supported is 170
 * 
 */

// Validation
$input = NULL;
if (
    sizeof($argv) < 2 ||
    !is_numeric($argv[1]) ||
    intval($argv[1]) < 0
) {
    echo("Usage: please input a non-negative integer\n");
    exit(0);
}

$factorial = 1;
$input = intval($argv[1]);

for ($x = $input; $x >= 1; $x--) {
    $factorial = $factorial * $x;
}

echo("$factorial\n");

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.