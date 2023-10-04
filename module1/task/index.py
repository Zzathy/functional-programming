books = [{"title": "Python", "borrowed": None}, {"title": "PHP", "borrowed": None}]
users = ["Izza", "Fathony"]

def inputBook(title):
    book = {"title": title, "borrowed": None}
    books.append(book)
    print(book["title"], "successfully added")

def listBook():
    print("List of books available :")
    for i in range(len(books)):
        print(i + 1, ".", books[i]["title"], ", Borrowed :", books[i]["borrowed"])

def borrowBook(user):
    if not books:
        print("There are no books available to borrow")
        return

    listBook()

    numberBook = int(input("Choose Book : ")) - 1

    if numberBook < len(books):
        if books[numberBook]["borrowed"] is None:
            books[numberBook]["borrowed"] = users[user - 1]
            print("You have borrowed a book", books[numberBook]["title"])
        else:
            print(books[numberBook]["title"], "is still borrowed")
    else:
        print("Book not found")
    
def returnBook(user):
    if not books:
        print("There are no books available to return")
        return
    
    listBook()

    numberBook = int(input("Choose Book : ")) - 1

    if numberBook < len(books):
        if books[numberBook]["borrowed"] is users[user - 1]:
            books[numberBook]["borrowed"] = None
            print("You have returned a book", books[numberBook]["title"])
        else:
            print("You dont have this book", books[numberBook]["title"])
    else:
        print("Book not found")

def main():
    while True:
        print("1. Admin\n2. User\n3. Exit")

        role = input("Input Role : ")

        if role == "1":
            print("What do you want to do?")
            print("1. Input Book\n2. Exit")
            choose = input("Choose : ")
            if choose == "1":
                inputBook(input("Book name : "))
        elif role == "2":
            print("User list:")
            for i in range(len(users)):
                print(i + 1, ".", users[i])
            user = int(input("Choose : "))
            print("What do you want to do?")
            print("1. Borrow Book\n2. Return Book\n3. Exit")
            choose = input("Choose : ")
            if choose == "1":
                borrowBook(user)
            elif choose == "2":
                returnBook(user)
        elif role == "3":
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()