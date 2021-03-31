#!/usr/bin/env python3
round = 0           # integer round initated to 0
answer = " "

while round < 3 and answer.lower() != "brian" and answer.lower() != "shrubbery":
    round += 1  #increase round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s the Life of ______": ')
    if answer.lower() == "brian": # logic to check if user gave correct answer
        print('Correct')
    elif answer.lower() == "shrubbery": # logic to check if user gave super secret answer
        print('You save the super secret answer!')
    elif round == 3:      # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry! Try again!")
