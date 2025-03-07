# Euler's method implementation without external libraries

# Define the differential equation: dy/dt = t - y^2
def f(t, y):
    return t - y**2

# Initial conditions
t0 = 0
y0 = 1
t_end = 2
n = 10  # Number of iterations

# Calculate step size
h = (t_end - t0) / n

# Initialize lists to store the results
t_values = [0] * (n + 1)
y_values = [0] * (n + 1)

# Set initial values
t_values[0] = t0
y_values[0] = y0

# Implement Euler's method
for i in range(n):
    y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values[i])
    t_values[i + 1] = t_values[i] + h

# Print the results
print("Euler's Method for dy/dt = t - y^2 with y(0) = 1")
print("t\t\ty\t\tdy/dt")
print("-" * 40)
for i in range(n + 1):
    print(f"{t_values[i]:.4f}\t\t{y_values[i]:.6f}\t\t{f(t_values[i], y_values[i]):.6f}")
