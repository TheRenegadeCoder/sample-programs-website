---

---

Welcome to the Rot 13 in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.