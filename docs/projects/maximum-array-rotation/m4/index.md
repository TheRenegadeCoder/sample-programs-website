---
authors:
- rzuckerm
date: 2025-09-13
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-09-13
layout: default
tags:
- m4
- maximum-array-rotation
title: Maximum Array Rotation in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/m4/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please provide a list of integers (e.g. "8, 3, 1, 2")
m4exit(`1')')

dnl Reference: https://www.gnu.org/software/m4/manual/m4.html#index-array
dnl array_get(var_name, idx)
define(`array_get', `defn(format(``%s[%s]'', `$1', `$2'))')

dnl array_set(var_name, idx, value)
define(`array_set', `define(format(``%s[%s]'', `$1', `$2'), `$3')')

dnl is_valid(n)
define(`is_valid', `eval(regexp(`$1', `^\s*-?[0-9]+\s*$') >= 0)')

dnl parse_int_list(varname, args):
dnl   varname[length] = 0
dnl   foreach arg in args:
dnl     if not is_valid(arg):
dnl       Return 0
dnl     varname[varname[length]] = arg
dnl     varname[length] = varname[length] + 1
dnl   Return 1
define(`parse_int_list',
`array_set(`$1', `length', 0)dnl
_parse_int_list(`$1', $2)'dnl
)
define(`_parse_int_list',
`ifelse(is_valid(`$2'), 0, `0',
`array_set(`$1', array_get(`$1', `length'), `$2')dnl
array_set(`$1', `length', incr(array_get(`$1', `length')))dnl
ifelse(eval($# > 2), 1, `_parse_int_list(`$1', shift(shift($@)))', `1')'dnl
)'dnl
)

dnl M4 does not have infinity so choose smallest integer value as minus infinity
define(`MINUS_INF', -2147483648)

dnl max(a, b)
define(`max', `ifelse(eval($1 > $2), 1, `$1', `$2')')

dnl maximum_array_rotation(varname):
dnl   wmax = -infinity
dnl   for n = 0 to varname[length] - 1:
dnl     w = array_rotation_sum(varname, n, varname[length])
dnl     wmax = max(wmax, w)
dnl   return wmax
define(`maximum_array_rotation', `_maxmimum_array_rotation(`$1', 0, MINUS_INF)')
define(`_maxmimum_array_rotation',
`ifelse(
eval($2 >= array_get(`$1', `length')), 1, `$3',
`_maxmimum_array_rotation(`$1', incr($2),
    max($3, array_rotation_sum(`$1', $2, array_get(`$1', `length'))))'`'dnl
)'dnl
)

dnl array_rotation_sum(varname, offset, mod):
dnl   w = 0
dnl   for n = 0 to mod - 1:
dnl     w = w + n * varname[(n + offset) % mod]
dnl   return w
define(`array_rotation_sum', `_array_rotation_sum(`$1', $2, $3, 0, 0)')
define(`_array_rotation_sum',
`ifelse(
eval($4 >= $3), 1, `$5',
`_array_rotation_sum(`$1', $2, $3, incr($4),
    eval($5 + $4 * array_get(`$1', eval(($4 + $2) % $3))))'`'dnl
)'dnl
)
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1 || !parse_int_list(`arr', ARGV1)), 1, `show_usage()')dnl
maximum_array_rotation(`arr')

```

{% endraw %}

Maximum Array Rotation in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).