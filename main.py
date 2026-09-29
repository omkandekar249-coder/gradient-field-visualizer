import numpy as np
from functions.plot import plot_gradient_field

def f(x, y):
    return x**2 + y**2 - 2*x*y + 3*x

if __name__ == "__main__":
    plot_gradient_field(
        f,
        x_range=(-5, 5),
        y_range=(-5, 5),
        density=25
    )

