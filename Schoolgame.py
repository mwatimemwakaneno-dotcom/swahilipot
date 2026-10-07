print("WELCOME TO THE SCHOOL GAME")
def get_player_name(name):
    name = input("Enter your name: ")
    return name 

print("Hello, " + get_player_name("name") + "! Let's start the game.")

playing = True
while playing:
    answer = input("What is 2 + 2? ")
    if answer == "4":
        print("Correct!")
    elif answer == "!4":
        print("Incorrect! The correct answer is 4.")
    else:
        print("Invalid input. Please enter a number.")

    again = input("Do you want to play again? (yes or no): ")
    if again.lower() != "yes":
        playing = False
        print("Thank you for playing the game!")

cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
print("Here are some car brands:")
for car in cars:
    print(car)
guess = input("Guess a car brand from the list above: ")
if guess in cars:
    print("Correct! " + guess + " is in the list.")
else:
    print("Sorry, " + guess + " is not in the list.")

again = input("Do you want to play again? (yes or no): ")
if again.lower() != "yes":
    playing = False
    print("Thank you for playing the game!")    




