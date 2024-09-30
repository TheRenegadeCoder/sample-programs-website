---
authors:
- rzuckerm
date: 2024-02-02
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2024-02-02
layout: default
tags:
- beef
- sleep-sort
title: Sleep Sort in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/beef/how-to-implement-the-solution.md
- sources/programs/sleep-sort/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;
using System.Threading;

namespace SleepSort;

class Program
{
    public static void Usage()
    {
        Console.WriteLine(
            """
            Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
            """
        );
        Environment.Exit(0);
    }

    public static Result<T> ParseInt<T>(StringView str)
    where T : IParseable<T>
    {
        StringView trimmedStr = scope String(str);
        trimmedStr.Trim();

        // T.Parse ignores single quotes since they are treat as digit separators -- e.g. 1'000
        if (trimmedStr.Contains('\''))
        {
            return .Err;
        }

        return T.Parse(trimmedStr);
    }

    public static Result<void> ParseIntList<T>(StringView str, List<T> arr)
    where T: IParseable<T>
    {
        arr.Clear();
        for (StringView item in str.Split(','))
        {
            switch (ParseInt<T>(item))
            {
                case .Ok(let val):
                    arr.Add(val);

                case .Err:
                    return .Err;
            }
        }

        return .Ok;
    }

    public static void SleepSort(List<int32> arr)
    {
        // Initialize temporary array to hold sleep values
        List<int32> tempArr = scope .();

        // Create and start threads
        Monitor monitor = scope .();
        List<Thread> threads = scope .();
        for (int32 sleepVal in arr)
        {
            Thread thread = new .(new [=sleepVal, &tempArr, &monitor] () => {
                Thread.Sleep(sleepVal * 1000);
                using (monitor.Enter())
                {
                    tempArr.Add(sleepVal);
                }
            });
            threads.Add(thread);
            thread.Start(false);
        }

        // Wait for threads to complete
        for (Thread thread in threads)
        {
            thread.Join();
            delete thread;
        }

        // Copy temporary array to array to sort
        arr.Clear();
        tempArr.CopyTo(arr);
    }

    public static void ShowList<T>(List<T> arr)
    {
        String line = scope .();
        for (T val in arr)
        {
            if (!line.IsEmpty)
            {
                line += ", ";
            }

            line.AppendF("{}", val);
        }

        Console.WriteLine(line);
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1)
        {
            Usage();
        }

        List<int32> arr = scope .();
        switch (ParseIntList<int32>(args[0], arr))
        {
            case .Ok:
                if (arr.Count < 2)
                {
                    Usage();
                }
            case .Err:
                Usage();
        }

        SleepSort(arr);
        ShowList<int32>(arr);
        return 0;
    }
}

```

{% endraw %}

Sleep Sort in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).