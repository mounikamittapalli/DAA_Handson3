import timeit
import matplotlib.pyplot as plt
import numpy as np

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1

# List of n values (small to large)
n_values = [1, 2, 3, 5, 10, 20,30,40,50, 100, 200, 500, 1000, 2000, 5000]

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
#Zoom in on smaller n values to find n_0
plt.xlim(0, 100)  # Zoom in on the first 50 values of n
plt.ylim(0, 0.5)  # Adjust y-axis limits to focus on the measured time scale

# Indicate where n_0 might be (based on visual inspection)
n_0 = 30
plt.axvline(x=n_0, color='g', linestyle=':', label=f'n_0 ≈ {n_0}')

plt.xlabel('n (Size of List)')
plt.ylabel('Time (Seconds)')
plt.title('location of n_0')
plt.legend()
plt.grid(True)
plt.show()


