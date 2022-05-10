---

title: Even Odd in Php
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Even Odd in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```php
<?php

if ($argc < 2 || !is_numeric($argv[1])) {
    die("Usage: please input a number\n");
}

$input = abs($argv[1]);

if ($input % 2 == 0) {
    echo "Even\n";
} elseif ($input % 2 == 1) {
    echo "Odd\n";
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).