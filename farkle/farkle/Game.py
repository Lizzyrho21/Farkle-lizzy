import random

from game_logic import GameLogic

# print("This is to test the rooling that you may get")
rand = random.Random()
dice_number = [1, 2, 3, 4, 5, 6]  # this is my array of dice
dice_number_randomize = []  # this is what I'm using to show the number.



def rollin():
    # this would random the number that I can choose from
    global dice_number_randomizes 
    for i in dice_number:
        dice_number_randomize.append(rand.randint(1, 6))
        dice_number_randomizes = list(dice_number_randomize)
    print(dice_number_randomize)

    # print(type(dice_number_randomizes))


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


    def numbers_saved(*self, num=None): #Inside of this method, we have our saved numbers from user pick, and calculate score
        global change_to_number #variable set
        split_the_numbers = numbers.split(",") #split the numebrs entered by the comma 
        change_to_number = [] # set em' in an array
        for i in split_the_numbers: #loop through the numbers we got from user
            change_to_number.append(int(i)) # as we place the numbers in the array we change each one to a vaild intger
            change_to_numbers = list(change_to_number)
        # call that funcation NV that we had in Gl pass that in.


        ##====Calculating the score=======##
        GameLogic.calculate_score(self,change_to_number) # calling from our GameLogic file, we want to calculate our score
        if (GameLogic.calculate_score): # If this is true
            remove_from_list(change_to_number, dice_number_randomize)
            # dice_number_randomize
            # for i in change_to_number: # we loop through the numbers in the array from user
            #     if not i in change_to_number: 
            #         print("FARKLE")
            #     else:    
            #         dice_number_randomize.remove(i) # we remove from the original array each number the user enters
            #     # FIXME: 1 OR 5 PRESENT A VALUEERROR: ValueError: list.remove(x): x not in list
            print(dice_number_randomize) # print our new dice 
            response = input("Type (r)oll to reroll the dice, or(b)ank to bank your points \n > ") #ask to reroll or bank points
                
            if response == "b":
                    print("Okay! Banking points...")
                    print("Here are your banked points!!") 
                    # Bank_points.bank_the_users_points(calculate_score.total_points)


            elif response == "r":
                    print("hang on.. rerolling the dice") 
                    # new_numbers_saved = [random.randint(1, 6) for i in dice_number_randomize]
                    new_numbers_saved = []
                    for i in dice_number_randomize:
                        new_numbers_saved.append(rand.randint(1,6))
                        # go through each number and randomize it from 1-6
                    print(new_numbers_saved)
                    x = [int(input("What are your new numbers? \n > "))]
                    
                    # self.numbers_saved(x)
                    remove_from_list(x, new_numbers_saved)
                    print(new_numbers_saved)

        else:
            print("FARKLE")

def remove_from_list(changednum, randomnum):
        # print("I am working!")
        # print(changednum, randomnum)
        for num in changednum: # goes through user array
            randomnum.remove(num) # removes values that match with user array
        return randomnum




                    # if x is not 5 or 1:
                    #     print("Farkle!")
                    #     while (dice_number_randomize): #while the array has numbers
                    #         for i in dice_number_randomize:
                    #             dice_number_randomize.remove(i) #step in and remove each number
                    #             self.roll()     
# self.roll() #then roll again
        
        # print(change_to_number)# This was just to make sure that everything was append.
        # TODO: Add number of rounds implementation
        # TODO: Add banking functionality

# #depending on if they win or lose!!
# def win_or_lose(self):  # Our method to check if user acheieved points
#         print("Called function!")
#         while(self.game_done):  # This is set to false because we are not sure if game is done
#             # if the final score is equal to the banked score, the user will win!
#             if(self.points_to_be_scored == bank_score):
#                 # you won message
#                 print("You won! Would you like to play again? \n yes or no")
#                 response = input(" > ")
#                 if response == "yes":
#                     print("Great!")
#                 elif response == "no":
#                     print("Thanks for playing!")
#                     self.game_done = False
#             elif self.points_to_be_scored != bank_score:
#                 print("You Lost!")
#                 self.game_done = False


# TODO: Implement the while loop to start and play game, user can type 'q' at anytime to quit the game
game_is_starting = True
play_game = play_game()
