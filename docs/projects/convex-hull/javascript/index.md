---
authors:
- Griffin Annshual
- rzuckerm
date: 2023-11-01
featured-image: convex-hull-in-every-language.jpg
last-modified: 2025-05-04
layout: default
tags:
- convex-hull
- javascript
title: Convex Hull in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/javascript/how-to-implement-the-solution.md
- sources/programs/convex-hull/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
/**
 * Calculate the Convex Hull of a set of 2D points using Graham's Scan algorithm.
 *
 * @param {Array} points - An array of 2D points represented as objects with x and y properties.
 * @returns {Array} - An array of points on the convex hull in counter-clockwise order.
 */
function convexHull(points) {
	function orientation(p, q, r) {
		const val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
		if (val === 0) return 0;
		return val > 0 ? 1 : -1;
	}

	const n = points.length
	if (n < 3) return points;

	let minPointIndex = 0;
	for (let i = 0; i < n; i++) {
		if (
			(points[i].y < points[minPointIndex].y) ||
			(points[i].y == points[minPointIndex].y && points[i].x < points[minPointIndex].x)
		) {
			minPointIndex = i;
		}
	}
	const sortedPoints = [...points].sort((a, b) => {
		const angleA = Math.atan2(a.y - points[minPointIndex].y, a.x - points[minPointIndex].x);
		const angleB = Math.atan2(b.y - points[minPointIndex].y, b.x - points[minPointIndex].x);
		return angleA - angleB;
	})

	const convexHull = [sortedPoints[0], sortedPoints[1]];

	for (let i = 2; i < n; i++) {
		while (
			convexHull.length > 1 &&
			orientation(
				convexHull[convexHull.length - 2],
				convexHull[convexHull.length - 1],
				sortedPoints[i]
			) !== -1
		) {
			convexHull.pop();
		}
		convexHull.push(sortedPoints[i]);
	}

	return convexHull;
}

/**
 * Executable function for Convex Hull calculation with command-line input.
 *
 * @param {string} inputX - Comma-separated X coordinates as a string.
 * @param {string} inputY - Comma-separated Y coordinates as a string.
 */
function main(inputX, inputY) {
	if (inputX == undefined || inputY == undefined){
		inputX = " ";
		inputY = " ";
	}
	const xArray = inputX.split(",").map(Number);
	const yArray = inputY.split(",").map(Number);

	if (
		xArray.length < 3 ||
		yArray.length < 3 ||
		xArray.length !== yArray.length ||
		xArray.some(item => isNaN(item))|| yArray.some(item => isNaN(item))
	) {
		console.log(
			'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")'
		);
		return;
	}

	const points = xArray.map((x, i) => ({ x, y: yArray[i] }));

	const convexHullResult = convexHull(points);
	convexHullResult.forEach((point) => console.log(`(${point.x}, ${point.y})`));
}

// Run the executable function with command-line arguments
const inputX = process.argv[2];
const inputY = process.argv[3];
main(inputX, inputY);

```

{% endraw %}

Convex Hull in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Griffin Annshual
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).