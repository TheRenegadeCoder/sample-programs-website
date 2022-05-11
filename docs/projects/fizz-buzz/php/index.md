---

title: Fizz Buzz in Php
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Fizz Buzz in Php was written by:

- Jeremy Grifski

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Sep 09 2018 22:41:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).