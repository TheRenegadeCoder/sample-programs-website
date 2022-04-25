To satisfy the requirements, a program must accept a string on the command line 
and return the length of the longest word in the string:

```shell
$ ./longest-word-in-string.lang "Google do a barrel roll"
$ 6
```

In this case, we have a string with 5 words. It appears that there are two words
that share the largest number of characters: Google and barrel. Naturally, we
don't care to decide between the two words. Instead, we return the length of them 
both: 6.
