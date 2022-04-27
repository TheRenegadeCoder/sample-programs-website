At this point, we probably want to actually run the Hello World in 
Kotlin code snippet. Perhaps the easiest way to do so is to leverage 
the online Kotlin editor.

Alternatively, we can use the latest standalone compiler. Of course, 
we’ll want to get a copy of Hello World in Kotlin while we’re at it. 
With both in hand, all we need to do is navigate to the folder containing 
our files and run the following:

```shell
kotlinc hello-world.kt -include-runtime -d hello-world.jar
java -jar hello-world.jar
```

Apparently, the standalone Kotlin compiler compiles Kotlin down to a 
runnable jar which we can then execute using the Java Runtime 
Environment. Of course, I haven’t tried it. After all, I pulled these 
directions from Kotlin documentation. Let me know if this works in the 
comments.
