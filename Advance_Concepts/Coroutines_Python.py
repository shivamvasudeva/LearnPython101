def searcher(): #its a co routine
    import time
    print("5 sec time consuming task")
    book = "Its a book of 1000 pages"
    time.sleep(2)

    while True:
        text = (yield) # if i use yield the searcher func becomes coroutine
        if text in book:
            print(f"{text}: in book ")
        else:
            print(f"{text}: Text not there")

search =  searcher()
next(search)
search.send("book")
search.send("1000")
search.send("shivam")
search.send("55555")
search.close()