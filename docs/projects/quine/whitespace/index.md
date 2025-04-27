---
authors:
- rzuckerm
date: 2025-04-16
featured-image: quine-in-whitespace.jpg
last-modified: 2025-04-27
layout: default
tags:
- quine
- whitespace
title: Quine in Whitespace
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/whitespace/how-to-implement-the-solution.md
- sources/programs/quine/whitespace/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Whitespace](https://sampleprograms.io/languages/whitespace) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```whitespace
   		  	 				  	    		 		 		  	  			   		 			   	 			 		  		 	  					 				   		 		 			 		   	  					 	 		  	 			      	     		   			 	       	   				  	  		   	    		 		     		 		 						    	  	 		    	 	   	  	 	 	  				 	 	 			   	 	    	    				 			 			      		 	  	  	     	  	 	 	 		    		 	 		 		    		 	 		  	 						 	    	 	  		  		  		 		 				 				 	  	   	 	 	  			 		    	 			  		  	 	    	 	  	 	 	  		 	 
    
   	     
		    	
   	  	
		    	 
   	 	 
		    	     
 
  
 	
  	
  	
     	

   
 
 	    
  	  	 
	  	
		 

  	
   	 
	 	  
 
	   
 	  	
 	  	
	 	    	 
	 						
  
 
	

    
 

   	 	 
	
  
   	
 
    		
	 						
     		
	 	  
 
	 		

 
 	

  		
 





```

{% endraw %}

Quine in [Whitespace](https://sampleprograms.io/languages/whitespace) was written by:

- rzuckerm

This article was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

The code listed in the "Current Solution" section looks like a polar bear in a
blizzard! In other words, it is nothing but whitespace characters. The reason
is two-fold:

1. In Whitespace, the only characters that contain instructions are whitespace
   characters. Everything else is ignored.
2. While it is possible to write a program that generates comments or other
   annotation, it would require a lot more code to do so. It is easier to just
   generate the whitespace characters that represent the code.

At the highest level, the code consists of the following:

- Push P (an integer value that represents the rest of the code) onto the
  stack.
- The rest of the code (for brevity, let's call this R).

The value of P is calculated by representing each whitespace character in
R as a base-3 number, least-significant value first, where:

- 0 = space
- 1 = tab
- 2 = linefeed

In other words:

- P = 3<sup>0</sup>r<sub>1</sub> + 3<sup>1</sup>r<sub>2</sub> + 3<sup>2</sup>r<sub>3</sub> + ... + 3<sup>T-1</sup>r<sub>T</sub>

where:

- T is the number of values in R.
- r<sub>i</sub> is the ith value of R.

P is a very large number: 125 base-10 digits!

So how does this approach generate an output that is identical to the actual
program file? The idea is based on a [description in RosettaCode][1] (the code
is not present since it looks like RosettaCode trims whitespace, and the code
is all whitespace). Let's break it down. The rest of the code, R, does this:

- Output the `Push` instruction as whitespace characters.
- Output P as whitespace characters.

The `Push` instruction consists of the following:

- The `Push` opcode: space, space
- The sign bit of P (0 for positive): space
- The value of P in base-2, most-significant bit first: space for 0, tab
  for 1
- The terminator for the `Push` instruction: newline

Outputting the `Push` instruction consists of the following:

- Output 3 spaces for the opcode and sign bit.
- Output the value of P as whitespace characters.
- Output linefeed.

In order to easily translate integers into whitespace characters, memory
(`mem`) is set up as follows:

- mem\[0\] = space
- mem\[1\] = tab
- mem\[2\] = linefeed

Outputting the value of P as whitespace characters is done like this:

- Find D = 2<sup>K</sup> such that D is greater than or equal to P:
  ```
  D = 1
  Do
    D = D * 2
  While D < P
  ```
- Output P in base-2, most-significant bit first, translated to whitespace
  characters:
  ```
  While (D = D // 2) != 0
    N = P // D
    Output mem[N % 2]
  End While
  ```
  where `//` means integer division, and `%` means modulo.

Outputting the rest of the program as whitespace characters consists of this:

- Output P in base-3, least-significant value first, translated to whitespace
  characters:
  ```
  While P != 0
    Output mem[P % 3]
    P = P // 3
  End While
  ```

To balance out the stack and end the program, there is a `Pop` instruction and
an `End` instruction that tells the Whitespace interpreter to end the program,
but those are already accounted for in the value of P.

To see this all together, take a look at the [Whitespace Assembly Code][2]
that was used to generate this sample. The Whitespace Assembly Language was
converted to whitespace characters using the [Whitespace Assembler][3]. This
sample is the output of the Assembler.

[1]: https://rosettacode.org/wiki/Quine#Whitespace
[2]: https://github.com/rzuckerm/whitespace-quine/blob/main/quine.ws.asm
[3]: https://pypi.org/project/whitespace-asm/


## How to Run the Solution

To run this program:

- Download a copy of [Quine in Whitespace][4].
- Browse to the [Try It Online Whitespace Interpreter][5].
- Open the code in an editor, select all, and copy the code to the clipboard.
- Paste it into the `Code` section in the browser window. The size of the code
  should be 679 bytes. If it is less, scroll all the way to the bottom and
  press Enter.
- Press the "Play" button at the top of the browser window to run the code.
- The `Output` section at the bottom should be identical to the original code.

[4]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/w/whitespace/quine.ws
[5]: https://tio.run/#whitespace
