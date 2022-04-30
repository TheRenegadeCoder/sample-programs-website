---

title: File Io in Dg
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the File Io in Dg page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Dg
import '/os'

write_file = filename s ->
    except
        err =>
            open filename 'w' |>.write <| s
        err :: OSError =>
            print "Cannot open file" filename

read_file = filename ->
    except
        err =>
            with fd = open filename 'r' =>
                print $ fd.read!
        err :: OSError =>
            print "Cannot open file" filename


filename = "output.txt"
write_file filename "Example text"
read_file filename
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).