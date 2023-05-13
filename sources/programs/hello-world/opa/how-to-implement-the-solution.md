As we mentioned, Opa code contains both front-end and server-side code.

Notice how we define a function that returns raw HTML (a la JSX) and also set
up the server, all in the same file. The `Server.start` would be analogous to a
`main()` function. In this case, it's parameters take the server's settings
(default http server in this case) and a component to render.

Also, we do not define imports of any kind. Everything is picked up off the
standard library.
