import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import streamlit as st


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

st.subheader("Graph of date in years against temperature in celsius of Algeria with error bar and curve of best fit")
st.pyplot(fig2)

st.subheader("Graph of date in years against temperature in celsius of Algeria")
st.pyplot(fig)

st.write('''The lowest temperature would occur at the minimum of the curve of best-fit, 
which would correspond to the value of t where cos(2*pi*t + b) is equal to -1 (since cos(theta) reaches
its minimum value of -1 i.e when theta = pi).
The function f(t) = a * cos(2*pi*t + b) + c has a period of 1 year,
meaning that the curve of best-fit will repeat every year. 
Therefore, the lowest temperature would occur once per year.

Using the popt array obtained from the curve_fit() function earlier, we can extract the optimized value of b, 
which represents the phase shift of the curve of best-fit. For example, we can print the value of b
therefore min temperature is {popt[1]*10} celsius which is 8.842645288016723 celsius
''')
st.write('''We can draw these deductions from the graph/ data that:
Based on the curve of best-fit generated from the data, we can conclude that there is a periodic pattern 
in the temperature fluctuations in Kenya over the years. The function used to generate the curve of best-fit is:

f(t) = a * cos(2*pi*t + b) + c

where t is the year, a, b, and c are fitting parameters.

The cos(2*pi*t + b) term in the function indicates that the temperature varies sinusoidally over time. 
This is consistent with the fact that the temperature on Earth is influenced by seasonal changes due to 
the tilt of the Earth's axis and its rotation around the Sun. 
The a parameter controls the amplitude of the temperature variation,
while c represents the average temperature over time.
''')
