import timeit
import matplotlib.pyplot as plt
import numpy as np

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
            y = i + j

# List of n values (small to large)
n_values = [1, 2, 5, 10, 20,30,40, 50, 100, 200, 500, 1000, 2000, 5000]

# Measure the time for each n
execution_times = []
for n in n_values:
    exec_time = timeit.timeit(lambda: f(n), number=1)
    execution_times.append(exec_time)

# Plot the polynomial fit curve
coeffs = np.polyfit(n_values, execution_times,2)
poly_fit = np.poly1d(coeffs)

# Plot the polynomial fit curve
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, label='Measured Time',marker='x',color= 'blue')
plt.plot(n_values, poly_fit(n_values), label='Polynomial Fit (Degree 2)',marker='o',color='red')
plt.xlabel('n (Size of List)')
plt.ylabel('Time (Seconds)')
plt.title('Time vs n for Function f(n)')
plt.legend()
plt.grid(True)
plt.show()


