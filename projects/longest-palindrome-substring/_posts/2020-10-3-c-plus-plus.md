---
title: Longest Palindromic Substring in Every Language
layout: default
date: 2019-10-08
last-modified: 2020-05-02
featured-image:
tags: [longest-palindrome-substring]
authors: 
  - Sayantan Paul
  - Hemabh Ravee
---

Given a string, we need to find the smallest substring inside the main string which is a palindrome.

## How to Implement the Solution
We will implement the solution using Method 3.
The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far.
* Time Complexity: O ( n^2 )
* Auxiliary Space: O ( 1 )

### Solution Code
```c++
#include <bits/stdc++.h> 
using namespace std; 

void printSubStr(char* str, int low, int high) 
{ 
	for (int i = low; i <= high; ++i) 
		cout << str[i]; 
} 

int longestPalindrome(char* str) 
{ 
	int maxLength = 1; 
	int start = 0; 
	int len = strlen(str); 
	int low, high; 

	for (int i = 1; i < len; ++i) { 

		low = i - 1; 
		high = i; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
		low = i - 1; 
		high = i + 1; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
	} 

	cout << "Longest palindrome substring is: "; 
	printSubStr(str, start, start + maxLength - 1); 

	return maxLength; 
} 

int main() 
{ 
	char str[] = "paapaapap"; 
	cout << "\nLength is: "
		<< longestPalindrome(str) 
		<< endl; 
	return 0; 
} 
```

Lets go over the entire code now -

### Print Substring Function

A utility function to print a substring ```str[low..high] ```
```c++
void printSubStr(char* str, int low, int high) 
{ 
	for (int i = low; i <= high; ++i) 
		cout << str[i]; 
} 
```

### Longest Palindrome Function
This function prints the longest palindrome substring (LPS) of str & it's length.
```c++
int longestPalindrome(char* str) 
{ 
	int maxLength = 1; 
	int start = 0; 
	int len = strlen(str); 
	int low, high; 

	for (int i = 1; i < len; ++i) { 

		low = i - 1; 
		high = i; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
		low = i - 1; 
		high = i + 1; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
	} 

	cout << "Longest palindrome substring is: "; 
	printSubStr(str, start, start + maxLength - 1); 

	return maxLength; 
} 
```

This function can be broken into 3 sections - 

1.  Function Attributes - 
	```c++
	int maxLength = 1; 
	int start = 0; 
	int len = strlen(str); 
	int low, high; 
	```

	```maxlength``` will hold the final result(length of LPS) <br>
	```start``` will hold the index of first character of LPS <br>
	```len``` just holds the length of input string <br>
	```low``` and ```high``` are variables using for iterating

2.  Next, we have a for loop which considers every character as center point of even and odd length palindromes and thus, finds the LPS
	```c++
	for (int i = 1; i < len; ++i) { 

		low = i - 1; 
		high = i; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
		low = i - 1; 
		high = i + 1; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			--low; 
			++high; 
		} 
	} 
	```
	This can further be divided in two sections - <br> 
	1. Find the longest even length palindrome with center points as i-1 and i. 
	2. Find the longest odd length palindrome with center point as i <br>

	Lets go over both these sections -
	1. Finding longest even length palindrome. 
	The idea is to fix two centres ( low and high ) and expand in both directions for longer palindromes.
		```c++
		low = i - 1; 
		high = i; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 

			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 

			++high; 
			--low; 
		} 
		```
		* ```low``` and ```high``` start with the center values ```i-1``` & ```i```
		* Hence, length of ```str[low..high]``` is always even
		* The while loop condition checks that ```low``` & ```high``` are not out of bound and that the string ```str[low..high]``` is a palindrome
		* If length of ```str[low..high]``` is more than current ```maxLength```, update ```maxLength``` as well as ```start```
		* Finally, we perform increment and decrement on the iterables

	2. Find the longest odd length palindrome.
	The idea is to fix a centre and expand in both directions for longer palindromes.
		```c++
		low = i - 1; 
		high = i + 1; 
		while (low >= 0 && high < len 
			&& str[low] == str[high]) { 
			if (high - low + 1 > maxLength) { 
				start = low; 
				maxLength = high - low + 1; 
			} 
			++high; 
			--low; 
		} 
		```
		* Every character is a palindrome so ```str[i]``` is already a palindrome
		* So, ```low``` and ```high``` start with the center values ```i-1``` & ```i+1```
		* Hence, length of ```str[low..high]``` is always odd
		* The while loop condition checks that ```low``` & ```high``` are not out of bound and that the string ```str[low..high]``` is a palindrome
		* If length of ```str[low..high]``` is more than current ```maxLength```, update ```maxLength``` as well as ```start```
		* Finally, we perform increment and decrement on the iterables


3. The display section is pretty obvious. We print the LPS using our stored values of ```start``` and ```maxLength```, & then we return the ```maxLength```
	```c++
	cout << "Longest palindrome substring is: "; 
	printSubStr(str, start, start + maxLength - 1); 

	return maxLength; 
	```

### The Main Function

```c++
int main() 
{ 
	char str[] = "paapaapap"; 
	cout << "\nLength is: "
		<< longestPalindrome(str) 
		<< endl; 
	return 0; 
} 
```
As usual, C++ programs cannot be executed without a main function. 
Here, we just create a string, pass it to ```longestPalindrome``` function and print the return value. 

## How to Run the Solution

One can run the code on C++ IDE's like CodeBlocks, Turboc++, Eclipse for C/C++, etc. Their installation is guided by the setup wizards and once install can allow you to run the locally on your machine, all these IDE's are available free of cost on their respective websites.

Perhaps the easiest way to run the solution is to leverage the online gdb 
compiler.

	
