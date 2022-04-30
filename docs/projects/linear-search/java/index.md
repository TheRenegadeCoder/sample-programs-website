---

title: Linear Search in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Linear Search in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```java
import java.util.*;

public class LinearSearch {

    public static void main(String[] args) {
        try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            Integer keyToSearch = Integer.parseInt(args[1]);
            String[] NumberArray = args[0].split(",");
            for(String Number: NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            if(listOfNumbers.size() >= 1){
                StringBuilder output = new StringBuilder();
                Boolean searched = linearSearch(listOfNumbers, keyToSearch);
                System.out.println(searched);
            }else{
                System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
            }
        }
        catch(Exception e) {
            System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
        }
    }

    private static Boolean linearSearch(ArrayList<Integer> list, Integer keyToSearch) {
        Boolean ans = false;
        for (Integer number : list) {
            if(number == keyToSearch) {
                ans = true;
                break;
            }
        }
        return ans;
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).