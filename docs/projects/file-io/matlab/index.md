---

title: File Io in Matlab
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the File Io in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Matlab
path = "output.txt";

% Write content to file
file = fopen(path,'w');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return
end
fprintf(file, "Hello, World!\n");
fclose(file);

% Read content from file
file = fopen(path,'r');
if file == -1
    fprintf(strcat(path, " does not exist\n"));
    return
end
a = fscanf(file,'%s');
fprintf(a)



```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.