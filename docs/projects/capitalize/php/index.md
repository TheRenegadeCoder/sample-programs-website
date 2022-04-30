---

title: Capitalize in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Capitalize in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).