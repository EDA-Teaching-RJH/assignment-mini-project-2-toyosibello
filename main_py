from models import Forward, Midfielder, Goalkeeper, VALID_STATUSES
from file_io import save_squad_csv, load_squad_csv, append_match_event, read_match_events

# a few starter players so there's something to look at straight away
def seed_demo_squad():
    return [
        Forward("Joao Pedro", "9", "Vice-Captain",
                "joaopedro@chelseafc.co.uk", goals_scored=14, team="Chelsea"),
        Midfielder("Cole Palmer", "20", "Starting XI",
                    "palmer@chelseafc.co.uk", assists=9, team="Chelsea"),
        Goalkeeper("Robert Sanchez", "1", "Starting XI",
                    "sanchez@chelseafc.co.uk", clean_sheets=11, team="Chelsea"),
        Midfielder("Moises Caicedo", "25", "Starting XI",
                    "caicedo@chelseafc.co.uk", assists=3, team="Chelsea"),
    ]

# A Squad management menu
def print_menu():
    print("""
==== Chelsea Squad Management System ====
1. List squad (A-Z)
2. Add player
3. Promote a player's status
4. Log a match event
5. View match log
6. Edit a player's stats
7. Save & Quit
""")

 # prints every player, sorted alphabetically by name
def list_squad(squad_list):
    # sort by name
    for player in sorted(squad_list, key=lambda p: p.name):
        print(f"  {player}")

# asks for player details and adds them to the squad
def add_player(squad_list):
    print("\nPositions: 1) Forward  2) Midfielder  3) Goalkeeper")
    choice = input("Choose position (1-3): ").strip()
    name = input("Name: ").strip()
    number = input("Player Number (shirt number, e.g. 9): ").strip()
    print(f"Statuses: {', '.join(VALID_STATUSES)}")
    status = input("Status: ").strip()
    email = input("Email: ").strip()

    # check the number isn't already taken
    if number in [p.number for p in squad_list]:
        print(f"Could not add player: number {number} is already taken.")
        return

    try:
        if choice == "1":
            player = Forward(name, number, status, email)
        elif choice == "2":
            player = Midfielder(name, number, status, email)
        elif choice == "3":
            player = Goalkeeper(name, number, status, email)
        else:
            print("That's not a valid position choice, player not added.")
            return
        squad_list.append(player)
        print(f"Added: {player}")
    except ValueError as e:
        print(f"Could not add player: {e}")

# moves a player up one squad status
def promote_player(squad_list):
    number = input("Player Number to promote: ").strip()
    for player in squad_list:
        if player.number == number:
            new_status = player.promote()
            print(f"{player.name} is now a {new_status}.")
            return
    print("Couldn't find a player with that number.")

# adds an event to the match log
def log_match_event(squad_list):
    number = input("Player Number: ").strip()
    if number not in [p.number for p in squad_list]:
        print("Don't recognise that player number, but I'll log it anyway.")
    minute = input("Minute (e.g. 34): ").strip()
    event = input("What happened: ").strip()
    append_match_event(number, minute, event)
    print(f"Logged at minute {minute}'.")

# prints every logged match event
def view_match_log():
    events = read_match_events()
    if not events:
        print("No match events logged yet.")
        return
    for entry in events:
        print(f"  [{entry['minute']}'] #{entry['number']}: {entry['event']}")

# lets you directly set a player's stat (goals/assists/clean sheets)
def edit_player_stats(squad_list):
    number = input("Player Number: ").strip()
    for player in squad_list:
        if player.number == number:
            current_stat = player.to_dict()["stat"]
            print(f"{player.name}'s current stat is {current_stat}.")
            new_value = input("New value: ").strip()
            try:
                # int() fails on non-numbers, so catch it here
                player.set_stat(int(new_value))
                print(f"Updated: {player}")
            except ValueError:
                print("That's not a valid number, stat not changed.")
            return
    print("Couldn't find a player with that number.")

# main menu loop
def main():
    squad_list = load_squad_csv()
    if not squad_list:
        # empty list counts as falsy, so this only runs if nothing loaded
        squad_list = seed_demo_squad()
        print("No saved squad found, starting with the demo squad.")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            list_squad(squad_list)
        elif choice == "2":
            add_player(squad_list)
        elif choice == "3":
            promote_player(squad_list)
        elif choice == "4":
            log_match_event(squad_list)
        elif choice == "5":
            view_match_log()
        elif choice == "6":
            edit_player_stats(squad_list)
        elif choice == "7":
            save_squad_csv(squad_list)
            print("Squad saved. See you at the next match.")
            break
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()