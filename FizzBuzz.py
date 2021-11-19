# Script for playing Fizz Buzz game, to learn more about conditionals. 
# https://www.teclado.com/30-days-of-python/python-30-day-6-project

for num in range(1,101):
    if (num % 3 == 0 and num % 5 == 0):
        print ("Fizz Buzz")
    elif (num % 5 == 0):
        print("Buzz")
    elif (num % 3 == 0):
        print("Fizz")
    else:
        print(num)
        
