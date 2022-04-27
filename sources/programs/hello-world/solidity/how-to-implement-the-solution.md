Without further ado, here’s an implementation of Hello World in Solidity:

```solidity
pragma solidity ^0.4.22;
contract helloWorld {   
    function renderHelloWorld () public pure returns (string) {       
        return 'Hello, World!';             
    }
}
```

While the format of Solidity looks a bit different from the more popular
programming languages today, what’s happening behind is fairly straightforward.

First we import the version of Solidity we’d like to use. Then we create a
function and specify we’d only like to return a string. And, voila!
