---
title: Insertion Sort in C++
layout: default
last-modified: 2020-05-02
featured-imaged: insertion-sort-in-every-language.jpg
tags: [c-plus-plus, insertion-sort]
authors:
  - sun-fox

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void insertSort(std::vector<int> &v)
{
    int n = v.size();
    int i = 0, j = 0, temp = 0;
    for (i = 1; i < n; i++)
    {
        int store = v[i];
        j = i - 1;
        while (store < v[j] && j >= 0)
        {
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = store;
    }
    return;
}

int main(int argc, char *argv[])
{
    std::vector<int> numbers;

    if (argc != 2)
    {
        std::cout << "Usage: please provide a list of at least two "
                     "integers to sort in the format \"1, 2, 3, 4, 5\""
                  << std::endl;
        return 1;
    }

    std::string str = argv[1];
    int i = 0, num = 0;
    if (str.size() < 2)
    {
        std::cout << "Usage: please provide a list of at least two "
                     "integers to sort in the format \"1, 2, 3, 4, 5\""
                  << std::endl;
        return 1;
    }

    std::stringstream ss(str);
    while (ss >> num)
    {
        numbers.push_back(num);

        if (ss.peek() == ',')
        {
            ss.ignore();
            ss.ignore();
        }

        else if (ss.tellg() != -1)
        {
            std::cout << "Usage: please provide a list of at least two "
                         "integers to sort in the format \"1, 2, 3, 4, 5\""
                      << std::endl;
            return 1;
        }
    }

    insertSort(numbers);

    for (i = 0; i < numbers.size() - 1; i++)
    {
        std::cout << numbers[i] << ", ";
    }
    std::cout << numbers[i] << std::endl;
    return 0;
}
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Prasun Kumar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 09 2019 21:10:56. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's walk through each line of code.

### Includes

In our sample, we include a single standard library utility:

```c++
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
```

Here, we can see that we include of `iostream` which contains the standard I/O
functions for printing messages onto the screen and for taking the inputs from the user.
The `bits/stdc++.h` includes common C++ header files.

### Handle Errors

This function is called when the command-line arguments are invalid. It displays the
usage statement and exits the program.

```c++
void handle_error()
{
    cout << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"" << endl;
    exit(0);
}
```

### Convert String to Array of Integers

```c++
vector<int> convert(string s)
{

    vector<int> v;
    string num = "";
    for (int i = 0; i < s.size(); i++)
    {
        if ((int)s[i] >= 48 && (int)s[i] <= 57 || s[i] == ' ')
        {
            num += s[i];
        }
        else if (s[i] == ',')
        {
            v.push_back(check(num));
            num = "";
        }
        else
        {
            handle_error();
        }
    }

    if (num.size() > 0)
    {
        v.push_back(check(num));
    }

    return v;
}
```

This function take a string containing a comma-separated list of integers
to sort and validate it. The `for` loop go through each character in the
string. When a number (from 48 to 57 -- from ASCII `0` to ASCII `9`) or a space is
detected, it appended to the `num` variable. When a comma is detected the
`check` function is called to convert it to an integer, and `push_back` is
called to append the integer to the vector `v`. If any other character is
detected, `handle_error` is called.

When the loop exits, `num` will either be empty, or it will contain the last
value. If `num is not empty, the last number is converted to an integer and
appended to the vector `v`.

Finally, the vector is returned to the caller.

### Check Function

```c+
int check(string s)
{
    int x1 = 0, x2 = s.size() - 1;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] != ' ')
        {
            x1 = i;
            break;
        }
    }

    for (int i = s.size() - 1; i >= x1; i--)
    {
        if (s[i] != ' ')
        {
            x2 = i;
            break;
        }
    }

    for (int i = x1; i <= x2; i++)
    {
        if (s[i] == ' ')
        {
            handle_error();
        }
    }

    return stoi(s);
}
```

This function is giving a string containing an individual value. It strips
off leading and trailing spaces. If there is no valid value, `handle_error`
is called.

### Insertion-Sort Function

In our sample, this function is responsible for sorting the array according
to the insertion sort algorithm:

```c++
void insertion_sort(string str, vector<int> arr) 
{ 

	stringstream ss;	 
	ss << str; 
	string temp; 
	int found; 
	while (!ss.eof()) 
	{ 
		ss >> temp; 
		if (stringstream(temp) >> found) 
		{
		    arr.push_back(found);
		}
		temp = ""; 
	} 
	
	int t,j;
    for(int i=1;i<arr.size();i++){
        t = arr[i];
        j = i-1;
        while(j >= 0 && t<=arr[j]){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = t;
    }
    
    int i;  
    for (i = 0; i < arr.size(); i++)  
        cout << arr[i] << " ";  
    cout << endl;
} 
```

Following are the explanation for the respective code snippets.

```c++
    stringstream ss;	 
    ss << str; 
    string temp; 
    int found; 
    while (!ss.eof()) 
    { 
        ss >> temp; 
        if (stringstream(temp) >> found) 
        {
            arr.push_back(found);
        }
        temp = ""; 
    } 
```

This section is responsible for extracting the numbers from the string and adding them to a vector,
so that easy iterative approach to insertion sort can be used.

```c++
    int t,j;
    for(int i=1;i<arr.size();i++){
        t = arr[i];
        j = i-1;
        while(j >= 0 && t<=arr[j]){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = t;
    } 
```

This section accepts the input array and the size of the array from the `main` function
Here we virtually divide the array into two parts i.e., the sorted and the unsorted part,
initially, the first element in the array is considered as sorted, even if it is not sorted.
Further, each element in the array is checked with the previous elements for the strict
inequality with each iteration, the sorting algorithm removes one element at a time and
finds the appropriate location within the sorted array and inserts it there. The iteration
continues until the unsorted array is empty, and get's it finally sorted.

Above you can see, that the variable `t` holds the unsorted array's first element and `j`
here keeps track of the index of the last element of the sorted array. Now we iterate 
throughout the remaining unsorted array one by one, finding a relevant position for the 
the value stored in 't' throughout the sorted array, as soon we get the desired location we 
place it there and then increment the sorted array end marker 'i' by unity.
This process continues until the array unsorted array size is reduced to zero.

### The display section

It's quite self-explanatory that it displays the new altered array:

```c++
    int i;  
    for (i = 0; i < n; i++)  
        cout << arr[i] << " ";  
    cout << endl; 
```

It takes the altered array and then prints it by iterating through it.

### Swap Function

This function swaps two values `x` and `y`. It is used for as part of the insertion sort
algorithm:

```c++
void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}
```

### The Main Function

As usual, C++ programs cannot be executed without a `main` function:

```c++
int main(int argc, char *argv[])
{
    ...
}
```

#### The Validation and Conversion Section

The first part of the `main` function validates the number of command-line
arguments. If there are too few, `handle_error` is called.

```c++
if (argc < 2)
{
    handle_error();
}
```

Next, the command-line argument is converted to a vector of integer values.
If there are too few values, the usage statement is displayed and the program
exits:

```c++
vector<int> v = convert(argv[1]);

if (v.size() < 2)
{
    cout << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"" << endl;
    exit(0);
}
```

#### The Insertion Sort Section

In our sample, this function is responsible for sorting the array according
to the insertion sort algorithm:

```c++
    int n = v.size();
    int min_idx;

    for (int i = 0; i < n - 1; i++)
    {
        min_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (v[j] < v[min_idx])
            {
                min_idx = j;
            }
        }
        swap(v[min_idx], v[i]);
    }
