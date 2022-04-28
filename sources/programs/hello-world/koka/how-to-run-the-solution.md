If you want to run Koka at your local machine, you can always install the Koka
compiler and try the snippet locally. There are no binary releases of Koka though.
You will have to build the compiler yourself. Don't worry! It sounds harder than
it is. All you need to do is install the following programs:

- The [Haskell platform][2] (version 7.4 or later)
- The [NodeJS runtime][3] (version 4.2 LTS or later)
- [Git][4] for version control

Now, you need to [clone the Koka repository][5] to your local environment. Then,
run the following commands at the local repo directory:

```console
npm install
cabal update
cabal install alex
jake
```

jake is the command for building the compiler, and it also runs the Koka
interactive environment where you can play around with Koka.

To actually run the solution, you need to run the following commands:

```console
:l YOUR_FILE.kk
main()
```

There you go! The sky is the limit now. But if you need help, you can check out
the [Koka book][6] and [the documentation][7].
