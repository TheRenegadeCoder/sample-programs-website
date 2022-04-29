---

title: Rot 13 in Java
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Rot 13 in Java page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Java
public class Rot13
{
   public static void main(String[] args)
   {
      if(args.length<1) {
         System.out.println("Usage: please provide a string to encrypt");
      }
      else {
         String code = args[0];
         String result = "";
         if(code.length()==0) {
            System.out.println("Usage: please provide a string to encrypt");
         }
         else {
            String lower = "abcdefghijklmnopqrstuvwxyz";
            String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            for(int a=0; a<code.length(); a++) {
               String ch = code.substring(a,a+1);
               int l = lower.indexOf(ch);
               int u = upper.indexOf(ch);
               if(l!=-1) {
                  result+=lower.substring( (l+13)%26,(l+14)%26!=0 ? (l+14)%26 : l+14 );
               }
               else if(u!=-1) {
                  result+=upper.substring( (u+13)%26,(u+14)%26!=0 ? (u+14)%26 : u+14 );
               }
               else {
                  result+=ch;
               }
            }
            System.out.println(result);
         }
      }
   }
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.