# gradient-field-visualizer
A NumPy-based tool to visualize gradient fields, contour maps, and critical points for multivariable functions. A Python project I originally wrote back in high school (Feb 2026) when I was trying to understand Calc 3 better. I tried desmos and I thought I could visualize gradient fields using Python. 

The program asks you for:
- A function 
- 𝑓(𝑥,𝑦)
- The x‑range
- The y‑range
- The density of the grid

Then it uses NumPy to compute numerical partial derivatives and Matplotlib to plot the gradient field.

To Run: 
  python main.py
  
Example input:
- f(x, y) = x**2 + y**2 - 2*x*y
- xmin = -5
- xmax = 5
- ymin = -5
- ymax = 5
- density = 30

Libraries Used: 
- Numpy
- Matplotlib

