---

title: Reverse String in Apex
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Reverse String in Apex page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Apex
String original= 'abcdef';
String revStr = ' ';

for (Integer i = original.length()-1; i >= 0; i--)
{
	revStr += original.substring(i, i+1);
}

system.debug(revStr );
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).