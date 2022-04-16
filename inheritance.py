class User:
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for ths page.")
new_user = User()
new_user.login()

def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account

class Team:
    name = "teamName"
    city = "teamCity"
    roster = ["player1", "player2", "player3"]
    year_founded = 0
    coach = "coachName"

class Warriors(Team):
    name = "Golden State Warriors"
    sport = "basketball"
    playing_site = "Oracle Arena"

class Buccaneers(Team):
    name = "Tampa Bay Buccaneers"
    championships = 2
    contact_sport = True
