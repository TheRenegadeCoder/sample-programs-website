---
title: Fizz Buzz in Lolcode
layout: default
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-01

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lolcode](https://sampleprograms.io/languages/lolcode) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lolcode
HAI 1.2

IM IN YR loop UPPIN YR var TIL BOTH SAEM var AN 101

    DIFFRINT 0 AN var
    O RLY?
      YA RLY
        I HAS A by3 ITZ BOTH SAEM 0 AN MOD OF var AN 3
        I HAS A by5 ITZ BOTH SAEM 0 AN MOD OF var AN 5
        
        BOTH OF by3 AN by5 
        O RLY?
          YA RLY
            VISIBLE "FizzBuzz"
          NO WAI
            by3
            O RLY?
              YA RLY
                VISIBLE "Fizz"
              NO WAI
                by5
                O RLY?
                  YA RLY
                    VISIBLE "Buzz"
                  NO WAI
                    VISIBLE var
                OIC
            OIC
        OIC
    OIC
    
IM OUTTA YR loop
KTHXBYE
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lolcode](https://sampleprograms.io/languages/lolcode) was written by:

- sayashraaj

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).