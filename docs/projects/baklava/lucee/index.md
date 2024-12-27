---
authors:
- rzuckerm
date: 2024-12-27
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-27
layout: default
tags:
- baklava
- lucee
title: Baklava in Lucee
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/lucee/how-to-implement-the-solution.md
- sources/programs/baklava/lucee/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Lucee](https://sampleprograms.io/languages/lucee) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lucee
<html>
    <head>
        <title>Baklava</title>
    </head>
    <body>
        <pre><cfscript>
for (n = -10; n <= 10; n++) {
    numSpaces = abs(n);
    numStars = 21 - 2 * numSpaces;
    spaces = repeatString(" ", numSpaces);
    stars = repeatString("*", numStars);
    writeOutput(spaces & stars & "<br>");
}
        </cfscript></pre>
	</body>
</html>

```

{% endraw %}

Baklava in [Lucee](https://sampleprograms.io/languages/lucee) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).