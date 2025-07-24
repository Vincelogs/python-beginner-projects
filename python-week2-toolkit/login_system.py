class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

class Admin(User):
    def view_users(self, users):
        print("\nRegistered Users:")
        for user in users:
            print(f"- {user.username}")

users = [
    User("james", "1234"),
    User("lucy", "pass"),
    Admin("vincent_admin", "adminpass")
]

username = input("Username: ")
password = input("Password: ")

logged_in = False
for user in users:
    if user.login(username, password):
        print(f"\nWelcome, {user.username}!")
        if isinstance(user, Admin):
            user.view_users(users)
        else:
            print("Standard user access.")
        logged_in = True
        break

if not logged_in:
    print("Invalid credentials.")