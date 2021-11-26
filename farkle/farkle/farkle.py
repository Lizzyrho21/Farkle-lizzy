import random
from Game import play_game

turn_not_over = True # This specifies our entire game starts
 # This specifies the start of our round
# print("Jerrod")

# we need to ask a question that ask do you want to play a game.
while turn_not_over:
   # play_game(i)
    start_question = input("Welcome To Farkle! To start the Game type (y)es\n to quit at anytime, type (q)uit >  ") # this is a input question. 
   # print(startGame)
    if start_question.lower() == "yes" or start_question.lower() == "y" or start_question.lower() == "yea":
        # turn_not_over = False
        # while start_round: #While this is true, the round will start
        play_game.start_game()
            # start_round = False
    elif start_question.lower() == "q":
        print("exiting game...")
        turn_not_over = False

# if user enters yes roll the dice /  if the user enters no the game start at 0.
# there should be 6 Values 1-6.
# if the user has a 1 or 5.
# Jerrod- we're gonna need a scorekeeper.
# if it a 1 they get 100 points.
# if it a 5 they get 50 points.
# else user doesn't have a dice that is 1 or 5. Do user have any other occurrence.


# TO DO: Lookup random int to create dice roll
                    #-----------Start Of Farkle Game / Farkle logic -------------------
# 1.  if user enters yes (play game), the dice rolls /  if the user enters no (don't play game), the game ends and final score is 0.

points_banked = 0

total_points = 0

dice = []
# 6. On 6th roll of dice, if user has either a 1 or 5 on dice roll, The user can roll again with points accumulated / If user does NOT get 1 or 5,
# ALL points not banked (saved) are lost and game ends (YOU LOST). 
# 7. User input if game lost: " GAME OVER. Would you like to play again?" ---> If user types yes, start game over / if user types no, give total score of banked points (if any).












