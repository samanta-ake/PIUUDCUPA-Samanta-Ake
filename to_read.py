print("================================")
print("      MANA TO-READ PROGRAMMA")
print("================================")
print("Grāmatu saraksts")
# Gramatu saraksts ar nosaukumu un lasisanas statusu
books = [
    ["Fourth Wing", "nav izlasīta"],
    ["Dune", "izlasīta"],
    ["After", "nav izlasīta"]
]

print()
print("===== IZVĒLNE =====")
print("1. Parādīt grāmatas")
print("2. Pievienot grāmatu")
print("3. Atzīmēt kā izlasītu")
print("4. Dzēst grāmatu")
print("5. Iziet")

choice = input("Izvēlies darbību: ")

if choice == "1":
    if len(books) == 0:
        print("Grāmatu saraksts ir tukšs!")
    else:
        for i in range(len(books)):
            print(i + 1, "-", books[i][0], "-", books[i][1])
elif choice == "2":
    new_book = input("Ievadi jaunās grāmatas nosaukumu: ")

    if new_book.strip() == "":
        print("Grāmatas nosaukums nav ievadīts!")
    else:
        books.append([new_book, "nav izlasīta"])
        print("Grāmata veiksmīgi pievienota!")
elif choice == "3":
    book_number = int(input("Kuras grāmatas numuru atzīmēt kā izlasītu? "))

    if book_number >= 1 and book_number <= len(books):
        books[book_number - 1][1] = "izlasīta"
        print("Grāmata atzīmēta kā izlasīta!")
    else:
        print("Tādas grāmatas nav!")
elif choice == "4":
    book_number = int(input("Kuras grāmatas numuru dzēst? "))

    if book_number >= 1 and book_number <= len(books):
        books.pop(book_number - 1)
        print("Grāmata izdzēsta no saraksta!")
    else:
        print("Tādas grāmatas nav!")
elif choice == "5":
    print("Programma beidzas.")
else:
    print("Nepareiza izvēle!")