def add_details(players):
    name = input("Enter Player Name:")
    phone = input("Enter Player name:")
    email = input("enter Player e4mail")
    players[name] = {'phone': phone, 'email': email}
    print(f"Name of {name} added.")

def view_platers(players):
    if players: 
        for name, details in players.items():
            print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("no player found.")

add_details(players)
view_contacts(players)