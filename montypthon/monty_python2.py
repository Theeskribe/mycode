#!/usr/bin/env python3
round = 0           # integer round initated to 0
while True:         # sets up an infinite
    round = round + 1
    print('Finish the movie title, "Monty Python\'s the Life of ______"')
    answer = input("Your guess--> ")

    if answer == 'Brian':
        print('Correct')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
