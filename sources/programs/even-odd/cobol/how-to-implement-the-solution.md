Let us try to understand the code step-wise. 

First, we must make sure we include the mandatory `DIVISIONS` in the beginning. The `IDENTIFICATION DIVISION` is used to specify the metadata of the program including the `PROGRAM-ID`. In this case, we have written `EVEN-ODD` to identify the code.

Next comes the `DATA DIVISION`. Here, we define our data variables, which will contain data like integer, alphabets etc. Here, we have mentioned `CMDARGS` and `NUM` which are short for Command Arguments and Number respectively. `PIC` stands for 'Picture Clause' which defines the type and size of data. `X` means an Alpha-numeric data can be expected in Command Arguments (maximum size is 38 bytes). We have used alphanumeric because the user can also enter alphabets instead of a number. On the other hand, `S9` shows that a number with positive or negative values can be expected as data (maximum size is 30 bytes).

Moving on, we encounter `PROCEDURE DIVISION`. This section includes the actual code with its functions. To solve this problem, we will use a computing operator 'Modulo' (%) which divides one number from the other and returns the remainder. So, if we divide any even number with 2, the remainder will always be 0, whereas, if we divide any odd number with 2, the remainder would be 1. 

For example, 12 % 2 = 0 and 13 % 2 = 1.

`ACCEPT` is a keyword used to accept arguments (data) from the Command-Line. So, this statement is used to accept the data entered by the user and run it through the code.

If command arguments are alphabetic, the program will display the error message `Usage: please input a number` and stop the program.

`NUMVAL` extracts numeric data from an alphanumeric data and stores them.

Next, we have nested (one inside the other) IF conditions. `IF NUM IS NUMERIC THEN` is used to make sure again that we are only using a numeric data to print an output. So, if the data entered is a number, the program will go ahead with this condition and the `MOD` (modulo) operator will be applied on the number.

`MOD (NUM, 2) = 0 THEN DISPLAY "Even"`. If the remainder is 0, then the number is even and so is the output.

If this condition is not true, i.e., if the remainder is not 0, the output will be `"Odd"`.

And finally, if the data is not a number, the output will be an error message "Usage: please input a number". 
