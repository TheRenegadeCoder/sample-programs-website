---

title: Fizz Buzz in Tex
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Fizz Buzz in Tex page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Tex
%&pdftex

\countdef\counter=1
\countdef\threecounter=2
\countdef\fivecounter=3
\counter=1
\threecounter=1
\fivecounter=1

\loop
    \def\printnum{1}
    \noindent
    \ifnum \threecounter>2
        Fizz%
        \threecounter=0
        \def\printnum{0}
    \fi
    \ifnum \fivecounter>4
        Buzz%
        \fivecounter=0
        \def\printnum{0}
    \fi
    \ifnum\printnum=1
        % print the counter variable
        \the\counter%
    \fi
    \hfil \break
    \advance \counter 1
    \advance \threecounter 1
    \advance \fivecounter 1
\ifnum \counter<101
\repeat

\end

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.