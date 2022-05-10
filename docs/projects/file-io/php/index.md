---

title: File Io in Php
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the File Io in Php page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```php
<?php

function write_file($file_name)
{
    $file = @fopen($file_name, "w");
    if ($file === false) {
        echo "Cannot open file \"", $file_name, "\" for writing.\n";
        return false;
    }

    fwrite($file, "Hello World.\n");
    fwrite($file, "Testing one...\n");
    fwrite($file, "two...\n");
    fwrite($file, "three!\n");

    fflush($file);
    fclose($file);
    return true;
}

function read_file($file_name)
{
    $file = @fopen($file_name, "r");
    if ($file === false) {
        echo "Cannot open file \"", $file_name, "\" for reading.\n";
        return;
    }

    while (!feof($file)) {
        echo fgets($file);
    }

    fclose($file);
}

$file_name = "output.txt";
if (write_file($file_name)) {
    read_file($file_name);
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).