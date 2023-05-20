---
title: File Input Output in Java
layout: default
date: 2019-10-13
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-13

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileInputOutput {

    public static void main(String[] args) {
        File file = new File("output.txt");
        writeToFile(file);
        readFile(file);
    }

    public static void readFile(File file) {

        try {

            BufferedReader buffer = new BufferedReader(new FileReader(file));
            try {
                String nextLine = buffer.readLine();
                while (nextLine != null) {
                    System.out.println(nextLine);
                    nextLine = buffer.readLine();
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
            writer.close();
        } catch (IOException e) {

            System.out.println("Error occurred while writing contents to file!");
        }

    }

}
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski
- Shubham Raj

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Oct 13 2019 19:02:32. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).