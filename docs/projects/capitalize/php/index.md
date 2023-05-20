---
title: Capitalize in Php
layout: default
date: 2019-10-12
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-12

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if (count($argv) == 2 && strlen($argv[1])) {
    $inputString = $argv[1];
    $capitalized = ucfirst($inputString);
    echo $capitalized;
} else {
    echo "Usage: please provide a string";
}
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Php](https://sampleprograms.io/languages/php) was written by:

- Dowayne Breedt
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 22:45:19. The solution was first committed on Oct 12 2019 20:02:21. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).