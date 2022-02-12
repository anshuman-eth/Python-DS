def search_engine(lst,m):
    n=m.lower()
    for i in lst:
        if n in i:
            print("Yes")


if __name__=="__main__":
    m=input("Enter a string to search from database:")
    lst=["This is good", "python is good", "python is not python snake", "python is high level language"]
    search_engine(lst,m)