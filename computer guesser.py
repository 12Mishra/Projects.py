import random

print("Hello player! Choose a number between 1-10 ")
b=random.randint(0,10)
user_input=int(input("Enter number which you have choosen "))

if user_input>10 and user_input<0:
    print("Out of range")
elif user_input==b:
    print("You have guessed correct")
else:
    print("You have guessed incorrect")

print("The computer had choosen",b)