print("===== MANA TO-READ PROGRAMMA =====")

books = [
    ["Fourth Wing", "nav izlasīta"],
    ["Dune", "izlasīta"],
    ["After", "nav izlasīta"]
]

print()
print("1. Parādīt grāmatas")
print("2. Pievienot grāmatu")
print("3. Iziet")

choice = input("Izvēlies darbību: ")

if choice == "1":
    for book in books:
        print("-", book[0], "-", book[1])
elif choice == "2":
    new_book = input("Ievadi grāmatas nosaukumu: ")
    books.append([new_book, "nav izlasīta"])
    print("Grāmata pievienota!")
    print("Pievienotā grāmata:", new_book)