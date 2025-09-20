import numpy as np
import matplotlib.pyplot as plt

#generate 1000 random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

#generate x values as indices
x = np.arange(len(data))

#plotting the scatter graph
plt.figure(figsize=(10, 6))
plt.scatter(x, data, alpha=0.6, color='blue', s=10)
plt.title('Scatter Plot of 1000 Random Numbers from a Normal Distribution')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
