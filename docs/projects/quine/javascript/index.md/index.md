# Quine in Javascript

## Solution

```Javascript
(function(){console.log('('+arguments.callee.toString()+')()')})()

```