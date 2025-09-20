import numpy as np

#creating a 5x5 array of random numbers between 1 and 100
array = np.random.randint(1, 101, size=(5, 5))

#printing array
print(array)



#printing max, min and mean
print("Maximum value",array.max())
print("Minimum value", array.min())
print("Mean", array.mean())

#min-max normalization
min_val = np.min(array)
max_val = np.max(array)
normalized_array = (array - min_val) / (max_val - min_val)
print("Normalised array",normalized_array, "\n")

#flatten
flat = normalized_array.flatten()
print(flat)