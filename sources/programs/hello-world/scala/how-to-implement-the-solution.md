At long last, let’s implement Hello World in Scala:

```scala
object HelloWorld extends App {
  println("Hello, World!")
}
```

Up first, we have the class definition much like Java. However, 
there are two interesting keywords here: object and extends.

In Java, we would typically define a class using the class keyword. 
In fact, we normally even do that in Scala, so what’s with this 
object keyword? Well, as it turns out, object is used when we want 
to define a singleton.

In object-oriented languages, a singleton is an object which has a 
one and only one policy. In other words, only one instance of the 
object will ever exist. Personally, I’ve only ever used the singleton 
design pattern to track state in a video game. Beyond that, I would 
consider it an anti-pattern.

That said, singletons are a feature in Scala, and they’re typically 
used to define static functions. In other words, singletons can be 
used to generate utility classes that don’t need to be instantiated 
to access their functionality.

In addition, singletons in Scala are often used as companion objects, 
but I can’t say I totally understand what that is. Let me know in the 
comments.

Anyway, in this case, our singleton also extends App. This allows us 
to bypass the creation of a main method. We could have just as easily 
implemented Hello World in Scala as follows:

```scala
object HelloWorld {
    def main(args: Array[String]): Unit = {
        println("Hello, World!");
    }
}
```

At this point, we have something reminiscent of Java. Of course, the syntax 
is a bit different, but it looks about the same if we squint hard enough.

Finally, the only thing we have left is the print statement which is pretty 
typical at this point. Not much of a surprise there!
