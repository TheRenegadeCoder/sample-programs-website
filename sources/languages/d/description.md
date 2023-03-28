If you haven't heard of [D][1], I'm hardly surprised. After all, it's 
not exactly a popular language. In fact, it currently ranks 39th by 
popularity on GitHub. For reference, languages ahead of D include 
[Visual Basic .NET][2] (31st), [Haskell][3] (21st), [Swift][4] (18th), and [C][5] (8th). 
Meanwhile, D sits narrowly ahead of newer languages like [Julia][6] (43rd) 
and [Elixir][7] (45th).

That said, according to [Wikipedia][1], D is still a pretty interesting 
language. As you can probably imagine, D is supposed to be an 
improvement on C++. Apparently, the designers weren't a fan of the 
practical issues surrounding C++ (surprise, surprise!). As a result, 
D includes features like design by contract, garbage collection, 
associative arrays, array slicing, and lazy evaluation.

Perhaps the most interesting feature to me has to be the inline 
assembler. Apparently, developers can write assembly code directly 
in D source code:

```d
void *pc;
asm
{
    pop  EBX         ;
    mov  pc[EBP], EBX ; 
}
```

By adding an asm block, developers can quickly tap into the hardware 
with assembly code. Now, I think that is a pretty cool programming 
language feature.

[1]: https://en.wikipedia.org/wiki/D_(programming_language)
[2]: https://en.wikipedia.org/wiki/Visual_Basic_(.NET)
[3]: https://en.wikipedia.org/wiki/Haskell
[4]: https://en.wikipedia.org/wiki/Swift_(programming_language)
[5]: https://en.wikipedia.org/wiki/C_(programming_language)
[6]: https://en.wikipedia.org/wiki/Julia_(programming_language)
[7]: https://en.wikipedia.org/wiki/Elixir_(programming_language)
