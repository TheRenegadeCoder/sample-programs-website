---

title: File Io in Perl
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the File Io in Perl page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```perl
#!/usr/bin/env perl

sub Main {
	Write("Some arbitrary data.");
	Read();
	exit(0);
}

sub Write {
	open(my $writing, ">output.txt") || die "File could not be written.\nError: $!";

	print $writing "@_"."\n";

	close($writing) || die "The file could not be closed on write.\nError: $!";
}

sub Read {
	open(my $reading, "<output.txt") || die "File could not be readed.\nError: $!";

	while (!eof($reading)) {
		print <$reading>;
	}

	close($reading) || die "The file could not be closed on reading.\nError: $!";
}

Main();
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).