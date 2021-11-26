import random
# from Game import play_game
from collections import Counter

turn_not_over = True


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

total_points = int(16)
class GameLogic:
    def __init__(self):
        self.rounds_left = 6
        

    # tuple of integers passed in here.
    def calculate_score(self, *user_array):
        
        total_score = 0
        number_count = Counter(*user_array)
        for num, count in number_count.items():
            # print(num, count)
            if num == 5 and count < 6:
                total_score += count * 50
                # print("I am running!")

                # print(self.total_points)
            elif num == 1 and count < 6:
                total_score += count * 100
                # print("I am running!")

            elif num == 4:
                total_score += 1 * 1000    # print(self.total_points)
                # print("I am running!")

            elif count == 5:
                total_score += 1 * 2000
                # print("I am running!")

            elif count == 6:
               total_score += 1 * 3000
                # print("I am running!")
        #  self.total_points += die_score
        print(f" Your score is being calculated...\n > {total_score}")
        
        
        
        
    # def number_validation(self, random_dice, user_arr):
       
    #     print("\n\n\n")
    #     print(random_dice)
    #     print(user_arr)
    #     print(self.total_points)

        
        
        # self.calculate_score(*user_arr)
        # # TODO: 1. we want to both arrays and step through them.
        # new_list = list(set(dices).intersection(user_arr))
        # print(new_list)
        # count_number = Counter([*new_list])
        # for arr, count in count_number.items():
        #     # FIXME: We have the matches, how can we ensure the count of values?
        #     print(arr, count)

        # count_random_numbers = Counter([*dices])
        # for arr, count in count_random_numbers.items():
        #     random_nums = {arr:count}

        # count_user_arr_numbers = Counter([*user_arr])
        # for arr, count in count_user_arr_numbers.items():
        #         print(arr, count)

        # Lookup: map: key/value pairs

        # TODO: 2. We want to check if the numbers from the user matches with the numbers and the count of numbers of the random array
        # TODO: 3 If True, continue with scoring / If False, then return an error


gamelogic = GameLogic()
# game_one.calculate_score()

# 3. If the user has a 1 or 5 in list of 6, continue as follows:
# 1 -100 points
# 5 - 50 points
# score is added to current score list
# 3B. else if user has triples, quadruples, quintuples, or sextuplets of any other values ranging from 1-6 --> add appropiate score to user score list.
# Jerrod- we're gonna need a scorekeeper.

# 6. On 6th roll of dice, if user has either a 1 or 5 on dice roll, The user can roll again with points accumulated / If user does NOT get 1 or 5,
# ALL points not banked (saved) are lost and game ends (YOU LOST).
# 7. User input if game lost: " GAME OVER. Would you like to play again?" ---> If user types yes, start game over / if user types no, give total score of banked points (if any).

# ------------- Bank (save) points -------------------
# 8. Input: User is asked if they want to bank the points or reroll the dice
# 9. If user enters bank points, the points are saved to banked points / If user presses roll dice, no points are saved to bank

# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned
# whereas we can change the elements of a list.
