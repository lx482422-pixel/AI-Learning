x = float(input("what's your score"))
if 0 <= x <= 100:
    if x >= 90:
        score = "A"
    elif x >= 80:
        score = "B"
    elif x >= 60:
        score = "c"
    else:
        score = "F"
    print(f"your score is {x} and your grade is {score}")
else:
    print("wrong")