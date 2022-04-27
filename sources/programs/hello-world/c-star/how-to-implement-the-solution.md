At long last, here’s Hello World in C*:

```cstar
#include <stdio.h>
main ()
{
    printf("Hello, World!")
}
```

As we can see, Hello World in C* looks alarmingly similar to C. That said, C*
is a superset of C, so this shouldn’t be too much of a surprise. At any rate,
let’s dig in.

Up first, we have the include statement which pulls in the stdio header. With
the standard IO header included, we’re able to write to standard output using
printf.

Next, we have our usual main function declaration which serves as the drop in
function for our program. We should be used to seeing this convention since it’s
common in the popular industrial languages like C++ and Java.

Finally, we make a call to printf which is a special print function that allows
for string formatting. Of course, all we’re going to pass to it is the “Hello,
World!” string. And, that’s it!
