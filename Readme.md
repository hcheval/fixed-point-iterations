A framework for implementing fixed point iterations in $W$-hyperbolic spaces.

A $W$-hyperbolic space is a metric space $(X, d)$ endowed with a convexity mapping $W : X \times X \times [0, 1] \to X$,
where $W(x, y, \lambda)$ is intended to abstractly represent a convex combination of the points 
$x$ and $y$ of parameter $\lambda$. 
For a structure $(X, d, W)$ to be called a $W$-hyperbolic space, it it is required to furthermore satisfy a number of axioms, which are not relevant to this implementation.

In this project, one defines a $W$-hyperbolic space by choosing a type $X$, representing the points in the space, an appropriate distance function, and an appropriate convexity mapping, defined on $X$.
Examples of such spaces defined in this project are:
- $\bb{R}$ for different norms (the ones given by numpy) 
- $\mathcal{l}^p$ spaces 
- $L^p([a, b])$ spaces

The fixed point iterations implemented as examples are:
- The Halpern iteration
- The Tikhonov-Mann iteration 

In order to define a new iteration, one should extend the `Iteration` class 
