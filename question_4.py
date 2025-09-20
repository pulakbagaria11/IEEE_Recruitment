import numpy as np

#creating a 5x5 array of random numbers between 1 and 100
array = np.random.randint(1, 101, size=(5, 5))
print(array, "\n")

#sliced matrix
array3x3 = array[1:4,1:4]
print(array3x3)

#first row and last column
first_row = array3x3[0]
last_column = array3x3[:,-1]

#calculating dot pdt
dot = first_row@last_column

print(dot)

