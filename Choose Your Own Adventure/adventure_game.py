#
"""
Created on Sat Oct 16 2021

@author: Aidan Majeed

The problem this code attempts to solve is simply boredom.
"""
# start of the interactive game
def start():
  print("\nAidan Majeed's Python Game to Solve Boredom!")
  print("============================================")
  print("Instructions: Type 1 OR 2 when asked.\n")
  # calls the intro function to pose the first scenario
  intro()  

# intro function begins the story and gives user first decision
def intro():
    print('One day, on your way to school, you see a glowing rock on the ground.\n')
    prompt = str(input("The rock peaks your interest. What do you do?\n 1: Pick up the rock\n 2: Ignore it.\n Enter 1 or 2: "))
    # if user input is equal to 1, call new function to pose a new choice
    if prompt == '1':
        print("You pick up rock and inspect it. However, you slip it in your bag as you're late for school.")
        school_arc()
    # if user input is equal to 2, end the game
    elif prompt == '2':
        print('You ignore the rock and head to school on time\n')
        ending_0()

# new scenario is presented based on previous choice
def school_arc():
    print("\nYou get to school, and finish your first class. Then you hear the rock vibrating in your bag. Do you: ")
    prompt = str(input(" 1: Skip class and deal with the rock\n 2: Leave it for later\n Enter 1 or 2: "))
    # if user input is equal to 1, call new function to pose a new choice
    if prompt == '1':
        print('You leave school in between classes and inspect the rock outside, only for it to engulf you in green aura.')
        power_arc()
    # if user input is equal to 2, call a new function to pose a new scenario    
    elif prompt == '2':
        print('You decide to wait and deal with the rock after class. However... \n')
        suspension()

# new scenario is presented based on a previous choice
def power_arc():
    print("\nThe aura that has just engulfed you has been absorbed into your body, and you feel tremendous power.")
    print('This power rush has scared you, and you scream, causing a shockwave, garnering much attention. What do you do?')
    prompt = str(input(" 1: Go home and test your power\n 2: Try and reason with those looking at you\n Enter 1 or 2: "))

    # if user input is equal to 1, call new function to pose a new choice
    if prompt == '1':
        print('Curious of your newfound power, you go home to test it.')
        train_arc()
    # if user input is equal to 2, end the game
    elif prompt == '2':
        print('You try to reason with those naturally scared of what you have just done.\n')
        ending_1()

# new scenario is presented based on a previous choice
def suspension():
    print('Leaving the rock in your bag for an extended period of time ended up causing a fire. Leading back to your bag, you end up suspended.')
    print('The fire left the rock in fragments, but it still looks valuable. What are you going to do with the rock?')
    prompt = str(input(" 1: Sell it for a lot of money\n 2: Keep it \n Enter 1 or 2: "))

    # if user input is equal to 2, end the game
    if prompt == '2':
        print("You decide to keep the rock since you're a hoarder.")
        ending_2()
    # if user input is equal to 1, end the game
    elif prompt == '1':
        print('With nothing to lose, you sell the rock at a pawn shop\n')
        ending_3()

# new scenario is presented based on a previous choice
def train_arc():
    print("\nYou decide to try and control your powers, and after a while you've figured out how to:")
    print("Think of a number, then say the phrase as many times as the number chosen.")

    N = int(input("Whats your number? (Has to be positive!): "))
    phrase = str(input("Enter a phrase here: "))
    # input N is greater than 0
    N > 0 == True
    
    # while N is positve
    while N > 0:
        #loops phrase inputted by user N times
        for N_phrases in range(N):  
            print (phrase)
        break

    print("\nIt worked and was strong! After testing the method, you have one final choice:")
    prompt = str(input(" 1: Use your powers for good\n 2: Use it for money\n Enter 1 or 2: "))

    # if user input is equal to 1, call the true ending
    if prompt == '1':
        print("You decide to use your powers for good")
        ending_4()
    # if user input is equal to 2, end the game
    elif prompt == '2':
        print('You decide to make money with these newfound powers.\n')
        ending_5()

# multiple ending functions, each called depending on user's choice
def ending_0():
    print('Congratulations for being boring! Nothing happened and you ended the story prematurely.')
    prompt = str(input("Want to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing I guess')

def ending_1():
    
    print('\nReasoning with them only leads to the police arriving on the scene. You end of getting arrested for vandalism. The End.')
    prompt = str(input("\nWant to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing!')

def ending_2():
    print('\nYou display the rock in your room as if it was a collectors item, and return to normalcy. The End.')
    prompt = str(input("\nWant to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing!')

def ending_3():
    print('\nSelling the rock fragments gets you a whopping $2500! Not bad. The End.')
    prompt = str(input("\nWant to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing!')

def ending_4():
    print('\nUsing your powers for good has resulted in you becoming a world renowned hero! Nice Job. The End?.')
    prompt = str(input("\nWant to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing!')


def ending_5():
    print('\nUsing your powers for money has made you insanely rich! But are you truly happy? The End.')
    prompt = str(input("\nWant to restart? Enter Y for yes and N for no: "))

    # if user decides to play again, main function is called and game restarts
    if prompt == 'Y':
        start()
    else:
        print('Thanks for playing!')



if __name__ == "__main__":
    start()