Online compilers such as [Kotlin Playground][2] or this [Online Kotlin Compiler][3] are a good way to get started.

To run on a personal computer, the ideal environment is [IntelliJ IDEA][4], as it and kotlin were both created by JetBrains.
If you have installed the command line version however, save the program to FizzBuzz.kt and run with these commands.
```bash
kotlinc FizzBuzz.kt -include-runtime -d FizzBuzz.jar
java -jar FizzBuzz.jar
```
