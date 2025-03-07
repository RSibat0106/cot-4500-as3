
def euler_method(f, t0, y0, h, n):
    t, y = t0, y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta_method(f, t0, y0, h, n):
    t, y = t0, y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y

# Given function: dy/dt = t - y^2
def func(t, y):
    return t - y**2

# Parameters
t0, y0 = 0, 1  # Initial conditions
t_final = 2
iterations = 10
h = (t_final - t0) / iterations

# Compute solutions
euler_result = euler_method(func, t0, y0, h, iterations)
runge_kutta_result = runge_kutta_method(func, t0, y0, h, iterations)

# Print results
print(f"{euler_result}")
print(f"{runge_kutta_result}")
