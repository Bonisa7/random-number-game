import random 

print ("Hey! welocme to a number guessing game:) ")
top_of_range= input("Type a number: ")

guesses = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range) 

elif top_of_range <= 0:
    print("Please type a number greater than zero")
    quit()

else: 
    print ("Please type a number next time")
    quit()

random_number=random.randint (0, top_of_range)

a= print ("guess a number between 0 and", top_of_range)

while True:

    user_guess=input(": ") 
    guesses+=1
    if user_guess.isdigit():
        user_guess = int(user_guess)
        

    elif user_guess <= 0:
        print("Please type a number greater than zero")
        quit()

    else: 
        print ("Please type a number next time")
        continue
         

    if user_guess == random_number:
        print("You got it!")
        break

    elif user_guess < random_number:
        print("You were below the number!")

    elif user_guess > random_number:
        print("You were above the number!")
    
    else:
        print("You got it wrong!, please try again:")

print("Yay! you got it in", guesses , "guesses" )  




