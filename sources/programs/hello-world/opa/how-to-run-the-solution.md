Typically at this point, we would cover a couple methods for running the solution.
For instance, we might share a link to an online editor. If that isn’t available,
sometimes we’ll even offer a way to run the solution locally on your PC. And,
you can do that with Opa, but we’ve opted instead to run Opa using Docker.

### But First, Lemme Explain Docker

To give a small overview of Docker and containers, imagine a virtual machine that
can boot up in less than a second, and the cost of provisioning, screwing up and
starting from scratch, is negligible. (Disclaimer: it’s totally not like that,
but let’s go with it.)

I absolutely despise installing stuff, using it once or twice, and then forgetting
about it. I rarely remember to uninstall such things, and you can never be too
sure that it hasn’t spread it’s 1kB-sized temp/config files all over. That’s why
I use containers.

Would you like to see what happens when you create a thousand random files
in / ? Or how the system screws up when deleting /var ? Or even try out a
fork-bomb (Disclaimer 2: It’s sorta dangerous in a container too)?

Well now you can! You can spin up a container with a fresh Ubuntu in it, toy
around with it, and have it deleted upon exit.

Containers are like VMs, except they share the kernel, network stack, and more,
with your own OS. They also can be constraint via cgroups (hard/soft CPU/memory
limits, and more). The root filesystem they use is mapped to folders in your
own machine, and whatever harm you do to them, does nothing on your system.

So, you can “easily” install Opa (or any other language/thing) in a container,
play around, stop it, and when you delete the container, your OS is still as
clean as before.

### How to Run Opa in Docker

Finally, we can actually dig into the execution of Hello World in Opa.

#### Image Setup

For my next trick, I built a Dockerfile. It contains the definition of all
which needs to be installed and set up in order to run Opa, on Ubuntu.

A Dockerfile is the definition/blueprint for an image, and an image is the
blueprint for a container. Applications run in containers.

This is mostly not reversible: While you can commit a container into an image,
you cannot extract the Dockerfile from an image.

So, if you want to build your own, local image, you can build it off the
Dockerfile, like so:

```console
~/devel/SPEPL/archive/o/opa master
❯ ls
Dockerfile hello-world.opa README.md
~/devel/SPEPL/archive/o/opa master
❯ docker build --tag opalang:1.1.1 .
Sending build context to Docker daemon 5.12kB
Step 1/6 : FROM ubuntu
---> 113a43faa138
[...]
Step 6/6 : RUN sudo npm install -g opabsl.opp intl-messageformat intl
---> Using cache
---> 626e6038445b
Successfully built 626e6038445b
Successfully tagged opalang:1.1.1
```

Now you have a working image. Congrats.

Docker has a “hub”, conveniently called Docker Hub, where users can upload
their public images for others to use. So, instead of building your own image,
you could have just used mine:

```console
~/devel/SPEPL/archive/o/opa master
❯ docker pull nicovillanueva/opalang:1.1.1
Using tag: 1.1.1
1.1.1: Pulling from nicovillanueva/opalang
[...]
Digest: sha256:7043076348bf5040220df6ad703798fd8593a0918d06d3ce30c6c93be117e430
Status: Downloaded newer image for nicovillanueva/opalang:1.1.1
```

So, finally, we can run hello-world.opa

#### How to Run it for Real This Time

Having the .opa file in the current directory, run: `docker run -it --rm --volume $PWD:/data/ nicovillanueva/opalang:1.1.1 opa /data/hello-world.opa`

```console
~/devel/SPEPL/archive/o/opa master 31s
❯ ls
Dockerfile  hello-world.opa  README.md
~/devel/SPEPL/archive/o/opa master
❯ docker run -it --rm --volume $PWD:/data/ nicovillanueva/opalang:1.1.1 opa /data/hello-world.opa
~/devel/SPEPL/archive/o/opa master*
❯ ls
Dockerfile  hello-world.js  hello-world.opa  package.json  README.md
```

What we just did was run my image (if you want to use your own, replace
“nicovillanueva/opalang:1.1.1” for what your provided as --tag in your docker build),
mapping the current directory ($PWD) to /data inside the container.

This allows the Opa container to pick up the .opa file and compile it, inside
the container. It gave no output, but notice that there’s a new hello-world.js

As this .js has some npm dependencies, we can also run it inside a container,
using the same image:

```console
~/devel/SPEPL/archive/o/opa master* 15m 22s
❯ docker run -it --rm -v $PWD:/data/ --publish 8080:8080 nicovillanueva/opalang:1.1.1 sh -c '/data/hello-world.js'
┌───────────────────────────────────────────────────────────┐
│                  npm update check failed                  │
│            Try running with sudo or get access            │
│           to the local update config store via            │
│ sudo chown -R $USER:$(id -gn $USER) /home/opauser/.config │
└───────────────────────────────────────────────────────────┘
Http serving on http://e9aa732ccc83:8080
```

Now we also --published the 8080 port. This maps your own 8080 port, to the
container’s 8080. Having this up, if you fire up your browser and navigate
to http://localhost:8080, you’ll see “Hello, World!”, printed using Opa.
