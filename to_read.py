print("===== MANA TO-READ PROGRAMMA =====")

books = [
    ["Fourth Wing", "nav izlasīta"],
    ["Dune", "izlasīta"],
    ["After", "nav izlasīta"]
]

print()
print("1. Parādīt grāmatas")
print("2. Pievienot grāmatu")
print("3. Atzīmēt kā izlasītu")
print("4. Iziet")

choice = input("Izvēlies darbību: ")

if choice == "1":
    for i in (len(books)):
        print(i + 1, "-", books[i][0], "-", books[i][1])
elif choice == "2":
    new_book = input("Ievadi grāmatas nosaukumu: ")
    books.append([new_book, "nav izlasīta"])
    print("Grāmata pievienota!")
    print("Pievienotā grāmata:", new_book)
elif choice == "3":
    book_number = int(input("Kuras grāmatas numuru atzīmēt kā izlasītu? "))
    books[book_number - 1][1] = "izlasīta"
    print("Grāmata atzīmēta kā izlasīta!")