---

title: Binary Search in Java
layout: default
last-modified: 2020-10-08
featured-image: binary-search-in-every-language.jpg
tags: [java, binary_search]
authors:
  - s18k

---

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class BinarySearch{  
 public static void binarySearch(ArrayList<Integer> arr, int first, int last, int key){  
   int mid = (first + last)/2;  
   while( first <= last ){  
      if ( arr.get(mid) < key ){  
        first = mid + 1;     
      }else if ( arr.get(mid) == key ){  
        System.out.println("True");  
        break;  
      }else{  
         last = mid - 1;  
      }  
      mid = (first + last)/2;  
   }  
   if ( first > last ){  
      System.out.println("False");  
   }  
 }  
 public static void main(String args[]){ 
    try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            String[] NumberArray = args[0].split(",");
            for(String Number: NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            int key = Integer.parseInt(args[1].trim());  
            int last=listOfNumbers.size()-1;  
            for(int i=0;i<last-1;i++){
                if(listOfNumbers.get(i)>listOfNumbers.get(i+1)){
                    System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
                    System.exit(1);
                }
            }
            binarySearch(listOfNumbers,0,last,key); 
        }
        catch(Exception e) {
            System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
        } 
 }  
}
```

{% endraw %}

[Binary Search](https://sampleprograms.io/projects/binary-search) in [Java](https://sampleprograms.io/languages/java) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution


### Solution


```
import java.util.ArrayList;
import java.util.Collections;

class BinarySearch {
    public static int binarySearch(int array[], int element) {
        int startIndex = 0;
        int endIndex = array.length - 1;
        int middleIndex = (startIndex + endIndex) / 2;

        while (startIndex <= endIndex) {
            if (array[middleIndex] == element) {
                return middleIndex;
            } else if (array[middleIndex] < element) {
                startIndex = middleIndex + 1;
            } else {
                endIndex = middleIndex - 1;
            }
            middleIndex = (startIndex + endIndex) / 2;
        }
        // if Element is not found
        return -1;
    }

    public static boolean isSorted(int array[], ArrayList<Integer> arrayList) {
        Collections.sort(arrayList);
        for (int i = 0; i < array.length; i++) {
            if (array[i] != arrayList.get(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        if (args.length != 2) {
            System.out.println("Wrong Input given ");
            System.out.println("Expected input \" Array of Integers \" \" Integer to be found \" ");
            return;
        }
        String arrayString = args[0];
        int element = Integer.parseInt(args[1]);
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (String character : arrayString.split(",")) {
            arrayList.add(Integer.parseInt(String.valueOf(character)));
        }
        int array[] = new int[arrayList.size()];
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
        if (isSorted(array, arrayList)) {
            int index = binarySearch(array, element);
            if (index == -1) {
                System.out.println("Element " + element + " not found in the Array");
            } else {
                System.out.println("Element " + element + " Found at index " + index);
            }
        } else {
            System.out.println("Given input array is not sorted");
        }

    }
}
```


### The Main Function

```
public static void main(String args[]) {
        if (args.length != 2) {
            System.out.println("Wrong Input given ");
            System.out.println("Expected input \" Array of Integers \" \" Integer to be found \" ");
            return;
        }
        String arrayString = args[0];
        int element = Integer.parseInt(args[1]);
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (String character : arrayString.split(",")) {
            arrayList.add(Integer.parseInt(String.valueOf(character)));
        }
        int array[] = new int[arrayList.size()];
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
        if (isSorted(array, arrayList)) {
            int index = binarySearch(array, element);
            if (index == -1) {
                System.out.println("Element " + element + " not found in the Array");
            } else {
                System.out.println("Element " + element + " Found at index " + index);
            }
        } else {
            System.out.println("Given input array is not sorted");
        }

    }
    
```
This is the main function and is automatically executed when this Java file runs
The input to the main function is supplied in the form of command line arguments. eg String "10,20,30,40,50" and the element to be found "40"
The function splits this input through the delimeter ',' and converts the strings to integer array.
The isSorted function is called to check if the given input array is sorted If not it throws the Error "Given input array is not sorted"
If the input array is sorted the binary search function is called 

### Binary Search

```
public static int binarySearch(int array[], int element) {
        int startIndex = 0;
        int endIndex = array.length - 1;
        int middleIndex = (startIndex + endIndex) / 2;

        while (startIndex <= endIndex) {
            if (array[middleIndex] == element) {
                return middleIndex;
            } else if (array[middleIndex] < element) {
                startIndex = middleIndex + 1;
            } else {
                endIndex = middleIndex - 1;
            }
            middleIndex = (startIndex + endIndex) / 2;
        }
        // if Element is not found
        return -1;
    }
```

* First, the search space must have constant time random access (i.e. an array). In addition, the search space must be sorted by some attribute. As a consequence, we're able to navigate the search space in O(log(N)) instead of O(N).

* If the middle element is greater than the element we want to find, we know that the element must be "to the left" of that element, assuming the collection is sorted least to greatest. From there, we can try the element in the middle of the left half, and so on

* Eventually, we'll find the element we're looking for and return true, or we'll reach the end of our search and return false. 
 


## How to Run the Solution

* Save the code as a .java file eg BinarySearch.java
* Run the command ``` javac BinarySearch.java ``` in the directory containing this file
* Run the command with the desired input arguments eg ``` java BinarySearch "10,20,30,40,50" "40" ``` 
