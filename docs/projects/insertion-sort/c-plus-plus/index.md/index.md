---

title: Insertion Sort in C++
layout: default
last-modified: 2020-05-02
featured-image:
tags: [c-plus-plus, Insertion-sort]
authors:
  - sun-fox

---

Welcome to the Insertion Sort in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C++
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

//Insertions sort algorithm
void insertSort(std::vector <int> &v){
        int n = v.size();
        int i = 0, j = 0, temp = 0;
        for(i = 1; i < n; i++){
		int store = v[i];
		j = i-1;
		while(store < v[j] && j >= 0){
			v[j+1] = v[j];
			j--;
		}
		v[j+1] = store;
        }
        return;
}

//Driver program
int main(int argc, char* argv[]){
    std::vector <int> numbers;

    if(argc != 2){
        std::cout << "Usage: please provide a list of at least two "
                    "integers to sort in the format \"1, 2, 3, 4, 5\"" << std::endl;
        return 1;
    }

    std::string str = argv[1];
    int i = 0, num = 0;
    if(str.size() < 2){
        std::cout << "Usage: please provide a list of at least two "
                    "integers to sort in the format \"1, 2, 3, 4, 5\"" << std::endl;
        return 1;
    }

    std::stringstream ss(str);
    while(ss >> num){
        numbers.push_back(num);

        // If the next character is comma then ignore it and the next whitespace
        if(ss.peek() == ','){
            ss.ignore();
            ss.ignore();
        }

        /* If the next character after the number is not a comma it checks
            whether it is the end of stream otherwise throws an error for
            wrong input format.
        */
        else if(ss.tellg()!=-1){
            std::cout << "Usage: please provide a list of at least two "
                        "integers to sort in the format \"1, 2, 3, 4, 5\"" << std::endl;
            return 1;
        }
    }
    
    insertSort(numbers);

    for(i = 0; i < numbers.size() - 1; i++){
        std::cout<< numbers[i] << ", ";
    }
    std::cout << numbers[i] << std::endl;
    return 0;
}

```

## How to Implement the Solution

Let's first take a look at the solution. Then, we'll walk through each line of code:

```c++
#include <iostream> 
#include <sstream> 
#include <string>
#include <vector>
using namespace std;

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

int main() 
{ 

	string str;
	vector<int>arr;
	getline (cin, str); 
	insertion_sort(str,arr); 
	return 0; 
} 
```

### Includes

In our sample, we include a single standard library utility:

```c++
#include <iostream> 
#include <sstream> 
#include <string>
#include <vector>
using namespace std;
```

Here, we can see that we include the standard I/O for printing messages onto the
screen and for taking the inputs from the user. The string stream library for accessing the string, the string to use the string data type as it not predefined in C++. The vector library to implement the concept of dynamic datatype vector.

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
This section accepts the input array and the size of the array from the main function 
Here we virtually divide the array into two parts i.e., the sorted and the unsorted part,
initially, the first element in the array is considered as sorted, even if it is not sorted.
Further, each element in the array is checked with the previous elements for the strict
inequality with each iteration, the sorting algorithm removes one element at a time and
finds the appropriate location within the sorted array and inserts it there. The iteration
continues until the unsorted array is empty, and get's it finally sorted.

Above you can see, that the variable 't' holds the unsorted array's first element and 'j' 
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

### The Main Function

As usual, C++ programs cannot be executed without a main function:

```c++
int main()  
{  

    string str;
	vector<int>arr;
	getline(cin, str); 
	insertion_sort(str,arr); 
	return 0;  
} 
```

Here the getline function is used to input data in a line from the user.

The for loop is responsible for the input into the array.
Here, we make a call to each function we've created:�`insertion_sort(str, arr)`, bypassing
the string input and the array to the function such that they match with their respective function signatures. And, that's it!



## How to Run the Solution

One can run the code on C++ IDE's like CodeBlocks, Turboc++, Eclipse for C/C++, etc.
Their installation is guided by the setup wizards and once install can allow you to 
run the locally on your machine, all these IDE's are available free of cost on their
respective websites.

Perhaps the easiest way to run the solution is to leverage the online gdb 
compiler.

Alternatively, you can try to run the C++ code in a similar way described in the last article. Honestly, it�s pretty easy to write and run C/C++ code 
on most platforms:

```console
gcc -o reverse-string reverse-string.cpp
```

Unfortunately, Windows pretty much requires the use of Visual Studios. So, 
instead of sharing platform-specific directions, I�ll fall back on my online compiler recommendation.[^1]
