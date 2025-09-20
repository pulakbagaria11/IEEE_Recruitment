#taking n as input
n = int(input())

#creating a blank string of size n
s =" "*n

#after every iteration, the last non "*" value of s gets converted into *
for i in range(-1, -n-1, -1):
    s = s[:i]+"*"*abs(i)
    print(s)
