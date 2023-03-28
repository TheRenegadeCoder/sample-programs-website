---

title: Longest Word in Php
layout: default
date: 2022-04-28
last-modified: 2023-03-26

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please provide a string");
}

function longest_word_length($str)
{
    // Split on whitespace, get string length of each word, take the maximum
    return max(array_map("strlen", preg_split("/\s+/", $str)));
}

// Exit if too few arguments
if (count($argv) < 2)
{
    usage();
}

// Exit if 1st command-line argument is empty
$str = $argv[1];
if (empty($str))
{
    usage();
}

// Get longest word length and display
$longest_len = longest_word_length($str);
echo "${longest_len}\n";
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).