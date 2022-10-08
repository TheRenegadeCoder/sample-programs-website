
### Solution

At this point, let's dig into the code a bit. The following sections break down the Binary Search in Java functionality.


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
 
