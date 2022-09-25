---

title: Factorial in D
layout: default
date: 2022-04-28
last-modified: 2022-09-25

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [D](https://sampleprograms.io/languages/d) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```d
// Factorial program in D


import std.stdio: writeln;
import std.getopt;
int fac(int a)
{
  if (a <= 1)
    {
      return 1;
    }
  return a*fac(a-1);
}
int main(string[] args)
{
  int depth;
  auto params = getopt(args, "depth", &depth);
  int result = fac(depth);
  writeln(result);
  return 0;
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [D](https://sampleprograms.io/languages/d) was written by:

- Scott Little

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).