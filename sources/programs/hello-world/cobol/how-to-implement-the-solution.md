From it's very nature, COBOL is a very readable language.
But even though it's readable, it follows very strict rules.

The structure of a COBOL program follows like this:

- At the highest level are "Divisions".
- "Divisions" consist of "Sections".
- "Sections" consist of "Paragraphs".
- "Paragraphs" consist of "Sentences".
- "Sentences" consist of "Statements".
- "Statements" consist of "Characters".

We know that Python as language cares a lot about indentation but COBOL is even more particular about it.
A COBOL program is divided into columns. The Divisions must start from column 8 (Area A).
Paragraphs and Sentences should start from column 12 (Area B) which you can see is 1 tab or 4 spaces away from Area A.
This indentation is also a reason why COBOL is so readable.
Now that we have cleared some basics, let's start reading the Hello World program.

The `IDENTIFICATION DIVISION` is one of the 4 Divisions that we have and it is mandatory.
As the name suggests, it consists of information that identifies the program like the author name, date of creation, etc.
One mandatory information for program identification is, you guessed it, the `PROGRAM-ID` statement.
Here we are declaring the `PROGRAM-ID` as `HELLO-WORLD`.
As a side note, we should ideally keep the `PROGRAM-ID` same as the file name and only 8 characters long. But since we will be running this program on a Linux environment, it's fine.

Next we have the other mandatory Division, `PROCEDURE DIVISION`.
This contains all the Paragraphs and Sentences that do the actual work.
Here, the Sentence doing our work is `DISPLAY "Hello, World!"`.
`DISPLAY` is our Statement here and it does what it says it does.
Then, we have another Statement, which is a Sentence in itself, `STOP RUN`.
It stops the run and returns the control to either the calling program or the OS.
Also, you should end any part of the program with a period. It might be optional at some places but it is recommended.
That's it! Apart from the little nuances of indentation and program structure, it's a very readable program.
