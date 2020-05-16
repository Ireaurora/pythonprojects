from random import randint

question = str(input("Should I roll the dice?"))

def roll():
    if question == "yes":
        return "First dice : " +str(randint(0, 6))  + "\nSecond dice : "  + str(randint(0, 6))
    else:
        return "Okay :("
    
print(roll())
