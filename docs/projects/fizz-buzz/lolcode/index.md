---

title: Fizz Buzz in Lolcode
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fizz Buzz in Lolcode page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lolcode
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).