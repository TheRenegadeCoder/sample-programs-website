---

title: Import/Export in JavaScript  
layout: default  
last-modified: 2020-11-01
featured-image:  
tags: [javascript, import-export]  
authors:  
  - ray6464
  - the_renegade_coder

---

Welcome to the Import Export in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
var myImport = require("./export");

console.log(myImport.myGreeting);
```

{% endraw %}

## How to Implement the Solution

Let's look at the code in detail:  

**export.js**:  

```javascript
exports.myGreeting = "Hello World";
```

**import.js**:  

```javascript
var myImport = require("./export");
console.log(myImport.myGreeting);
```

In the "export.js" file we have the "exports" object built into JavaScript (like document, or console). 
We give the "exports" object a property named "myGreeting" with the value "Hello World". When another 
file wants to import a value/variable, it can extract that variable from the properties of the 
"exports" object of this file.

In the "imports.js" file we have a variable named "myImport" which uses the "require" keyword to extract 
the exports object from another file (in this case the "export.js" file) and assign it to the variable 
"myImport". Then, we log the value of "myImport.myGreeting" which will be the same as the value 
of "exports.myGreeting" since "myImport" and "exports" is the same object now.


## How to Run the Solution

To run this code you need to run this file in NodeJS. To do that you need to install NodeJS and then use 
a terminal/cmd to move to the directory where you are keeping the "export.js" and "import.js" files, and 
execute the command "node import.js".
