---

title: Longest Word in Java
layout: default
date: 2022-04-28
last-modified: 2022-10-10

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;
class LongestWord {
    public static void error(){
        System.out.println("Usage: please provide a string");
    }
    public static void main(String[] args) {
        if(args.length <=0){
            error();
        }else if(args[0].length()==0){
            error();
        }else{
            String inputStr = args[0];
            String [] words = inputStr.split("\\s+");
            int max = -1;
            for(String word:words){
                if(word.length()>max){
                    max = word.length();
                }
            }
            System.out.println(max);
        }
  }
}
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Java](https://sampleprograms.io/languages/java) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).