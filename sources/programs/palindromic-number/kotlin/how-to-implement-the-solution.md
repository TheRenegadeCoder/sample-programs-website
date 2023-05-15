We first create some variables we will use in the algorithm in the `main` function as shown here:

```kotlin
fun main(args: Array<String>) {
    var n: Int
    var num: Int
    var digit: Int
    var rev: Int = 0
 ```

 Then we will convert the input argument from a string to an integer:

 ```kotlin
try {
    num = args[0].toInt()

    if (num >= 0){
        ...
    }else{
        println("Usage: please input a non-negative integer")
    }


}catch(e: Exception){
    println("Usage: please input a non-negative integer")
}
```

If there is an error or the number is negative, we display the usage statement.

```kotlin
 Then we use a `do` while loop to reverse the number that was typed in:

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
