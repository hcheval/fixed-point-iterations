A framework for implementing, simulating and visualizing fixed point iterations in $W$-hyperbolic spaces.

A $ W $ hyperbolic space is a metric space $(X, d)$ endowed with a convexity mapping $W : X \times X \times [0, 1] \to X$,
where $W(x, y, \lambda)$ is intended to abstractly represent a convex combination of parameter $(\lambda)$ of the points 
$x$ and $y$, satisfying a number of axioms.

In this project, one defines a $W$-hyperbolic space by choosing a type $X$ representing the points in the space, an appropriate distance function, and an appropriate convexity mapping defined on $X$.
Examples of such spaces defined in this project are:
$\mathbb{R}^n$ for different norms (the ones given by `numpy`),
$\mathcal{l}^p$ spaces and 
$L^p([a, b])$ spaces.

The fixed point iterations implemented as examples are:
- The Mann iteration
- The Halpern iteration
- The Tikhonov-Mann iteration 

The project provides ways to computed and plot the rates of asymptotic regularity of the iteration.

In order to define a new iteration, one should extend the `Iteration` class 
and override the `update` method which defines the way the value $x_{n + 1}$ is to be computed from $x_n$.
Furthermore, one should define a constructor for the new iteration,
setting the space in which the iteration takes place, 
the initial value,
and the operator relative to which asymptotic regularity should be computed (this may be left as `None`).

For example, let us define the Mann iteration, governed by the update rule $x_{n + 1} = W(x_n, T_n, \lambda_n)$:
```
class Mann(Iteration):
    def __init__(self, space, parameters: Callable[[int], float], operator: Callable[[X], X], initial: X):
        Iteration.__init__(self, 
            space = space, 
            operator = lambda x, n: operator(x), 
            initial = initial
        )
        self.parameters = parameters

    def update(self, curr, step):
        return self._space.W(curr, self._operator(curr, 0), self.parameters(step))
```

TODO: 
- define other spaces, particularly nonlinear ones such as CAT(0) spaces 
- create a way to visualize the way an algorithm produces its values 

Packages required:
- numpy 
- sympy 
- geomstats
- matplotlib 
- tqdm 
