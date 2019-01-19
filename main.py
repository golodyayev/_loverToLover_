import random
from class2 import COUPLE_DF,questions

couple = COUPLE_DF()
question = questions()
while True:
    time = random.random()
    if time > 0.9999:

        couple.read()

        couples = couple.get_couple()
        question.append(couples)


        for i in range(len(couples)):
            print("Send task #XXXXXX to {} ".format(couples.iloc[i][0]))