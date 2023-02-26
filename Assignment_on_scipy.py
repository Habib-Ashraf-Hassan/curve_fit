import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def f(t, a, b, c):
    return a * np.cos(2*np.pi*t + b) + c


dataF = np.loadtxt('Algeria_temp1_anually.txt', delimiter=',', dtype='str')
yr = dataF[1:, 2]
avr_temp = dataF[1:, 3]

x = yr.astype(np.float64)
y = avr_temp.astype(np.float64)

# Create a new plot with just the temperature vs year data
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(x, y, '-o', color='blue')
ax.set_xlabel('Date(years)')
ax.set_ylabel('Temperature (Celsius)')
ax.set_title('Algeria Temperature')
plt.savefig("Algeria temp graph")
plt.show()

# Fit the function to the data using curve_fit()
popt, pcov = curve_fit(f, x, y)

# Extract the optimized parameters
a_fit, b_fit, c_fit = popt

# Set the figure size to 10 inches wide by 8 inches tall
fig2, ax2 = plt.subplots(figsize=(10, 8))

# Create a line plot of temperature vs year with error bars
ax2.errorbar(x, y, fmt='o', ecolor='red', capsize=5)

# Generate the curve of best-fit using the optimized parameters
t_fit = np.linspace(x.min(), x.max(), 100)
temp_fit = f(t_fit, a_fit, b_fit, c_fit)

# Add the curve of best-fit to the plot
ax2.plot(t_fit, temp_fit, '-r', label='Curve of best-fit')

# Add x and y axis labels, a title, and a legend
ax2.set_xlabel('Date(years)')
ax2.set_ylabel('Temperature (Celsius)')
ax2.set_title('Algeria Temperature with line of best fit')
ax2.legend(loc='best')
plt.savefig("Algeria temp graph with curve of best fit")
plt.show()
