#   quiz master

user_name = input("Hello Player! Please enter your name: ")
print("Welcome", user_name, "to Science Quiz Master!")
print("Please type Yes/Y to start or type quit/Q to exit the game")

user_mark = 0
user_choice = input("Enter your choice: ")
while user_choice == 'y':
    print("Let us start the game! Have fun! ")
    print("What is RBC?")
    ans1 = input("Your answer: ")
    print("What is the value of acceleration due to gravity?")
    ans2 = float(input("Your answer: "))
    print("Who is the famous physicist known for his work for Theory of Relativity?")
    ans3 = input("Your answer: ")
    print("What is the symbol for Sodium metal?")
    ans4 = input("Your answer: ")
    print("Which is the most reactive metal in the activity series?")
    ans5 = input("Your answer: ")

    if ans1 == "Red Blood Cell".lower():
        print("You are correct")
        user_mark += 1
    elif ans2 == 9.8:
        print("You are correct")
        user_mark += 1
    elif ans3 == "Albert Einstein".lower():
        print("You are correct")
        user_mark += 1
    elif ans4 == "Na":
        print("You are correct")
        user_mark += 1
    elif ans5 == "Potassium".lower():
        print("You are correct")
        user_mark += 1
    else:
        print("You are incorrect")

    print("Thank you for playing the game!")
    print("You have scored", user_mark, "out of 5")

    if user_mark >= 3:
        print("Well Done")
    elif user_mark < 3:
        print("Nice try")

    accuracy = (user_mark / 5) * 100
    print("You have", accuracy,"% accuracy")
print("Thank you! Have a nice day")

