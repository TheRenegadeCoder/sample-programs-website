---
title: Job Sequencing in Php
layout: default
date: 2019-10-28
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2019-10-28

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php

if ($argc < 3 || empty($argv[1]) || empty($argv[2])) {
    return_error();
}

$profits = parse_int_array($argv[1]);
$deadlines = parse_int_array($argv[2]);

$profits_count = count($profits);
$deadlines_count = count($deadlines);

if ($profits_count < 1 || $profits_count != $deadlines_count) {
    return_error();
}

$max_deadline = max($deadlines);

$jobsToDo = array_fill(0, $profits_count, 0);

for ($i = 0; $i < $profits_count; $i++) {
    $job_index = $deadlines[$i] - 1;
    while ($job_index >= 0 && $job_index < $profits_count) {
        if ($jobsToDo[$job_index] == 0) {
            $jobsToDo[$job_index] = $profits[$i];
            break;
        }
        $job_index--;
    }
}

echo array_sum($jobsToDo);

function parse_int_array($arg)
{
    return array_map('intval', explode(',', trim($arg, ',')));
}

function return_error()
{
    echo "Usage: please provide a list of profits and a list of deadlines\n";
    exit();
}
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Php](https://sampleprograms.io/languages/php) was written by:

- Jeremy Grifski
- Kateryna Tokar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 09 2022 21:44:19. The solution was first committed on Oct 28 2019 19:28:30. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).