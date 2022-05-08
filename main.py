from Iteration import *

iter = Mann(
    space = lp(), 
    parameters = lambda n: 1./(n + 1), 
    operator = lambda x: 0.5 * x
)
iter.initial = 1 / (sp.Symbol("n") + 1)

iter.run_steps(10000)
iter.as_reg(plotting = True)
iter.as_reg_to_op(plotting = True)
iter.steps_until_as_reg(epsilons=[1./n for n in range(1, 100)])

plt.show()


# from sympy.abc import *
# sp.pprint(sp.summation(1 / (n**2), (n, 1, sp.oo)).evalf())