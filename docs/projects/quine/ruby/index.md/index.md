# Quine in Ruby

## Solution

```Ruby
s="s=%c%s%c; printf s,34,s,34,10%c"; printf s,34,s,34,10

```