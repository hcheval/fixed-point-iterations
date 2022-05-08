from abc import *
from functools import reduce
from typing import *
import numpy as np #type: ignore
import sympy as sp #type: ignore
import matplotlib.pyplot as plt #type: ignore
from tqdm import tqdm
from WHyperbolic import *


sp.init_printing(unicode = True)
X = TypeVar("X")



class Iteration(Generic[X]):
    def __init__(self, space:WHyperbolicSpace[X], initial: Optional[X] = None, operator = None):
        self.space = space
        self.initial: Optional[X] = initial
        self.operator = operator
        self.computed_values = []
        self.as_reg_err = []
        self.as_reg_to_op_err = []

    @abstractmethod
    def update(self, curr: X, step: int):
        ...

    def check_runnable(self) -> bool:
        return self.initial is not None

    def run_steps(self, steps: int, display_progress = True):
        if self.initial is None:
            print("Cannot run iteration because an initial value has not been provided.")
        # if as_reg_to_op and self.operator is None:
        #     print("Cannot compute asymptotic regularity relative to operator because no operator was provided.")

        prev = self.initial
        self.computed_values = [prev]
        for i in range(0, steps):
            if display_progress and i % 100 == 0:
                print(i, " / ", steps) 
            
            curr = self.update(prev, i)
            self.computed_values += [curr]
            prev = curr
    
        return self.computed_values


    def as_reg(self, steps = None, plotting = True):
        if len(self.computed_values) == 0: 
            if steps is None:
                print("The iterations has not been previously run. Asymptotic information can be computed now, but a number of steps must be provided")
            else:
                self.run_steps(steps)
        print("Computing asymptotic regularity errors...")
        self.as_reg_err = [self.space.dist(xi, xj) for xi, xj in tqdm(zip(self.computed_values[:-1], self.computed_values[1:]), total=len(self.computed_values[1:]))]
        if plotting:
            plt.plot(self.as_reg_err)
        return self.as_reg_err

    def as_reg_to_op(self, steps = None, plotting = True):
        if len(self.computed_values) == 0:
            if steps is None:
                    print("The iterations has not been previously run. Asymptotic information can be computed now, but a number of steps must be provided")
            else:
                self.run_steps(steps)
        print("Computing asymptotic regularity to operator errors...")
        self.as_reg_to_op_err = [self.space.dist(xi, self.operator(xi)) for xi in tqdm(self.computed_values)]
        if plotting:
            plt.plot(self.as_reg_to_op_err)
        return self.as_reg_to_op_err

    def steps_until_as_reg(self, epsilons: List[float], steps = None, plotting = True) -> Dict:
        if not self.computed_values:
            if steps is None:
                pass
            else: 
                self.run_steps(steps)

        steps = dict()
        for eps in epsilons:
            steps[eps] = next(i for i in tqdm(range(0, len(self.as_reg_err))) if self.as_reg_err[i] < eps)
        print("Computing steps needed to asymptotic regularity errors...")
        if plotting:
            plt.plot([snd for _, snd in steps.items()])
        return steps
    
    


class Mann(Iteration):
    def __init__(self, space, parameters: Callable[[int], float], operator: Callable[[X], X]):
        Iteration.__init__(self, space)
        self.parameters = parameters
        self.operator = operator

    def update(self, curr, step):
        return self.space.W(curr, self.operator(curr), self.parameters(step))



class Halpern(Iteration):
    def __init__(self, space, parameters, anchor, operator):
        Iteration.__init__(self, space)
        self.parameters = parameters
        self.anchor = anchor 
        self.operator = operator 

    def update(self, curr, step):
        return self.space.W(self.anchor, self.operator(curr), self.parameters(step))