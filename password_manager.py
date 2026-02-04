from cryptography.fernet import Fernet
import os


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("New encryption key generated and saved as 'key.key'")
    return key


def load_key():
    key_path = "key.key"
    if not os.path.exists(key_path):
        print("No key found. Generating a new one...")
        return generate_key()
    
    with open(key_path, "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
fer = Fernet(key)

MASTER_PASSWORD = "secret9@z+123?"


def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords file found yet.")
        return

    try:
        with open('passwords.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    user, encrypted_pwd = line.split("|", 1)
                    decrypted = fer.decrypt(encrypted_pwd.encode()).decode()
                    print(f"User: {user:<20} | Password: {decrypted}")
                except Exception as e:
                    print(f"Error decrypting line: {line!r} → {e}")
    except Exception as e:
        print(f"Error reading passwords file: {e}")


def add():
    name = input("Account Name: ").strip()
    if not name:
        print("Account name cannot be empty.")
        return

    pwd = input("Password: ").strip()
    if not pwd:
        print("Password cannot be empty.")
        return

    encrypted = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted}\n")
    
    print(f"→ Password for '{name}' saved successfully.")


print("Simple Password Manager")
print("───────────────────────")

master_pwd = input("What is the master password? ").strip()

if master_pwd != MASTER_PASSWORD:
    print("Incorrect master password. Exiting.")
    exit()

print("Access granted.\n")

while True:
    mode = input("Add new password, view existing ones or quit? (add / view / q): ").strip().lower()
    
    if mode in ('q', 'quit', 'exit'):
        print("Goodbye!")
        break
    
    elif mode == "view":
        view()
    
    elif mode == "add":
        add()
    
    else:
        print("Invalid choice. Use: add, view, or q")