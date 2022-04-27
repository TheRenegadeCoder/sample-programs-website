# Quine in Dg

## Solution

```Dg
s = 's = %r\nprint $ s%%s'
print $ s%s

```