```

Here we virtually divide the array into two parts: the sorted and the unsorted part.
Initially, the first element in the array is considered as sorted, even if it is not sorted.
Further, each element in the array is checked with the previous elements for the strict
inequality with each iteration, the sorting algorithm removes one element at a time and
finds the appropriate location within the sorted array and inserts it there. The iteration
continues until the unsorted array is empty, and get's it finally sorted.

Above you can see, that the variable `min_index` starts out as the index of the sorted
array's first element (`i`). The variable `j` loops over the unsorted portion of the array.
By the end of the `for j` loop, `min_index` contains the index of the minimum unsorted
value. The `swap` function swaps the minimum value in the unsorted portion of the array
at `min_index` with the current value in the sorted portion of the array at `i`.

We continue to iterate `i` until the array is sorted.

#### The Display Section

Finally, the sorted vector is displayed:

```c++
for (int i = 0; i < n - 1; i++)
{
    cout << v[i] << ", ";
}
cout << v[n - 1];
```

And that's it!


## How to Run the Solution

One can run the code on C++ IDE's like [CodeBlocks][1], [Turboc++][2], [Eclipse for C/C++][3], etc.
Their installation is guided by the setup wizards and once install can allow you to 
run the locally on your machine, all these IDE's are available free of cost on their
respective websites.

Perhaps the easiest way to run the solution is to leverage the online gdb 
compiler.

Alternatively, you can try to run the C++ code in a similar way described in the last article. Honestly, it's pretty easy to write and run C/C++ code 
on most platforms:

```console
gcc -o insertion-sort reverse-string.cpp
```

Unfortunately, Windows pretty much requires the use of [Visual Studio][4]. So, 
instead of sharing platform-specific directions, I'll fall back on my
[online compiler recommendation][5].

[1]: https://www.codeblocks.org/
[2]: https://developerinsider.co/download-turbo-c-for-windows-7-8-8-1-and-windows-10-32-64-bit-full-screen/
[3]: https://www.eclipse.org/downloads/packages/release/2023-03/r/eclipse-ide-cc-developers
[4]: https://visualstudio.microsoft.com/downloads/
[5]: https://www.onlinegdb.com/online_c++_compiler
