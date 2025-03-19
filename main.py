import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f1(x):
    return x**2 - 4 * np.sin(x)

def f2(x):
    return x**2 - 1

def f3(x):
    return x**3 - 3*x**2 + 3*x - 1

# Bisection method
def bisection(f, a, b, max_iter=1000, callback=None):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    prev_c = None
    for _ in range(max_iter):
        # Bisection formula
        c = (a + b) / 2
        # Call the callback function if provided
        if callback:
            callback(c)
        # if the previous c is the same as the current c, return c
        if c == prev_c:
            return c
        
        prev_c = c
        #set the new interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Newton's method
def newton(f, df, x0, max_iter=1000, callback=None):
    prev_x1 = None
    for _ in range(max_iter):
        # newton's formula
        x1 = x0 - f(x0) / df(x0)
        # Call the callback function if provided
        if callback:
            callback(x1)
        # if the previous x1 is the same as the current x1, return x1
        if x1 == prev_x1:
            return x1
        prev_x1 = x1
        x0 = x1
    return x0

# Secant method
def secant(f, x0, x1, max_iter=1000, callback=None):
    prev_x2 = None
    for _ in range(max_iter):
        # Check for division by zero
        if f(x1) == f(x0):
            print("Division by zero in secant method.")
            return x1
        # Secant formula
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        # Call the callback function if provided
        if callback:
            callback(x2)
        # if the previous x2 is the same as the current x2, return x2
        if x2 == prev_x2:
            return x2
        
        prev_x2 = x2
        x0, x1 = x1, x2
    return x1

# Derivatives of the functions
def df1(x):
    return 2*x - 4 * np.cos(x)

def df2(x):
    return 2*x

def df3(x):
    return 3*x**2 - 6*x + 3

# Function to find valid values for the bisection method
def find_valid_bisection_interval(f, start, end, step=0.1):
    a = start
    while a < end:
        b = a + step
        if f(a) * f(b) < 0:
            return a, b
        a = b
    raise ValueError("No valid interval found within the given range.")

# Function to track convergence rates
def track_convergence(method, *args, **kwargs):
    max_iter = kwargs.get('max_iter', 100)
    history = []
    def callback(x):
        history.append(x)
    kwargs['callback'] = callback
    root = method(*args, **kwargs)
    return root, history, len(history)

def plot_convergence(history, title):
    plt.figure()
    plt.plot(history, marker='o')
    plt.title(title)
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def main():
    # List of functions and their derivatives
    functions = [
        (f1, df1, "Function 1", 0.0),
        (f2, df2, "Function 2", -1.0),
        (f3, df3, "Function 3", 1.0)
    ]

    for f, df, name, actual_root in functions:
        print(f"\nProcessing {name}:")

        # Define the interval and initial guesses
        try:
            a, b = find_valid_bisection_interval(f, -1.23, 1)
            print(f"Valid interval for bisection: [{a}, {b}]")
        except ValueError as e:
            print(f"Skipping {name} due to invalid interval: {e}")
            continue

        x0_newton = -0.353
        x0_secant, x1_secant = -0.567, -0.353

        # Track convergence for each method
        root_bisection, history_bisection, iter_bisection = track_convergence(bisection, f, a, b)
        root_newton, history_newton, iter_newton = track_convergence(newton, f, df, x0_newton)
        root_secant, history_secant, iter_secant = track_convergence(secant, f, x0_secant, x1_secant)

        # Print the roots and iterations
        print(f"Bisection method root: {root_bisection}, error: {abs(root_bisection - actual_root)}, iterations: {iter_bisection}")
        print(f"Newton's method root:  {root_newton}, error: {abs(root_newton - actual_root)}, iterations: {iter_newton}")
        print(f"Secant method root:    {root_secant}, error: {abs(root_secant - actual_root)}, iterations: {iter_secant}")

        # Plot the convergence
        plot_convergence(history_bisection, f"{name} - Bisection Method Convergence")
        plot_convergence(history_newton, f"{name} - Newton's Method Convergence")
        plot_convergence(history_secant, f"{name} - Secant Method Convergence")

if __name__ == "__main__":
    main()




