A framework for implementing, simulating and visualizing fixed point iterations in $W$-hyperbolic spaces.

A $W$-hyperbolic space is a metric space $(X, d)$ endowed with a convexity mapping $W : X \times X \times [0, 1] \to X$,
where $W(x, y, \lambda)$ is intended to abstractly represent a convex combination of the points 
$x$ and $y$ of parameter $\lambda$. 
For a structure $(X, d, W)$ to be called a $W$-hyperbolic space, it it is required to furthermore satisfy a number of axioms, which are not relevant to this implementation.

In this project, one defines a $W$-hyperbolic space by choosing a type $X$, representing the points in the space, an appropriate distance function, and an appropriate convexity mapping, defined on $X$.
Examples of such spaces defined in this project are:
$\mathbb{R}$ for different norms (the ones given by numpy),
$\mathcal{l}^p$ spaces and 
$L^p([a, b])$ spaces.

The fixed point iterations implemented as examples are:
- The Halpern iteration
- The Tikhonov-Mann iteration 

The project provides ways to computed and plot the rates of asymptotic regularity of the iteration.

In order to define a new iteration, one should extend the `Iteration` class 
and override the `update` method which defines the way the value $x_{n + 1}$ is to be computed from $x_n$.
Furthermore, one should define a constructor for the new iteration,
setting the space in which the iteration takes place, 
the initial value,
and the operator relative to which asymptotic regularity should be computed (this may be left as `None`).

For examples, let us define the Mann iteration, governed by the update rule $x_{n + 1} = W(x_n, T_n, \lambda_n)$:
`
class Mann(Iteration):
    def __init__(self, space, parameters: Callable[[int], float], operator: Callable[[X], X], initial: X):
        Iteration.__init__(self, 
            space = space,
            operator = lambda x, n: operator(x),
            initial = initial
        )
        self.parameters = parameters

    def update(self, curr, step):
        return self._space.W(self.anchor, self._operator(curr, 0), self.parameters(step))

`

Packages required:
- numpy 
- sympy 
- matplotlib 
- tqdm 