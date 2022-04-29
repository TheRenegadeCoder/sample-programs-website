---

title: Bubble Sort in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Bubble Sort in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Java
import java.util.ArrayList;

public class BubbleSort {

    public static void main(String[] args) {
        try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            String[] NumberArray = args[0].split(",");
            for(String Number: NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            if(listOfNumbers.size() >= 2){
                StringBuilder output = new StringBuilder();
                ArrayList<Integer> SortedList = sort(listOfNumbers);

                for(Integer Number: SortedList){
                    if(SortedList.indexOf(Number) == 0){
                        output.append(Number);
                    }else{
                        output.append(", ").append(Number);
                    }
                }
                System.out.println(output);
            }else{
                System.out.println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
            }
        }
        catch(Exception e) {
            System.out.println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        }
    }

    private static ArrayList<Integer> sort(ArrayList<Integer> list){
        int memory;
        for(int i = 1; i < list.size(); i++) {
            for(int j=0; j< list.size() - i; j++) {
                if(list.get(j) > list.get(j+1)) {
                    memory = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, memory);
                }
            }
        }
        return list;
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.