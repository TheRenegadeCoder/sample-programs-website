# Fizz Buzz in Tex

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.