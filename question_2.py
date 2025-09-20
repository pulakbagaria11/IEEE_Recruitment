
#create an infinite loop which breaks when the no. of words is less than 100
while True:
    #paragraph input
    para = input("Enter a paragraph")
    #converting uppercase characters into lowercase
    para = para.lower()
    #a blank para2 to store all letter and spaces (exclude all special symbols)
    para2 = ""
    for i in para:
        if i.isalpha() or i==" ":
            para2+=i


    #creating a list of different words
    words = para2.split()

    #checking if the number of words is less than or eqqual to 100
    if len(words)<=100:
        break
    else:
        print("Word limit crossed. Try again")

c = 0

for word in words:
    #if the word is same when spelt backwards, print it
    if word == word[-1::-1]:
        print(word)
        c+=1
if c==0:
    #if no palindrome is found, print 0
    print(0)