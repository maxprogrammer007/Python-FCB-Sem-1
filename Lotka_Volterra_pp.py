import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Lotka-Volterra equations
def predator_prey_system(y, t, alpha, beta, delta, gamma):
    x, z = y
    dxdt = alpha * x - beta * x * z
    dzdt = delta * x * z - gamma * z
    return [dxdt, dzdt]

# Set the initial conditions and parameters
initial_conditions = [40, 9]  # Initial prey and predator populations
alpha = 0.1  # Prey birth rate
beta = 0.02  # Rate at which predators kill prey
delta = 0.01  # Rate at which predators increase by consuming prey
gamma = 0.1  # Predator death rate

# Set the time points for integration
t = np.linspace(0, 200, 1000)

# Solve the system of differential equations
solution = odeint(predator_prey_system, initial_conditions, t, args=(alpha, beta, delta, gamma))

# Extract the prey and predator populations from the solution
prey_population, predator_population = solution.T

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, prey_population, label='Prey (x)')
plt.plot(t, predator_population, label='Predator (y)')
plt.title('Lotka-Volterra Predator-Prey Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
