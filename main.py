from mimetypes import init
from Iteration import *

iter = TikhonovMann(
    space = FiniteDimensional(1),
    parameters1 = lambda n: n/(n + 1), 
    parameters2 = lambda n: 0.5, 
    operator = lambda x: np.sqrt(x ** 2 + 5),
    initial = np.array([0]),
    origin = np.array([7])
)


# [print(iter[i]) for i in range(0, 1000)]

plt.figure(0)
as_reg_errs = iter.get_as_reg_errs(100)
as_reg_to_op_errs = iter.get_as_reg_to_op_errs(100)
plt.plot(as_reg_errs)
plt.plot(as_reg_to_op_errs)

plt.figure(1)
steps_until = iter.get_steps_until_as_reg_errs(10)
plt.plot(steps_until)

plt.figure(2)
steps_until_op = iter.get_steps_until_as_reg_to_op_errs(10)
plt.plot(steps_until_op)

plt.show()
