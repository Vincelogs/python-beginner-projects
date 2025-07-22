# login_system.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, input_username, input_password):
        return self.username == input_username and self.password == input_password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_all_users(self, users_list):
        print("\n📋 Registered Users:")
        for user in users_list:
            print(f"- {user.username}")

# App runner
users = [
    User("james", "1234"),
    User("lucy", "pass"),
    Admin("vincent_admin", "adminpass")
]

print("=== Login System ===")
username = input("Username: ")
password = input("Password: ")

logged_in = False

for user in users:
    if user.login(username, password):
        print(f"\n✅ Welcome, {user.username}!")

        if isinstance(user, Admin):
            user.view_all_users(users)
        else:
            print("You have standard user access.")

        logged_in = True
        break

if not logged_in:
    print("❌ Invalid username or password.")
