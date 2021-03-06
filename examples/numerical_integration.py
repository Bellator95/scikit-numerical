""" Example of numerical integration using Gauss formula for 2-d function. """

import numpy as np
from numerical.integration import gauss


def f(x):
    return np.power(x[0], 2) + 2 * x[1] + 5


gauss.integrate(f, 0, 1, 0, 2 * np.pi, steps=(0.02, np.pi / 8))
