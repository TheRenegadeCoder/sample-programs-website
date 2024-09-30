---
authors:
- rzuckerm
date: 2024-02-18
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2024-02-18
layout: default
tags:
- beef
- transpose-matrix
title: Transpose Matrix in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/beef/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;

namespace TransposeMatrix;

class Matrix<T>
{
    int mRows;
    int mCols;
    T[,] mMatrix ~ delete _;

    public this(int rows, int cols, List<T> arr)
    {
        mRows = rows;
        mCols = cols;
        mMatrix = new T[mRows, mCols];
        int index = 0;
        for (int i < mRows)
        {
            for (int j < mCols)
            {
                mMatrix[i, j] = arr[index];
                index++;
            }
        }
    }

    public void ShowMatrixAsList()
    {
        String line = scope .();
        for (int i < mRows)
        {
            for (int j < mCols)
            {
                if (!line.IsEmpty)
                {
                    line += ", ";
                }

                line.AppendF("{}", mMatrix[i, j]);
            }
        }

        Console.WriteLine(line);
    }

    public void Transpose()
    {
        T[,] matrixT = new T[mCols, mRows];
        for (int i < mRows)
        {
            for (int j < mCols)
            {
                matrixT[j, i] = mMatrix[i, j];
            }
        }

        Swap!(mRows, mCols);
        delete mMatrix;
        mMatrix = matrixT;
    }
}

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please enter the dimension of the matrix and the serialized matrix");
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

    public static int Main(String[] args)
    {
        if (args.Count < 3)
        {
            Usage();
        }

        int cols = ?;
        switch (ParseInt<int>(args[0]))
        {
            case .Ok(out cols):
                if (cols < 1)
                {
                    Usage();
                }

            case .Err:
                Usage();
        }

        int rows = ?;
        switch (ParseInt<int>(args[1]))
        {
            case .Ok(out rows):
                if (rows < 1)
                {
                    Usage();
                }

            case .Err:
                Usage();
        }

        List<int32> arr = scope .();
        if (ParseIntList<int32>(args[2], arr) case .Err)
        {
            Usage();
        }

        if (rows * cols != arr.Count)
        {
            Usage();
        }

        Matrix<int32> matrix = scope .(rows, cols, arr);
        matrix.Transpose();
        matrix.ShowMatrixAsList();
        return 0;
    }
}

```

{% endraw %}

Transpose Matrix in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).