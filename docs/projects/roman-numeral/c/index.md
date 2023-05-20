---
title: Roman Numeral in C  
layout: default  
date: 2021-10-27
last-modified: 2021-10-27
featured-imaged: roman-numeral-in-every-language.jpg
tags: [c, roman-numeral]  
authors:
- shubhragupta-code

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include  <stdio.h>
#include <stdlib.h>
#include <string.h>

int val[150];

int main(int argc,char **argv)
{
    if(argv[1]==NULL){
        printf("Usage: please provide a string of roman numerals");
        return 0;
    }
    if(strlen(argv[1])==0){
        printf("0");
        return 0;
    }
    
    int len=strlen(argv[1]);
    val['I']=1;
    val['V']=5;
    val['X']=10;
    val['L']=50;
    val['C']=100;
    val['D']=500;
    val['M']=1000;
    long long ans=0;
    
    for(int i=1;i<len;++i){
        if(!val[argv[1][i]]){
            printf("Error: invalid string of roman numerals");
            return 0;
        }
        if(val[argv[1][i]]>val[argv[1][i-1]])ans-=2*val[argv[1][i-1]];
        ans+=val[argv[1][i]];
    }
    if(!val[argv[1][0]]){
        printf("Error: invalid string of roman numerals");
        return 0;
    }
    printf("%lld",ans+val[argv[1][0]]);
}
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C](https://sampleprograms.io/languages/c) was written by:

- LezendarySandwich

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 20 2019 12:36:36. The solution was first committed on Oct 20 2019 11:59:04. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's understand this code block by block in the order of execution.

### Main Function

```c
#include  <stdio.h>
#include <stdlib.h>
#include <string.h>

int val[150];
```

In the first three lines, we are including header files using [include directive][1] to utilize some functions defined in header files later in the program.
Here, Standard Input/Output header file(*\<stdio.h\>*) is called to use **printf()** function and *\<string.h\>* to use **strlen()** function. **[strlen()][2]** returns the length of string and **[printf()][3]** prints formatted string as output.
We are also declaring a variable of length 150.

Now let's move on the `main` function.

```c
int main(int argc,char **argv)
{
    ...
}
```

In C, we declare a function using general form:

```
return_type function_name(parameter){
  ...
}
```

So, we are declaring main function with return_type integer and **argc** and **argv** as parameters to access command line arguments.
**argc** and **argv** are variables which `main` function will get when run in command-line. **argc** stores argument count while **argv** stores array of strings that are arguments. This should be kept in mind that all command-line arguments are stored as strings.

**argv[0]** represents first argument which always is equal to name of our program. If we type the following command in terminal:

```console
./roman-numeral IV
```

Here, ```./roman-numeral``` represents **argv[0]** and ```IV``` represents **argv[1]**.

### Control Flow

```c
if(argv[1]==NULL){
    printf("Usage: please provide a string of roman numerals");
    return 0;
}
```

First if condition checks if the argument provided is a null string or not. If so, it prints correct usage pattern and returns with exit code of 0.

```c
if(strlen(argv[1])==0){
    printf("0");
    return 0;
}
```
Now, if length of the argument provided is 0, then it prints **0** and returns with value 0.

```c
int len=strlen(argv[1]);
val['I']=1;
val['V']=5;
val['X']=10;
val['L']=50;
val['C']=100;
val['D']=500;
val['M']=1000;
long long ans=0;
```

This blocks initialize a integer variable with the length of string provided by the argument. It also initializes the array. Since, in C we directly do not have dictionaries, here we have utilised the power of ASCII values. "I" has an [ASCII][4] value of 73. So, at **val[73] = 1**. Remaining values also get assigned in the similar fashion. Next 'long long' datatype variable **ans** is initialized with value of 0.

```c
for(int i=1;i<len;++i){
    if(!val[argv[1][i]]){
        printf("Error: invalid string of roman numerals");
        return 0;
    }
    if(val[argv[1][i]]>val[argv[1][i-1]])ans-=2*val[argv[1][i-1]];
    ans+=val[argv[1][i]];
}
```

Now, in this `for` loop, first `if` conditions check if the each letter in the alphabet is a Roman Numeral. If it is not, it prints Error and exits the main function with exit code 0. Else, it proceeds with the rest of the function.
If a smaller value appears before a larger one, the smaller value is subtracted 2 times from the **ans**. Then, each value is added in the **ans**.

```c
if(!val[argv[1][0]]){
    printf("Error: invalid string of roman numerals");
    return 0;
}
printf("%lld",ans+val[argv[1][0]]);
```

Since in the above `for` loop, we have not considered the value of **argv[1][0]**, we check if it is correct Roman Numeral and prints error message if it is not.
Lastly, we print **ans + val[argv[1][0]]** using the format specifier **%lld** for long long datatype.  

[1]: https://en.wikipedia.org/wiki/Include_directive
[2]: https://man7.org/linux/man-pages/man3/strlen.3.html
[3]: https://man7.org/linux/man-pages/man3/printf.3.html
[4]: https://en.wikipedia.org/wiki/ASCII


## How to Run the Solution

```console
gcc -o roman-numeral roman-numeral.c
./roman-numeral
```
Another handy option is to compile and run using online C Compiler such as [OnlineGDB][5], [Repl][6]

[5]: https://www.onlinegdb.com/
[6]: https://replit.com/languages/c
