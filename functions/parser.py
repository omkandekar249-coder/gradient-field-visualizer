import numpy as np

def parse_function(user_input):
    """
    Convert user input like 'x**2 + y**2' into a Python function f(x, y).
    """
    allowed_names = {
        'np': np,
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'log': np.log,
        'abs': np.abs
    }

    def f(x, y):
        return eval(user_input, {"__builtins__": {}}, {**allowed_names, 'x': x, 'y': y})

    return f

