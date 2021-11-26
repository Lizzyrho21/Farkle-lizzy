import random

from game_logic import GameLogic

# print("This is to test the rooling that you may get")
rand = random.Random()
dice_number = [1, 2, 3, 4, 5, 6]  # this is my array of dice
dice_number_randomize = []  # this is what I'm using to show the number.


def rollin():
    # this would random the number that I can choose from
    for i in dice_number:
        dice_number_randomize.append(rand.randint(1, 6))
    print(dice_number_randomize)


# when user types 'yes', game starts
# two variables are set : game_not_done = False , points_achevied = 10,000
# game_done = True
bank_score = 10  # placeholder for banked score


class play_game:
    def __init__(self):
        self.points_to_be_scored = 10000  # This is the score the user wants to acheieve
        self.game_done = True
        self.saved_numbers = []  # user inputs numbers from array
        self.roll = rollin  # we set a property to equal this function we created

    def start_game(self):
        # start_game function implements the gameplay
        # 1. rules will be printed to the screen
        global numbers
        start_round = True  # For starting round
        self.roll() #roll the dice!
        while start_round: #this is true
            numbers = input(" > ") #they can input numbers
            if numbers == "q": # however, if they type q or quit..
                start_round = False # this loop will return false
            else:
                self.numbers_saved()
        # 2. dice rolls with 6 random values (range from 1-6)
        # 3. user enters values

    def numbers_saved(self): #Inside of this method, we have our saved numbers from user pick, and calculate score
        global change_to_number #variable set
        split_the_numbers = numbers.split(",") #split the numebrs entered by the comma 
        change_to_number = [] # set em' in an array
        for i in split_the_numbers: #loop through the numbers we got from user
            change_to_number.append(int(i)) # as we place the numbers in the array we change each one to a vaild intger
        # call that funcation NV that we had in Gl pass that in.


        ##====Calculating the score=======##
        GameLogic.calculate_score(self,change_to_number) # calling from our GameLogic file, we want to calculate our score
        if (GameLogic.calculate_score): # If this is true
            for i in change_to_number: # we loop through the numbers in the array from user
                dice_number_randomize.remove(i) # we remove from the original array each number the user enters
                new_dice = dice_number_randomize
            print(dice_number_randomize) # print our new dice 
            response = input("Type (r)oll to reroll the dice, or(b)ank to bank your points \n > ") #ask to reroll or bank points
                
            if response == "b":
                    print("Okay! Banking points...")
                    print("Here are your banked points!!") 
                    # Bank_points.bank_the_users_points(calculate_score.total_points)


            elif response == "r":
                    print("hang on.. rerolling the dice") 
                    numbers_saved = [random.randint(1, 6) for i in range(len(new_dice))]
                    print(numbers_saved)
                    # self.numbers_saved()
                    # GameLogic.calculate_score(self, change_to_number)






                    # if x is not 5 or 1:
                    #     print("Farkle!")
                    #     while (dice_number_randomize): #while the array has numbers
                    #         for i in dice_number_randomize:
                    #             dice_number_randomize.remove(i) #step in and remove each number
                    #             self.roll()     
# self.roll() #then roll again
        
        # print(change_to_number)# This was just to make sure that everything was append.
        # TODO: If there are no numbers for the user to submit they have the option to bank the points or roll the dice again
        # TODO: Add number of rounds implementation
        # TODO: Add banking functionality

#depending on if they win or lose!!
    def win_or_lose(self):  # Our method to check if user acheieved points
        print("Called function!")
        while(self.game_done):  # This is set to false because we are not sure if game is done
            # if the final score is equal to the banked score, the user will win!
            if(self.points_to_be_scored == bank_score):
                # you won message
                print("You won! Would you like to play again? \n yes or no")
                response = input(" > ")
                if response == "yes":
                    print("Great!")
                elif response == "no":
                    print("Thanks for playing!")
                    self.game_done = False
            elif self.points_to_be_scored != bank_score:
                print("You Lost!")
                self.game_done = False


# TODO: Implement the while loop to start and play game, user can type 'q' at anytime to quit the game
game_is_starting = True
play_game = play_game()

# while game_is_starting:

#     response = input("Type (q)uit to quit \n")
#     if response.lower() == "q":
#         game_is_starting = False
#         print("Thanks for playing!")


# =======EVERYTHING BELOW IS DEBUG INFO / NOTES ===========
# game.win_or_lose()
# game.start_game()
# game_not_done will be a while loop that is initally set to false
# If user has more than 0 points, game will continue (or loop)
# If user does not reach more than 0 points, gae will = ZILCH (or end)
# class GameLogic:
#     def __init__(self):
#         self.total_points = 0
#         self.rounds_left = 6
