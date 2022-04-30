---

title: Hello World in C#
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-c-sharp-featured-image.JPEG
tags: [c-sharp, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
namespace SamplePrograms
{
    public class HelloWorld
    {
        static void Main()
        {
            System.Console.WriteLine("Hello, World!");
        }
    }
}
```

{% endraw %}

## How to Implement the Solution

Now, we can implement Hello World in C# in a couple of ways. For simplicity,
I'll share the minimalist approach but be aware that there are more complete ways
to do this:

```csharp
class HelloWorld {
  static void Main() {
    System.Console.WriteLine("Hello, World!");
  }
}
```

If you read the Hello World in Java tutorial, then this probably looks very
similar. In fact, C# shares a lot of the same look and feel as Java. With that
being the case, I'll only highlight the major pieces here.

Before we can print, we have to create a class. Inside our class, we declare
the main method. And inside our main method, we run our print command. The syntax
and core libraries are a little different, but it feels eerily similar to Java.


## How to Run the Solution

Perhaps the easiest way to run this solution would be to open up an online C#
compiler. Just copy the code from above and drop it into the editor before
hitting run.

Alternatively, we can download Visual Studio or Mono to run C# locally. Of
course, we'll want a copy of the solution as well. Refer to the manual of the
various tools to run C#.

As far as I know, there aren't any easy ways to run C# code from the command
line, but I imagine it can be done.
