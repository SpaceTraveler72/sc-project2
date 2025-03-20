# SC Project 2

## Description

This project finds the roots of various functions using the bisection, newton, and secant methods. It prints
out the roots found in results.txt and a convergence analysis in convergence_results.txt. The program also
creates a variety of graphs that show each method's steps to get to the root. Close out of one graph to get
to the next.

### Bisection Method

The bisection method is a root-finding technique that works by repeatedly dividing an interval in half and selecting the subinterval where the root lies. It requires the function \( f(x) \) to be continuous on the interval \([a, b]\) and \( f(a) \cdot f(b) < 0 \).

The steps are as follows:

1. Compute the midpoint \( c = \frac{a + b}{2} \).
2. Evaluate \( f(c) \):
   - If \( f(c) = 0 \), \( c \) is the root.
   - If \( f(a) \cdot f(c) < 0 \), set \( b = c \).
   - Otherwise, set \( a = c \).
3. Repeat until the interval \([a, b]\) is sufficiently small.

The method guarantees convergence to a root if the initial interval satisfies the conditions.

### Newton Method

The Newton method (or Newton-Raphson method) is an iterative root-finding technique that uses the derivative of the function to approximate the root. Starting with an initial guess \( x_0 \), the method iteratively refines the estimate using the formula:

\[
x\_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

The method converges quadratically if the initial guess is close to the root and \( f'(x) \neq 0 \) at the root. However, it requires the derivative \( f'(x) \) to be known and may fail if the derivative is zero or the function is not well-behaved.

### Secant Method

The Secant method is a root-finding technique similar to the Newton method but does not require the derivative of the function. Instead, it approximates the derivative using a secant line through two points. Starting with two initial guesses \( x_0 \) and \( x_1 \), the method iteratively refines the estimate using the formula:

\[
x*{n+1} = x_n - f(x_n) \cdot \frac{x_n - x*{n-1}}{f(x*n) - f(x*{n-1})}
\]

The Secant method converges faster than the bisection method but slower than the Newton method. It is useful when the derivative is difficult to compute or unavailable.

## Usage

To install the libraries for the project, run the following command:
(or just use a virtual environment)

```sh
pip install -r requirements.txt
```
