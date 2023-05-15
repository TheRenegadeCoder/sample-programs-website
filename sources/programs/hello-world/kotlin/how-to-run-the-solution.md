At this point, we probably want to actually run the Hello World in
Kotlin code snippet. Perhaps the easiest way to do so is to leverage
the online Kotlin editor.

Alternatively, we can use the latest [standalone compiler][1]. Of course,
we'll want to get a copy of [Hello World in Kotlin][2] while we're at it.
With both in hand, all we need to do is navigate to the folder containing
our files and run the following:

```shell
kotlinc HelloWorld.kt -include-runtime -d HelloWorld.jar
java -jar HelloWorld.jar
```

The standalone Kotlin compiler compiles Kotlin down to a
runnable Java Archive (`jar`) which we can then execute using the Java Runtime
Environment.

[1]: https://kotlinlang.org/docs/command-line.html#manual-install
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/k/kotlin/HelloWorld.kt
