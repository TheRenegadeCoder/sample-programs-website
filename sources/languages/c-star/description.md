This is not the C* language described in [Wikipedia][1]. According to its
creator, [Emil Laine][2] in [this GitHub issue][3], it is a new language.
From the [commit history][4], it looks like the language was created in 2017.
However, according to the [issue][3], they are no longer actively maintaining
this language. At the time of this writing, the last commit was done in May
2023.

According to the [C* documentation][5]:

> C* (pronounced “C star”) is a hybrid low-level / high-level programming language
  focused on runtime performance and developer productivity, in this order of priority.
  The language is simple and unopinionated, has a clean C-like syntax, and supports
  imperative, generic, data-oriented, functional, and object-oriented programming.

According to the [C* introduction][6], the C* language is intended to overcome the
short-comings of [C][7] and the complexity of [C++][8]. Unlike [Rust][9], it is intended
to be used in non-safety-critical applications, so it does not have the complex
lifetime and ownership model that Rust does. However, it has some memory safety
features like these:

- Array bounds checking
- Integer overflow checking
- Null checking

For further information on this language, see the [C* documentation][5].

[1]: https://en.wikipedia.org/wiki/C*
[2]: https://github.com/emlai
[3]: https://github.com/cx-language/cx/issues/77
[4]: https://github.com/cx-language/cx/commits/main
[5]: https://cx-language.github.io/
[6]: https://cx-language.github.io/introduction
[7]: https://en.wikipedia.org/wiki/C_(programming_language)
[8]: https://en.wikipedia.org/wiki/C%2B%2B
[9]: https://en.wikipedia.org/wiki/Rust_(programming_language)
