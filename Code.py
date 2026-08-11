import json
import os


FILE = "passwords.json"


class PasswordManager:
    def __init__(self):
        self.passwords = self.load()

    def load(self):
        if not os.path.exists(FILE):
            return {}

        try:
            with open(FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    def save(self):
        try:
            with open(FILE, "w", encoding="utf-8") as file:
                json.dump(self.passwords, file, indent=4)
        except OSError:
            print("❌ Could not save data.")

    def add_password(self, website, username, password):
        self.passwords[website] = {
            "username": username,
            "password": password
        }
        self.save()
        print("✅ Password saved.")

    def search(self, website):
        data = self.passwords.get(website)

        if data:
            print(f"\nWebsite: {website}")
            print(f"Username: {data['username']}")
            print(f"Password: {data['password']}")
        else:
            print("❌ Password not found.")

    def delete(self, website):
        if website in self.passwords:
            del self.passwords[website]
            self.save()
            print("🗑️ Password deleted.")
        else:
            print("❌ Website not found.")


manager = PasswordManager()

while True:
    print("\n--- Password Manager ---")
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")
        manager.add_password(website, username, password)

    elif choice == "2":
        website = input("Website: ")
        manager.search(website)

    elif choice == "3":
        website = input("Website: ")
        manager.delete(website)

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice.")
