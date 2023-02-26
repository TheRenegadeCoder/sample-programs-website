---

title: Reverse String in Apex
layout: default
date: 2022-04-28
last-modified: 2023-02-26

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Apex](https://sampleprograms.io/languages/apex) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```apex
String original= 'abcdef';
String revStr = ' ';

for (Integer i = original.length()-1; i >= 0; i--)
{
	revStr += original.substring(i, i+1);
}

system.debug(revStr );
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Apex](https://sampleprograms.io/languages/apex) was written by:

- coderdecoder01

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).