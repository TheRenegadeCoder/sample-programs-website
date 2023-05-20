---
title: The Opa Programming Language
layout: default
last-modified: 2020-05-02
tags: [opa]
authors:
  - nicovillanueva

---

Welcome to the Opa page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

[Opa][1] is sadly a short-lived language, created in 2011 by the company [MLState][2].
It's strongly focused on webapps, as it lets you write server-side and client-side
code, side by side. The client-code is compiled into [JavaScript][3], and the server-code,
into [Node.js][4]. All using strong, static typing. Pretty nifty.

In version 0.9.0, it natively supported [MongoDB][5], as if it had an [ORM][6] built in.
In 1.1.0, this support was extended to [PostgreSQL][7] too.

It reminds me a bit of [React/JSX][9], as it's wholeheartedly designed for interoperability
with HTML. It's actually a first-class citizen. Blurring the line between client
and server code is something that I'm really fond of.

The problem is that, having had only 2 years of activity, the "user experience"
is really bad. Setting up the environment is... problematic, to say the least. It
requires installing [Node.js][4] and [OCaml][9], with dependencies of each one sprinkled in.
Which in turn need dependencies. Some of which have to be compiled from source.
In a time where installing a language (or anything really) should not take more
than 2 or 3 commands (`apt update && apt install -y Stuff-0.1.1-dev`), this was a
paaaain!!

Luckily, there's this cute technology called containers.

[1]: https://en.wikipedia.org/wiki/Opa_(programming_language)
[2]: https://www.crunchbase.com/organization/mlstate
[3]: https://en.wikipedia.org/wiki/JavaScript
[4]: https://en.wikipedia.org/wiki/Node.js
[5]: https://en.wikipedia.org/wiki/MongoDB
[6]: https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping
[7]: https://en.wikipedia.org/wiki/PostgreSQL
[8]: https://legacy.reactjs.org/docs/introducing-jsx.html
[9]: https://en.wikipedia.org/wiki/OCaml


## Articles

- [Hello World in Opa](https://sampleprograms.io/projects/hello-world/opa)