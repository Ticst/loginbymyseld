users = []
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.status = "online"

    def __str__(self):
        return self.username
        
    def CheckPassword(self,pw):
        return self.password == pw

def UserCreat():
    while True:
        username = input("Username\n>")
        password = input("Password\n>")

        new_user = User(username,password)
        users.append(new_user)

        print("new user created", new_user)

        again = input("\ndo you want to continue y/n\n>").lower()
        if again != "y":
            break

def Status():
    username = input("\nEnter username:\n> ")
    pw = input("\nEnter password:\n> ")
    found = False
    for user in users:
        if user.username == username:
            found = True
            if user.CheckPassword(pw):
                print("Correct password")
                print("Do you want to change your status y/n")
                change = input(">").lower()
                if change == "y":
                    if user.status == "online":
                        user.status = "offline"
                    else:
                        user.status = "online"
            else:
                print("Wrong password")
    if not found:
        print("User not found")

def End():
    print("\n---All Users---")
    for user in users:
        print(user.username, "-", user.password, "-", user.status)

def Commands():
    while True:
        print("\n\n-- r -- e -- d -- q --\n\n")
        firstcomm = input(">").lower()
        if firstcomm == "r":
            UserCreat()
        elif firstcomm == "e":
            End()
        elif firstcomm == "s":
            Status()
        elif firstcomm == "q":
            break
        else:
            print("not a command")

Commands()
