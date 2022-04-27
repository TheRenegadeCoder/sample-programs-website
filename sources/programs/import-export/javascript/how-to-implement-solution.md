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
