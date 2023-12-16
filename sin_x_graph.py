import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data using NumPy
x = np.linspace(0, 10, 100)  # Generate 100 points from 0 to 10
y = np.sin(x)  # Compute the sine function for each point

# Plot the data using Matplotlib
plt.plot(x, y, label='Sin Function')
plt.title('NumPy and Matplotlib Test')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.show()  # Display the plot
# C:\Users\Administrator\AppData\Local\Programs\Python\Python312