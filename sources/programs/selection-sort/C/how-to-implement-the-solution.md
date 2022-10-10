### Selection Sort in C

Selection sort is another algorithm that is used for sorting. This sorting algorithm, iterates through the array and finds the smallest number in the array and swaps it with the first element if it is smaller than the first element. Next, it goes on to the second element and so on until all elements are sorted.

### Example of Selection Sort

Consider the array:= [10,5,2,1]

The first element is 10. The next part we must find the smallest number from the remaining array. The smallest number from 5 2 and 1 is 1. So, we replace 10 by 1.

The new array is [1,5,2,10] Again, this process is repeated.

Finally, we get the sorted array as [1,2,5,10].

Let us continue with this article on Selection Sort in C and see how the algorithm works,

### Algorithm for Selection Sort:

**Step 1** − Set min to the first location

**Step 2** − Search the minimum element in the array

**Step 3** – swap the first location with the minimum value in the array

**Step 4** – assign the second element as min.

**Step 5** − Repeat the process until we get a sorted array.

Let us take a look at the code for the the programmatic implementation,

### Code for Selection Sort

```c
#include <stdio.h>
int main()
{
    int a[100], n, i, j, position, swap;
    printf("Enter number of elementsn");
    scanf("%d", &n);
    printf("Enter %d Numbersn", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for(i = 0; i < n - 1; i++)
    {
        position=i;
        for(j = i + 1; j < n; j++)
        {
            if(a[position] > a[j])
            position=j;
        }
        if(position != i)
        {
            swap=a[i];
            a[i]=a[position];
            a[position=swap;
        }
    }
    printf("Sorted Array:n");
    for(i = 0; i < n; i++)
    printf("%dn", a[i]);
    return 0;
}
```
