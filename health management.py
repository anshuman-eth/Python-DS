def lock(m):
    if m==1:
        h=int(input("Enter 1 for exercise or 2 for diet data:"))
        if h==1:
            e=input("Enter the exercise data:")
            f=open("harry_e.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        elif h==2:
            e=input("Enter the diet data:")
            f=open("harry_d.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        else:
            print("Wrong input")

    elif m==2:
        r=int(input("Enter 1 for exercise or 2 for diet data:"))
        if r==1:
            e=input("Enter the exercise data:")
            f=open("rohan_e.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        elif r==2:
            e=input("Enter the diet data:")
            f=open("rohan_d.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        else:
            print("Wrong input")
    elif m==3:
        h1=int(input("Enter 1 for exercise or 2 for diet data:"))
        print("Hammad")
        if h1==1:
            e=input("Enter the exercise data:")
            f=open("hammad_e.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        elif h1==2:
            e=input("Enter the diet data:")
            f=open("hammad_d.txt","a")
            f.write(e)
            f.write("\n")
            f.close()
            print("Data successfully added.")
        else:
            print("Wrong input")
    else:
        print("Wrong input.")

def retrive(m):
    if m==1:
        h=int(input("Enter 1 for exercise or 2 for diet data:"))
        if h==1:
            f=open("harry_e.txt")
            output=f.read()
            print("Harry's Exercise List:\n",output)
            f.close()
        elif h==2:
            f=open("harry_d.txt")
            output=f.read()
            print("Harry's Diet List:\n",output)
            f.close()
        else:
            print("Wrong input")

    elif m==2:
        r=int(input("Enter 1 for exercise or 2 for diet data:"))
        print("Rohan")
        if r==1:
            f=open("rohan_e.txt")
            output=f.read()
            print("Rohan's Exercise List:\n",output)
            f.close()
        elif r==2:
            f=open("rohan_d.txt")
            output=f.read()
            print("Rohan's Diet List:\n",output)
            f.close()
        else:
            print("Wrong input")
    elif m==3:
        h1=int(input("Enter 1 for exercise or 2 for diet data:"))
        print("Hammad")
        if h1==1:
            f=open("hammad_e.txt")
            output=f.read()
            print("Hammad's Exercise List:\n",output)
            f.close()
        elif h1==2:
            f=open("hammad_d.txt")
            output=f.read()
            print("Hammad's Diet List:\n",output)
            f.close()
        else:
            print("Wrong input")
    else:
        print("Wrong input")


n=int(input("Type 1 to lock the data  or type 2 to retrive the data:"))
if n==1:
    m=int(input("Type 1 for Harry, 2 for Rohan, 3 for hammad to lock the dataData:"))
    lock(m)
elif n==2:
    m=int(input("Type 1 for Harry, 2 for Rohan, 3 for hammad to retrive the data Data:"))
    retrive(m)

else:
    print("Wrong Input")
