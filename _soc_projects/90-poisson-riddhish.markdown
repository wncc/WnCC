---
layout: soc-project
image: /images/poisson.png
title: Poisson Solver with Image Editing
mentor: "Riddhish Bhalodia"
category: Scientific Computation
weight: 70
ribbon: completed
mentees:
- Dhruv Ilesh Shah
---

This notebook will be written using python, also employing numpy and OpenCV, we will initially implement Poisson solver for the discrete case which is immensely useful for many application then we will proceed on the application part which will be from <a href="https://www.cs.jhu.edu/~misha/Fall07/Papers/Perez03.pdf">this paper</a>

<!--break-->

### Week 0
 *  Read the concerned paper and discuss about implementation.
 *  Familiarize with simple optimization problems and how they are treated in the discrete domain.
 *  Familiarize with Image handling in Python (OpenCV or PIL)

### Week 1
 *  Design discretized algorithm for Laplace solver, with no Gradient field.
 *  Work out a method for obtaining a mask - manually/on click.
 *  Get good images to work upon and implement the mask.
 *  Implement the Laplacian Solver on an image with random regions highlihgted. Worked Fine.
 *  Temporary usage of `gimp` for creating mask, at the same time as naive cloning.
 *  First real implementation of the Poisson Solver, complete with guidance field and real mask. (Geometric implementation)

### Week 2
 *  Vectorize the search step of algorithm: Speed goes 3x.
 *  Attempt to approach the problem by the *Algebraic Method*, which can accomplish the task in under 5 seconds, employing sparse matrices.
 *  Futile efforts. Implementation on python might not work due to underlying design of sparse matrices (easily done on MATLAB).
 * 	Start off with the notebook by explaining the math and the implementation of the algorithm in the block-wise manner.

The notebook has been completed and this project has been completed in just over two weeks. Follow this <a href="https://github.com/riddhishb/ipython-notebooks/blob/master/Poisson%20Editing/README.md">readme</a> to run the notebook on your system, or check out the rendered notebook on the official <a href="https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks#signal-and-sound-processing">iPython Wiki</a>.
