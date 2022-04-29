---

title: Fibonacci in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fibonacci in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Php
<?php

if ($argc < 2 || !is_numeric($argv[1]) || intval($argv[1]) < 0) {
    die("Usage: please input the count of fibonacci numbers to output");
}

$input = intval($argv[1]);

$a = 0;
$b = 1;
$fibonacci = 0;

for ($index = 1; $index <= $input; $index++) {
    $fibonacci = $a + $b;
    $a = $b;
    $b = $fibonacci;
    echo "$index: $a\n";
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.