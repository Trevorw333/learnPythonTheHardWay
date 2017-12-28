import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber ==2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber ==4:
        return "I wish python had switch statements"
    elif answerNumber ==5:
        return "You get the idea"
    elif answerNumber ==6:
        return "last one"

r = random.randint(1,6)
fortune = getAnswer(r)
print(fortune)