At this point, let's dig into the code a bit. The following sections break down the Binary Search in Java functionality.

### The Main Function

```java
public static void main(String args[]) {
    try {
        ArrayList<Integer> listOfNumbers = new ArrayList<>();
        String[] NumberArray = args[0].split(",");
        for (String Number : NumberArray) {
            listOfNumbers.add(Integer.parseInt(Number.trim()));
        }
        int key = Integer.parseInt(args[1].trim());
        int last = listOfNumbers.size() - 1;
        for (int i = 0; i < last - 1; i++) {
            if (listOfNumbers.get(i) > listOfNumbers.get(i + 1)) {
                System.out.println(
                        "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
                System.exit(1);
            }
        }
        binarySearch(listOfNumbers, 0, last, key);
    } catch (Exception e) {
        System.out.println(
                "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
    }
}
```
This is the main function and is automatically executed when this Java file runs.
* The input to the main function is supplied in the form of command line arguments, e.g., String "10,20,30,40,50" and the element to be found "40".
* The function splits this input through the delimeter ',' and converts the strings to integer array.
* The function checks if the array is sorted. 
* If the input array is sorted the binary search function is called.
* The "usage" statement is displayed and the program exits if the command line arguments are incorrect, the list is not sorted, or anything throws an exception.

### Binary Search

```java
public static void binarySearch(ArrayList<Integer> arr, int first, int last, int key) {
    int mid = (first + last) / 2;
    while (first <= last) {
        if (arr.get(mid) < key) {
            first = mid + 1;
        } else if (arr.get(mid) == key) {
            System.out.println("True");
            break;
        } else {
            last = mid - 1;
        }
        mid = (first + last) / 2;
    }
    if (first > last) {
        System.out.println("False");
    }
}
```

* First, the search space must have constant time random access (i.e., an array). In addition, the search space must be sorted by some attribute. As a consequence, we're able to navigate the search space in O(log(N)) instead of O(N).

* If the middle element is greater than the element we want to find, we know that the element must be "to the left" of that element, assuming the collection is sorted least to greatest. From there, we can try the element in the middle of the left half, and so on

* Eventually, we'll find the element we're looking for and display "True", or we'll reach the end of our search and display "False". 
