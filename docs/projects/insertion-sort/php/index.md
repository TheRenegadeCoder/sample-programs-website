---
title: Insertion Sort in Php
layout: default
date: 2019-10-13
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-10-13

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

function insertion_Sort($my_array)
{
    for ($i = 0; $i < count($my_array); $i++) {
        $val = $my_array[$i];
        $j = $i - 1;
        while ($j >= 0 && $my_array[$j] > $val) {
            $my_array[$j + 1] = $my_array[$j];
            $j--;
        }
        $my_array[$j + 1] = $val;
    }
    return $my_array;
}

if (empty($argv[1])) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$test_array = array_map('intval', explode(',', $argv[1]));
$array_size = count($test_array);

if ($array_size <= 1) {
    exit('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

$out = insertion_Sort($test_array);
echo implode(', ', $out);
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Parker Johansen
- sljtheultima

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Oct 13 2019 16:44:31. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).