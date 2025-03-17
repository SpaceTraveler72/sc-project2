import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Define the functions
def f1(x):
    return x**2 - 4 * np.sin(x)

def f2(x):
    return x**2 - 1

def f3(x):
    return x**3 - 3*x**2 + 3*x - 1

# Bisection method
def bisection(f, a, b, tol=1e-5, max_iter=100, callback=None):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    for _ in range(max_iter):
        c = (a + b) / 2
        if callback:
            callback(c)
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Newton's method
def newton(f, df, x0, tol=1e-5, max_iter=100, callback=None):
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if callback:
            callback(x1)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# Secant method
def secant(f, x0, x1, tol=1e-5, max_iter=100, callback=None):
    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            return x1
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if callback:
            callback(x2)
        if abs(x2 - x1) < tol:
            return x2
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
    tol = kwargs.get('tol', 1e-5)
    max_iter = kwargs.get('max_iter', 100)
    history = []
    def callback(x):
        history.append(x)
    kwargs['callback'] = callback
    root = method(*args, **kwargs)
    return root, history

def plot_convergence(history, title):
    plt.figure()
    plt.plot(history, marker='o')
    plt.title(title)
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def main():
    # Define the interval and initial guesses
    a, b = find_valid_bisection_interval(f1, -10, 10)
    x0_newton = 2
    x0_secant, x1_secant = 2, 3

    # Track convergence for each method
    root_bisection, history_bisection = track_convergence(bisection, f1, a, b)
    root_newton, history_newton = track_convergence(newton, f1, df1, x0_newton)
    root_secant, history_secant = track_convergence(secant, f1, x0_secant, x1_secant)

    # Print the roots
    print(f"Bisection method root: {root_bisection}")
    print(f"Newton's method root: {root_newton}")
    print(f"Secant method root: {root_secant}")

    # Plot the convergence
    plot_convergence(history_bisection, "Bisection Method Convergence")
    plot_convergence(history_newton, "Newton's Method Convergence")
    plot_convergence(history_secant, "Secant Method Convergence")

if __name__ == "__main__":
    main()




