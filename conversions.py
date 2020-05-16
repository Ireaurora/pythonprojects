def initial():
    initial_unit = str(input("Enter the unit you currently have"))
    final_unit = str(input("Enter the unit you want to get"))
    if initial_unit == "stones" and final_unit == "kg":
        print(from_stones_to_kg(int(input("Enter the amount"))))
    elif initial_unit == "pounds" and final_unit == "kg":
        print(from_pounds_to_kg(int(input("Enter the amount"))))
    elif initial_unit == "kg" and final_unit == "stones":
        print(from_kg_to_stones(int(input("Enter the amount"))))
    elif initial_unit == "kg" and final_unit == "pounds":
        print(from_kg_to_pounds(int(input("Enter the amount"))))
    else:
        False

def from_stones_to_kg(stones):
    if stones != 0:
        newweight = stones * 6.35029
        return "You had " + str(stones) + " stones. Now you have " + str(newweight) + "kg"
    else:
        return 0

def from_pounds_to_kg(pounds):
    if pounds != 0:
        newweight = pounds * 0.453592
        return "You had " + str(pounds) + " pounds. Now you have " + str(newweight) + "kg"
    else:
        return 0

def from_kg_to_stones(kg):
    if kg != 0:
        newweight = kg / 6.35029
        return "You had " + str(kg) + "kg. Now you have " + str(newweight) + " stones"
    else:
        return 0

def from_kg_to_pounds(kg):
    if kg != 0:
        newweight = kg / 0.453592
        return "You had " + str(kg) + "kg. Now you have " + str(newweight) + " pounds"
    else:
        return 0

initial()
