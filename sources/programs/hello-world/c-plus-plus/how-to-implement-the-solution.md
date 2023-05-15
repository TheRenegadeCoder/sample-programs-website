Even though C++ was built on C, the implementation of Hello World in 
C++ is slightly different.

It appears this implementation of Hello World may be competing with 
Java for hardest to learn. But at any rate, let's break it down.

Once again, the first line is an `include` statement. Here, we're including 
the IO stream code in our solution. This is how we gain access to the 
IO objects like `cout`.

Next, we gain access to the `std` namespace which basically allows us to 
shorten `std::cout` to `cout`. It's really just a style thing that eliminates 
a lot of verbosity that you might get with other languages like Java. 
Of course, if another namespace also has a `cout`, we'll run into problems.

After that, we make a `main` method as usual. This is exactly the same as 
C, so I won't bother explaining the return type bit again.

Finally, we write our string to the `cout` stream. The syntax is a bit 
strange, but basically we can imagine that the Hello World string is 
inserted into the `cout` stream. In fact, the double-arrow operator is 
the insertion operator, and it has some fun properties. For instance, 
the operator can be chained together, but that's a topic for another time.
