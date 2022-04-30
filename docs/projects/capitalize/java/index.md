---

title: Capitalize in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Capitalize in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Java
public class Capitalize
{

    public static boolean isLetter(char someChar)
    {
        return (someChar >= 'a' && someChar <= 'z') || (someChar >= 'A' && someChar <= 'Z');
    }

    public static boolean isUpperCase(char someChar)
    {
        return (someChar >= 'A' && someChar <= 'Z');
    }

    public static void main(String[] args)
    {
        if (args.length == 0 || args[0].equals(""))
        {
            System.out.println("Usage: please provide a string");
            System.exit(1);
        }
        String sentence = args[0];

        char firstChar = sentence.charAt(0);
        if (isLetter(firstChar) && !isUpperCase(firstChar))
        {
            char[] charArray = sentence.toCharArray();
            charArray[0] = Character.toUpperCase(firstChar);
            sentence = new String(charArray);
        }
        System.out.println(sentence);

    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).