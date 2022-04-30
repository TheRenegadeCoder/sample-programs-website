---

title: Rot 13 in Php
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Rot 13 in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Php
<?php

if (empty($argv[1]) || $argv[1] == "" || count($argv) == 0) {
    die("Usage: please provide a string to encrypt\n");
}

function rot13(string $string) {
    return strtr($string,
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm');
}

echo rot13($argv[1]) . "\n";
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).