---

title: Dijkstra in Javascript
layout: default
date: 2022-04-28
last-modified: 2023-03-19

---

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function main() {

    const mat = process.argv[2];
    const src = parseInt(process.argv[3]);
    const des = parseInt(process.argv[4]);

    usage = "Usage: please provide three inputs: a serialized matrix, a source node and a destination node"

    if (isNaN(des) || isNaN(src) || !mat) {
        return console.log(usage);
    }

    const matList = mat.split(", ");
    const len = matList.length;
    const n = Math.sqrt(len); 

    // Non-Square Input
    if (n * n != len) {
        return console.log(usage);
    }

    // The Source or The Destination < 0
    if (src < 0 || des < 0) {
        return console.log(usage);
    }

    // Weight < 0
    if (matList.some(weight => weight < 0)) {
        return console.log(usage);
    } 

    // The Source or The Destination > SquareRootOfMatrix - 1
    if (src > n - 1 || des > n - 1) {
        return console.log(usage);
    }

    const mapping = [];
    while (matList.length) {
        mapping.push(matList.splice(0, n).map((i) => parseInt(i)));
    }

    const dijkstra = (src, des, n) => {
        // Create a priority queue to store nodes that
        // are being preprocessed.
        const q = [];

        // Create an array for distances and initialize all
        // distances as infinite (Infinity)
        const dist = new Array(n).fill(Infinity);

        // Insert source itself in priority queue and initialize
        // its distance as 0.
        // A node is a tuple with [id, cost]
        q.push([src, 0]);
        dist[src] = 0;

        while (q.length) {
            let cur = q[0];
            q.shift();
            let u = cur[0];
            let cost = cur[1];

            // Get all adjacent of u.
            for (let i = 0; i < n; i++) {
                let v = mapping[u][i];
                if (v == 0) continue;

                // If there is shorter path to v through u.
                if (cost + v < dist[i]) {
                    // Updating distance of v
                    dist[i] = cost + v;
                    q.push([i, dist[i]]);
                }
            }
        }
        return dist[des];
    };

    console.log(dijkstra(src, des, n));
}

main()
```

{% endraw %}

[Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- Matteo Planchet

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 14 2022 21:04:26. The solution was first committed on Oct 25 2021 16:28:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).