import socket

def encrypt(text, shift=3):
    return ''.join(chr(ord(c) + shift) for c in text)

def login():
    username = input("Username: ")
    password = input("Password: ")
    return {"username": username, "password": password}

def get_boxer_info():
    name = input("Boxer's Name: ")
    weight = input("Weight Class: ")
    record = input("Record (e.g., 22-1-1): ")
    return {"name": name, "weight": weight, "record": record}

def search_boxer():
    search_name = input("\nEnter the name of the boxer to look up: ")
    found = False
    try:
        with open("boxer.txt", "r") as file:
            for line in file:
                if search_name.lower() in line.lower():
                    print("✅ Boxer Found:", line.strip())
                    found = True
                    break
        if not found:
            print("❌ Boxer not found.")
    except FileNotFoundError:
        print("⚠️ boxer.txt not found.")


# --- CLIENT CONNECTION ---
client = socket.socket()
client.connect(('localhost', 9999))  # Ensure server is running on port 9999

# Step 1: Authenticate
auth = login()
auth_message = f"AUTH,{auth['username']},{auth['password']}"
client.send(encrypt(auth_message).encode())
auth_response = client.recv(1024).decode()
print("Server:", auth_response)

if "Success" not in auth_response:
    client.close()
    exit()

# Step 2: Send boxer info
while True:
    boxer = get_boxer_info()
    boxer_message = f"BOXER,{boxer['name']},{boxer['weight']},{boxer['record']}"
    client.send(encrypt(boxer_message).encode())
    response = client.recv(1024).decode()
    print("Server:", response)

    another = input("Add another boxer? (yes/no): ")
    if another.lower() != 'yes':
        break

client.close()

# Step 3: Search for a boxer
search_boxer()
