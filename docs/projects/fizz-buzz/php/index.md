---
title: Fizz Buzz in Php
layout: default
date: 2018-09-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-09-09

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

for ($i = 1; $i < 101; $i++) {
    $output = "";

    if ($i % 3 == 0) {
        $output .= "Fizz";
    }

    if ($i % 5 == 0) {
        $output .= "Buzz";
    }

    if (!$output) {
        $output = $i;
    }

    echo $output . "\n";
}
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Sep 09 2018 22:41:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).