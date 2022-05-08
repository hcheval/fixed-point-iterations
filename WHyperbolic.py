from typing import *
import numpy as np
import sympy as sp


X = TypeVar("X")

class WHyperbolicSpace(Generic[X]):
    def __init__(self, dist: Callable[[X, X], float], W: Callable[[X, X, float], X]):
        self.dist = dist 
        self.W = W


class FiniteDimensional(WHyperbolicSpace[np.array]):
    def __init__(self, dim: int, order = 2):
        self.dim = dim
        WHyperbolicSpace.__init__(self, 
            dist=lambda x, y: np.linalg.norm(x - y, ord=order), 
            W=lambda x, y, a: (1 - a) * x + a * y
        )


class LpInterval(WHyperbolicSpace[sp.core.function.FunctionClass]):
    def __init__(self, left: int = 0, right: int = 1, order = 2, variable: sp.Symbol = sp.Symbol("t")):
        self.dim = "continuum"
        WHyperbolicSpace.__init__(self,
            dist = lambda x, y: (sp.integrate(sp.Abs(x - y) ** order, (variable, left, right)) ** (1 / order)).evalf(),
            W = lambda x, y, a: (1 - a) * x + a * y
        )


class lp(WHyperbolicSpace[sp.core.function.FunctionClass]):
    def __init__(self, order = 2, variable = sp.Symbol("n")):
        self.dim = "countable"
        WHyperbolicSpace.__init__(self,
            dist = lambda x, y: (sp.summation(sp.Abs(x - y) ** order, (variable, 0, sp.oo)) ** (1 / order)).evalf(),
            W = lambda x, y, a: (1 - a) * x + a * y
        )