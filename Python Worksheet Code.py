#!/usr/bin/env python
# coding: utf-8
Factorial of a number
# In[ ]:


num = int(input("Enter a number: "))    
f = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in f*i    
   print("The factorial of",num,"is",f)    

Number is prime or factorial
# In[ ]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")

python program to check whether a given string is palindrome or not
# In[ ]:


x =  input("The palindrome word") #"malayalam"
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")

Python program to get the third side of right-angled triangle from two given sides.
# In[ ]:


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )

python program to print the frequency of each of the characters present in a given string
# In[ ]:


input = input("provide word input for character/alphabet frequency")
frequencies = {} 
  
for char in input: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

print ("Per char frequency in '{}' is :\n {}".format(input, str(frequencies)))


# In[ ]:




