---

title: File Io in Java
layout: default
date: 2022-04-28
last-modified: 2022-05-14

---

Welcome to the [File Io](https://sampleprograms.io/projects/file-io) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileIO {

	public static void main(String[] args) {

		// create a new file output.txt
		File file =new File("output.txt");

		//method to open a file and add contents
		writeToFile(file);
		//method to open the file and print its content line by line
		readFile(file);

	}

	public static void readFile(File file) {

		try {

			BufferedReader buffer=new BufferedReader(new FileReader(file));
			try {
				String nextLine=buffer.readLine();// read the file one line at a time
				while(nextLine!=null) {
					//display the line on the screen
					System.out.println(nextLine);
					nextLine=buffer.readLine(); // read the next line to print
				}
				buffer.close();
			} catch (IOException e) {

				System.out.println("Error occurred while reading the file");
			} 

		} catch (FileNotFoundException e) {

			System.out.println("Error occurred while opening the file!");
		}

	}

	public static void writeToFile(File file) {

		String content = "We wish you a Merry Christmas\n" + 
				"We wish you a Merry Christmas\n" + 
				"We wish you a Merry Christmas\n" + 
				"And a happy New Year.";
		try {
			FileWriter writer = new FileWriter(file);
			writer.write(content); 
			writer.close(); // closes the file
		} catch (IOException e) {

			System.out.println("Error occurred while writing contents to file!");
		}

	}

}
```

{% endraw %}

[File Io](https://sampleprograms.io/projects/file-io) in [Java](https://sampleprograms.io/languages/java) was written by:

- Shubham Raj
- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 18:07:28. The solution was first committed on Oct 13 2019 18:50:32. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).