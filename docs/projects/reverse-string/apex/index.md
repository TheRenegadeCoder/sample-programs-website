---

title: Reverse String in Apex

---

Welcome to the Reverse String in Apex page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.