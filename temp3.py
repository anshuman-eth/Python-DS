def searcher():
    import time
    #some 4 second time consuming task
    book="This is a book on code with harry"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Your text is not in the book.")


search=searcher()
print("Search Started")
next(search)
print("Next method run")
search.send("harry")
input("Press any key:")
search.send("code")
search.close()