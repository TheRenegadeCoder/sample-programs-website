---

---

Welcome to the Palindromic Number in C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
/*
 accept an integer, reverse it, compare it with original
 print true, if original and reversed number are same
 print false, if original and reversed number are same
*/
#include <stdio.h>
#include <stdlib.h>

void palindromic_number(int number){
  int temp = number, no_of_digits = 0,reversed_number = 0;

  while (temp > 0){
    reversed_number = (reversed_number * 10) + (temp % 10);
    temp = (int)(temp / 10);
    no_of_digits ++;
  } /*end of building reverse number*/
  
  if (no_of_digits < 2){
    printf("Usage: please input a number with at least two digits");
    exit(1);  
  }
  else{
    if (reversed_number == number){
      printf("true");
    }
    else{
      printf("false");
    }
  } /*end of more than 2 digit number check*/
 /*end of palindromic_number function*/
}

/*Return 1 if number, else return 0*/
int is_int(char *number_string){
  if(number_string[0] > '9' || number_string[0] < '0')
    return(0);
  for (int counter = 0; number_string[counter]; counter++){
    if(number_string[0] > '9' || number_string[0] < '0')
      return(0);
  }
  return(1);    

}

/* accept only integers with minimum 2 digits */
int main(int argc, char **argv){
  /*Read command line arg*/
  if (argc != 2 || is_int(argv[1]) != 1){
    printf("Usage: please input a number with at least two digits");    
    return(1);  
  }
   palindromic_number(atoi(argv[1]));
   return(0);
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.