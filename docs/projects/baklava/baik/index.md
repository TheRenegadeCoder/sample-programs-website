---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- baik
- baklava
title: Baklava in Baik
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/baik/how-to-implement-the-solution.md
- sources/programs/baklava/baik/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Baik](https://sampleprograms.io/languages/baik) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```baik
# Since this language has Indonesian keywords, I figured it would be
# fun to use Indonesian variable and function names:
#
# - menangkal = counter
# - jumlah_spasi = number of spaces
# - jumlah_bintang = number of stars
# - senar = string
# - beberapa_kali = number of times
#
# References:
# - Google Translate
# - https://www.slideshare.net/slideshow/147-3411pb-baik/20917498

# Main function
# -------------------------------------------------
untuk (menangkal = 0; menangkal <= 20; menangkal++)
ulang
    # number of spaces = abs(counter - 10)
    jumlah_spasi = menangkal - 10
    jumlah_spasi = abs jumlah_spasi

    # number of stars = 21 - 2 * number of spaces
    jumlah_bintang = 21 - 2 * jumlah_spasi

    # Output number of spaces " "
    senar = " "
    &tulis_senar_ulangi(senar, jumlah_spasi)

    # Output number of stars "*"
    senar = "*"
    &tulis_senar_ulangi(senar, jumlah_bintang)

    # Output newline
    tulis "\n"
lagi

tamat
# -------------------------------------------------

# Output repeat string function
fungsi tulis_senar_ulangi(senar, beberapa_kali)
{
    untuk (menangkal = 1; menangkal <= beberapa_kali; menangkal++)
    ulang
        tulis senar
    lagi
}

```

{% endraw %}

Baklava in [Baik](https://sampleprograms.io/languages/baik) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).