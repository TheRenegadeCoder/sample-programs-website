To run the solution to check if a number is a palindrome or not, we first create some variables we will use in the algorithm in the main function as shown here:
```kotlin
    var n: Int
    var num: Int
    var digit: Int
    var rev: Int = 0
 ```
 Then we will prompt the user to input the number that needs to be checked:
 ```kotlin
    print("Enter a positive number: ")
    num = readLine()!!.toInt()
 ```
 Then we use a do while loop to reverse the number that was typed in:
 ```kotlin
    do {
        digit = num % 10
        rev = (rev * 10) + digit
        num = num / 10
    }while (num != 0)
```
Finally, we check if the number and its reverse are the same or not. If they are the same, we tell the user that it's true, otherwise we tell the user that it's false, as shown here:
```kotlin
    if (n == rev){
        println(true)
    }else{
        println(false)
    }
```
