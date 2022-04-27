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
