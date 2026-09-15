print("===== MANA TO-READ PROGRAMMA =====")

books = [
    ["Fourth Wing", "nav izlasīta"],
    ["Dune", "izlasīta"],
    ["After", "nav izlasīta"]
]

print()
print("1. Parādīt grāmatas")
print("2. Iziet")

choice = input("Izvēlies darbību: ")

if choice == "1":
    for book in books:
        print("-", book[0], "-", book[1])
elif choice == "2":
    print("Programma beidzas.")