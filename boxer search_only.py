name = input("Enter boxer's name to search: ")

found = False
try:
    with open("boxer.txt", "r") as file:
        for line in file:
            if name.lower() in line.lower():
                print("✅ Boxer Found:", line.strip())
                found = True
                break
    if not found:
        print("❌ Boxer not found.")
except FileNotFoundError:
    print("⚠️ boxer.txt not found.")
