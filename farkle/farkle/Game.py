import random

from game_logic import GameLogic
from game_logic import bankedpoints

# print("This is to test the rooling that you may get")
rand = random.Random()
dice_number = [1, 2, 3, 4, 5, 6]  # this is my array of dice
dice_number_randomize = []  # this is what I'm using to show the number.
change_to_number = []  # variable set
placeholder_points = 0



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
        self.roll()  # roll the dice!
        while start_round:  # this is true
            numbers = input(" > ")  # they can input numbers
            if numbers == "q":  # however, if they type q or quit..
                start_round = False  # this loop will return false
            else:
                self.numbers_saved(numbers)
        # 2. dice rolls with 6 random values (range from 1-6)
        # 3. user enters values

    # Inside of this method, we have our saved numbers from user pick, and calculate score
    def numbers_saved(self, num):
        # split the numebrs entered by the comma
        split_the_numbers = num.split(",")
        # change_to_number = []  # set em' in an array
        for i in split_the_numbers:  # loop through the numbers we got from user
            # as we place the numbers in the array we change each one to a vaild intger
            change_to_number.append(int(i))   
        # call that funcation NV that we had in Gl pass that in.

        ##====Calculating the score=======##
        # calling from our GameLogic file, we want to calculate our score
        GameLogic.calculate_score(self, change_to_number)
        if (GameLogic.calculate_score):  # If this is true
            remove_from_list(change_to_number, dice_number_randomize)
            print(dice_number_randomize)  # print our new dice
            # ask to reroll or bank points
            still_rolling = True
            while (still_rolling):
                response = input(
                "Type (r)oll to reroll the dice, or(b)ank to bank your points \n > ")

                if response == "b":
                    print("Okay! Banking points...")
                    print("Here are your banked points!!")
                    # print(self.total_points)
                    bankedpoints.bank()
                # Bank_points.bank_the_users_points(calculate_score.total_points)

                elif response == "r":

                    print("hang on.. rerolling the dice")
                # change_to_number.clear()
                
                # new_numbers_saved = [random.randint(1, 6) for i in dice_number_randomize]
                    new_numbers_saved = []
                    for i in dice_number_randomize:
                        new_numbers_saved.append(rand.randint(1, 6))
                        # go through each number and randomize it from 1-6
                    if 1 in new_numbers_saved or 5 in new_numbers_saved:

                        print(new_numbers_saved)
                        change_to_number.clear()
                        x = input("What are your new numbers? \n > ")
                        # remove_from_list(x, new_numbers_saved)
                        split_the_numbers = x.split(",")
            # change_to_number = []  # set em' in an array
                        for i in split_the_numbers:  # loop through the numbers we got from user
                # as we place the numbers in the array we change each one to a vaild intger
                            change_to_number.append(int(i))
                            print(change_to_number)
                            GameLogic.calculate_score(self, change_to_number)
                    else:
                        still_rolling = False
                        print(new_numbers_saved)
                        print("FARKLE!")
                        print(f"Your total points are {placeholder_points}")


def remove_from_list(changednum, randomnum):
    # print("I am working!")
    # print(changednum, randomnum)

    for num in changednum:  # goes through user array
        randomnum.remove(num)  # removes values that match with user array
    return randomnum


# TODO: Implement the while loop to start and play game, user can type 'q' at anytime to quit the game
game_is_starting = True
play_game = play_game()
# dice_number_randomize
# for i in change_to_number: # we loop through the numbers in the array from user
#     if not i in change_to_number:
#         print("FARKLE")
#     else:
#         dice_number_randomize.remove(i) # we remove from the original array each number the user enters
#     # FIXME: 1 OR 5 PRESENT A VALUEERROR: ValueError: list.remove(x): x not in list
