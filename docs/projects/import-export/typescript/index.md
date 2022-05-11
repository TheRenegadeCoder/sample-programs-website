---

title: Import/Export in TypeScript  
layout: default  
last-modified: 2020-11-01
featured-image:  
tags: [typescript, import-export]  
authors:  
  - ray6464
  - the_renegade_coder

---

Welcome to the Import Export in Typescript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
import { myGreeting } from "./export";

console.log(myGreeting);
```

{% endraw %}

Import Export in Typescript was written by:

- Anna

## How to Implement the Solution

Let's look at the code in detail:  

code for export.ts:-  

```tyepscript
export const myGreeting = "Hello World";
```

code for import.ts:-  

```typescript
import { myGreeting } from "./export";
console.log(myGreeting);
```

In the "export.ts" file we have use the "export" keyword to export the constant "myGreeting" to other importing files.

In the "imports.ts" file we have used the "import" keyword to import the "myGreeting" value from the file "export.js".

Notice here that we need to know the name of the exported variable to import it, and we need to add the "./" prefix 
for exporting files placed in the same directory as the importing file.

Then we simply logged "myGreeting" to the console.


JavaScript Keywords used in this code:  
1. export  
2. const  
3. import  
4. from  
5. console    


## How to Run the Solution

First you need to install TypeScript then verify installation with "tsc -v". Then use the command "tsc export.ts import.ts" 
to compile TypeScript code to JavaScript. After compiling you will have two more files in this directory named "export.js" 
and "import.js".

Then To run this code you need to run this file in NodeJS. To do that you need to install NodeJS and then use a terminal/cmd 
to move to the directory where you are keeping the "export.js" and "import.js" files, and execute the command "node import.js".
