import numpy as np
from functions.parser import parse_function
from functions.plot import plot_gradient_field

print("Welcome to the Gradient Field Visualizer!")
print("Enter a function of x and y (example: x**2 + y**2 - 2*x*y + 3*x)")
user_input = input("f(x, y) = ")

# Convert user input into a Python function
f = parse_function(user_input)

# Ask for ranges
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ymin = float(input("Enter ymin: "))
ymax = float(input("Enter ymax: "))

# Ask for density
density = int(input("Enter density (20–40 recommended): "))

# Run the visualizer
plot_gradient_field(
    f,
    x_range=(xmin, xmax),
    y_range=(ymin, ymax),
    density=density
)
