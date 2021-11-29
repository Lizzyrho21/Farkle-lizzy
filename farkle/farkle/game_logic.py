import random
# from Game import play_game
from collections import Counter

turn_not_over = True
#FIXME: #Bug in bank_points add wrong numbers 
# print("lizzy-branch") #lizzy-branch!


# -----------Start Of Farkle Game / Farkle logic -------------------
# 1.  if user enters yes (play game), the dice rolls /  if the user enters no (don't play game), the game ends and final score is 0.

points_banked = 0

# total_points = 0

dice = []

# dice_tuples = (1, 2, 3, 4, 5, 6)  # Tuples of numbers for dice roll


# 2. The dice rolls, and 6 Values ranging from 1-6 are presented, user has 6 tries to get points

#             print(self.total_points)
# FIXME: fix total score to add correct score for user
# TODO: Add banker class
# TODO: Add rounds left for user
global final_points
final_points = 0


total_points = int(16)
class GameLogic:
    def __init__(self, total_points):
        self.total_points = total_points
        
        

    # tuple of integers passed in here.
    def calculate_score(self, *user_array):
        # final_points = 20
        total_points = 0
        number_count = Counter(*user_array)
        for num, count in number_count.items():
            # print(num, count)
            if num == 5 and count < 6:
                total_points += count * 50
                # print("I am running!")

                # print(self.total_points)
            elif num == 1 and count < 6:
                total_points += count * 100
                # print("I am running!")

            elif num == 4:
                total_points += 1 * 1000    # print(self.total_points)
                # print("I am running!")

            elif count == 5:
                total_points += 1 * 2000
                # print("I am running!")

            elif count == 6:
               total_points += 1 * 3000
                # print("I am running!")
        #  self.total_points += die_score
        # total_score += total_score
        print(f" Your score is being calculated...\n > {total_points}")
        # final_points += total_score

#     Handle banking points
# Define a Banker class
class Banker(GameLogic):
    def __init__(self):
        super().__init__(total_points)
        self.banked_points = 0
       
        
    
    def bank(self):
        # self.total_points += self.banked_points
        self.banked_points += self.total_score
        print(self.banked_points)
        print(self.total_points)
        # return self.banked_points

# Add a shelf instance method
# Input to shelf is the amount of points (integer) to add to shelf.
# shelf should temporarily store unbanked points.
# Add a bank instance method
# bank should add any points on the shelf to total and reset shelf to 0.
# bank output should be the amount of points added to total from shelf.
# Add a clear_shelf instance method
# clear_shelf should remove all unbanked points.    

gamelogic = GameLogic(0)
bankedpoints = Banker()
# bankedpoints.bank(gamelogic.total_score)

# ------------- Bank (save) points -------------------
# 8. Input: User is asked if they want to bank the points or reroll the dice
# 9. If user enters bank points, the points are saved to banked points / If user presses roll dice, no points are saved to bank

# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned
# whereas we can change the elements of a list.
