---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- depth-first-search
- visual-basic
title: Depth First Search in Visual Basic
title1: Depth First Search
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/visual-basic/how-to-implement-the-solution.md
- sources/programs/depth-first-search/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Class Node

    Public ReadOnly Property Id As Integer

    Private ReadOnly _childrenSet As New HashSet(Of Integer)
    Private ReadOnly _children As New List(Of Integer)

    Public ReadOnly Property Children As IReadOnlyList(Of Integer)
        Get
            Return _children
        End Get
    End Property

    Public Sub New(id As Integer)
        Me.Id = id
    End Sub

    Public Sub AddChild(childId As Integer)
        If _childrenSet.Add(childId) Then
            _children.Add(childId)
        End If
    End Sub

End Class

Public Class Tree

    Private ReadOnly _nodes As New Dictionary(Of Integer, Node)

    Public ReadOnly Property RootId As Integer

    Public Sub New(rootId As Integer)
        Me.RootId = rootId
    End Sub

    Public Sub AddNode(node As Node)
        _nodes(node.Id) = node
    End Sub

    Public Function TryGetNode(id As Integer, ByRef node As Node) As Boolean
        Return _nodes.TryGetValue(id, node)
    End Function

    Public ReadOnly Property Nodes As IReadOnlyCollection(Of Node)
        Get
            Return _nodes.Values
        End Get
    End Property

End Class

Public Module DepthFirstSearch

    Private Sub ShowUsage()
        Console.Error.WriteLine(
            "Usage: please provide a tree in an adjacency matrix form " &
            "(""0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"") " &
            "together with a list of vertex values (""1, 3, 5, 2, 4"") and the integer to find (""4"")"
        )
    End Sub


    Public Function ParseIntegerList(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            Throw New ArgumentException("Input string is null or whitespace")
        End If

        Dim parts = input.Split(","c, StringSplitOptions.RemoveEmptyEntries Or StringSplitOptions.TrimEntries)
        Dim list As New List(Of Integer)(parts.Length)

        For Each part In parts

            Dim value As Integer
            If Not Integer.TryParse(part, value) Then
                Throw New ArgumentException($"Invalid integer value: '{part}'")
            End If

            list.Add(value)

        Next

        If list.Count < 1 Then
            Throw New ArgumentException("List must contain at least one integer")
        End If

        Return list

    End Function


    Public Function CreateTree(matrix As List(Of Integer),
                              vertices As List(Of Integer)) As Tree

        Dim n = vertices.Count

        If matrix.Count <> n * n Then
            Throw New ArgumentException("Adjacency matrix size does not match vertex count squared")
        End If

        Dim tree As New Tree(vertices(0))

        For Each v In vertices
            tree.AddNode(New Node(v))
        Next

        For row = 0 To n - 1

            Dim node As Node = Nothing
            If Not tree.TryGetNode(vertices(row), node) Then
                Throw New ArgumentException("Missing node")
            End If

            Dim baseIndex = row * n

            For col = 0 To n - 1

                If matrix(baseIndex + col) <> 0 Then
                    node.AddChild(vertices(col))
                End If

            Next

        Next

        Return tree

    End Function


    Public Function DFS(tree As Tree, target As Integer) As Boolean

        Dim visited As New HashSet(Of Integer)
        Dim stack As New Stack(Of Integer)

        stack.Push(tree.RootId)

        While stack.Count > 0

            Dim current = stack.Pop()

            If Not visited.Add(current) Then
                Continue While
            End If

            If current = target Then
                Return True
            End If

            Dim node As Node = Nothing
            If tree.TryGetNode(current, node) Then
                For Each child In node.Children
                    stack.Push(child)
                Next
            End If

        End While

        Return False

    End Function


    Public Function Main(args As String()) As Integer

        If args.Length <> 3 Then
            ShowUsage()
            Return 1
        End If

        Try

            Dim matrix = ParseIntegerList(args(0))
            Dim vertices = ParseIntegerList(args(1))

            Dim target As Integer
            If Not Integer.TryParse(args(2), target) Then
                ShowUsage()
                Return 1
            End If

            Dim tree = CreateTree(matrix, vertices)
            Dim found = DFS(tree, target)

            Console.WriteLine(found.ToString().ToLowerInvariant())
            Return 0

        Catch
            ShowUsage()
            Return 1
        End Try

    End Function

End Module
```

{% endraw %}

Depth First Search in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).