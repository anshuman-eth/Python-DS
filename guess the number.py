n=18

print("Hi there! We are playing a game of guessing the number.\nYou will get total 9 chances to guess the number.\n")
x=9
for i in range(0,11):
    x=x-1
    print("Let's  Guess a number.")
    g=int(input())
    print("Chance remaining is:",x)
    if x==0:
        print("You lost mf.")
        break
    elif g>100:
        print("opps you are too far from the number, try with lower one.")
        continue
    elif g>50:
        print("opps you are few far from the number, try with lower one.")
        continue
    elif g>25:
        print("You are close, try with another lower one.")
        continue
    elif g>18:
        print("You are just little close, try with another lower one.")
        continue
    elif g < -100:
        print("opps you have entered very high negative number, try with lower one.")
        continue
    elif g<2:
        print("opps you are far from the number, try with higher one.")
        continue
    elif g<8:
        print("opps you are far from the number, try with higher one.")
        continue
    elif g<18:
        print("You are just little close, try with another higher one.")
        continue
    
    elif g==18:
        print("Congratulations you won the game. Kudos to you. You completed it in",9-x,"chances")
        break

    