import numpy as np
import matplotlib.pyplot as plt
from .gradient import compute_gradient

def plot_gradient_field(f, x_range, y_range, density=20):
    x = np.linspace(*x_range, density)
    y = np.linspace(*y_range, density)
    X, Y = np.meshgrid(x, y)

    U = np.zeros_like(X)
    V = np.zeros_like(Y)

    for i in range(density):
        for j in range(density):
            U[i, j], V[i, j] = compute_gradient(f, X[i, j], Y[i, j])

    Z = f(X, Y)

    plt.figure(figsize=(8, 6))
    plt.contour(X, Y, Z, levels=20, cmap='coolwarm')
    plt.quiver(X, Y, U, V, color='black', alpha=0.7)

    plt.title("Gradient Field Visualizer")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
