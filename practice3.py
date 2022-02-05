import random

def guess(a,b):
    r=random.randint(a,b)
    s=random.randint(a,b)
    l=0
    m=0
    print(f"Please guess the number between {a} and {b}.\n")
    while True:
        l=l+1
        print("Player 1 ready!")
        n=int(input("Enter a nubmer:"))
        if n>b and n<a:
            print("Lol you entered a number out of the range.\n Try again!")
        elif n<r:
            print("Wrong guess, try with a bigger number again.")
        elif n>r:
            print("Wrong guess, try wilth a lower number again.")
        elif n==r:
            print(f"Correct..\nyou took {l} trials to guess the number.")
            print()
            break

    print("Player 2 ready!")
    while True:
        m=m+1
        n1=int(input("Enter a nubmer:"))
        if n1>b and n1<a:
            print("Lol you entered a number out of the range.\n Try again!")
        elif n1<s:
            print("Wrong guess, try with a bigger number again.")
        elif n1>s:
            print("Wrong guess, try with a lower number again.")
        elif n1==s:
            print(f"Correct..\nyou took {m} trials to guess the number.")
            print()
            break

    if l>m:
        print("Player 2 wins this game. Congrats.")
    elif l==m:
        print("OPPS. It's a draw. you can play this game again.:)")
    else:
        print("Player 1 wins this game. Congrates.")


if __name__=="__main__":
    print()
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    guess(a,b)