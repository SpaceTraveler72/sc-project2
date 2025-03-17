import math
import numpy as np
import matplotlib.pyplot as plt

def finite_difference(h, x):
    # The finite difference formula is (f(x + h) - f(x))/h
    # where f(x) = sin(x)
    # h = step size
    # x = point of evaluation
    
    return (math.sin(x + h) - math.sin(x))/h
    
def central_difference(h, x):
    # The central difference formula is (f(x + h) - f(x - h))/(2h)
    # where f(x) = sin(x)
    # h = step size
    # x = point of evaluation
    
    return (math.sin(x + h) - math.sin(x - h))/(2*h)

def truncation_error_finite(h, x):
    # alternative method using taylor's theorem for f(x + h)
    # for taylor series next term error is less than: 
    # En+1 = h^n+1 * (f^n+1(e) / (n+1)!)
    # where e is some number between x and x + h
    
    # assume e is x + h for maximum error
    return abs(h/2)

def truncation_error_central(h, x):
    # because the central difference formula expands to cancel out the odd terms
    # the taylor expansion is already a alternating series meaning the error is less
    # than the next term
    
    # assume e is x + h for maximum error
    return abs(h**2 / 6)

def roundoff_error_finite(h):
    # the closer f(x + h) - f(x) is to 0 (machine epsilon) the more roundoff error we will have
    # the roundoff error is proportional to epsilon/h because the difference is modified by h
    
    epsilon = np.finfo(float).eps
    return epsilon *.5 / h

def roundoff_error_central(h):
    # the closer f(x + h) - f(x - h) is to 0 (machine epsilon) the more roundoff error we will have
    # the roundoff error is proportional to epsilon/2h because the difference is modified by 2h
    
    epsilon = np.finfo(float).eps
    # print(f"Machine epsilon in the form of 2^n: 2^{np.log2(epsilon):.0f}")
    return epsilon *.5 / (2 * h)

def plot_errors(x, h_min=1e-9, h_max=1e-1):
    # calculate h values using a log scale to get a good distribution of points
    h_values = np.logspace(math.log10(h_max), math.log10(h_min), 1000)
    
    # calculate the errors
    truncation_finite = [truncation_error_finite(h, x) for h in h_values]
    truncation_central = [truncation_error_central(h, x) for h in h_values]
    roundoff_errors_finite = [roundoff_error_finite(h) for h in h_values]
    roundoff_errors_central = [roundoff_error_central(h) for h in h_values]
    
    # calculate the total errors
    total_error_finite = [truncation_finite[i] + roundoff_errors_finite[i] for i in range(len(h_values))]
    total_error_central = [truncation_central[i] + roundoff_errors_central[i] for i in range(len(h_values))]

    # find the minimum total errors and corresponding h values
    min_total_error_finite = min(total_error_finite)
    min_h_finite = h_values[total_error_finite.index(min_total_error_finite)]
    
    min_total_error_central = min(total_error_central)
    min_h_central = h_values[total_error_central.index(min_total_error_central)]

    print(f"Minimum total error for finite difference: {min_total_error_finite:.5e} at h = {min_h_finite:.5e}")
    print(f"Minimum total error for central difference: {min_total_error_central:.5e} at h = {min_h_central:.5e}")

    plt.figure(figsize=(12, 6))

    # plot the finite difference errors
    plt.loglog(h_values, truncation_finite, label='Truncation Error Finite Difference', color='blue')
    plt.loglog(h_values, roundoff_errors_finite, label='Roundoff Error Finite Difference', color='purple')
    plt.loglog(h_values, total_error_finite, label='Total Error Finite Difference', color='green')

    # plot the central difference errors
    plt.loglog(h_values, truncation_central, label='Truncation Error Central Difference', color='red')
    plt.loglog(h_values, roundoff_errors_central, label='Roundoff Error Central Difference', color='orange')
    plt.loglog(h_values, total_error_central, label='Total Error Central Difference', color='yellow')

    # make the plot look nice
    plt.xlabel('h')
    plt.ylabel('Error')
    plt.title(f'Truncation and Roundoff Errors at x = {x}')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    plot_errors(x=1, h_min=1e-16, h_max=1e-0)