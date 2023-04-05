---

title: Longest Palindromic Substring in Php
layout: default
date: 2022-04-28
last-modified: 2023-04-04

---

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
// Find longest palindromic string using matching array
// Source: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
function longest_palindromic_substring($str)
{
    // Initialize array indicating whether there is a character match
    // between two characters to indicate that nothing matches
    $n = strlen($str);
    $matches = array_fill(0, $n, array_fill(0, $n, FALSE));

    // Indicate all length 1 strings match
    for ($i = 0; $i < $n; $i++)
    {
        $matches[$i][$i] = TRUE;
    }

    // Convert string to lowercase
    $temp_str = strtolower($str);

    // Find all length 2 matches
    $start = 0;
    $max_len = 1;
    for ($i = 0; $i < $n - 1; $i++)
    {
        if ($temp_str[$i] == $temp_str[$i + 1])
        {
            $matches[$i][$i + 1] = TRUE;
            if ($max_len < 2)
            {
                $start = $i;
                $max_len = 2;
            }
        }
    }

    // Find all length 3 or higher matches
    for ($len = 3; $len <= $n; $len++)
    {
        // Loop through each starting character
        for ($i = 0; $i < $n - $len + 1; $i++)
        {
            // If match for one character in from start and end characters
            // and start and end characters match, set match for start and
            // end characters, and update max length
            $j = $i + $len - 1;
            if ($matches[$i + 1][$j - 1] && $temp_str[$i] == $temp_str[$j])
            {
                $matches[$i][$j] = TRUE;
                if ($len > $max_len)
                {
                    $start = $i;
                    $max_len = $len;
                }
            }
        }
    }

    return substr($str, $start, $max_len);
}

function usage()
{
    exit("Usage: please provide a string that contains at least one palindrome");
}

// Exit if 1st command-line argument is missing is empty
if (count($argv) < 2 || empty($argv[1]))
{
    usage();
}

// Get longest palindromic substring. Exit if none found
$str = $argv[1];
$longest = longest_palindromic_substring($str);
if (strlen($longest) < 2)
{
    usage();
}

// Show longest palindromic substring
echo "${longest}\n";
```

{% endraw %}

[Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).