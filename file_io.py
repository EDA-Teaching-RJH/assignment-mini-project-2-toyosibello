import csv
import os

from models import Forward, Midfielder, Goalkeeper

FIELDNAMES = ["number", "name", "status", "email", "team", "role", "stat"]

# writes the whole squad out to a csv file
def save_squad_csv(squad_list, path="squad_roster.csv"):
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for player in squad_list:
            writer.writerow(player.to_dict())

# reads the csv back in and rebuilds the correct player type
def load_squad_csv(path="squad_roster.csv"):
    squad_list = []

    if not os.path.exists(path):
        return squad_list

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # csv gives everything back as text, so convert to int
            stat = int(row["stat"])
            # rebuild the right subclass based on the role column
            if row["role"] == "Forward":
                player = Forward(row["name"], row["number"], row["status"], row["email"], goals_scored=stat, team=row["team"])
            elif row["role"] == "Midfielder":
                player = Midfielder(row["name"], row["number"], row["status"], row["email"], assists=stat, team=row["team"])
            elif row["role"] == "Goalkeeper":
                player = Goalkeeper(row["name"], row["number"], row["status"], row["email"], clean_sheets=stat, team=row["team"])
            else:
                continue
            squad_list.append(player)

    return squad_list

# adds one line to the match log txt file
def append_match_event(number, minute, event, path="match_log.txt"):
    with open(path, "a") as file:
        file.write(f"{number} | {minute}' | {event}\n")

# reads the match log back in and splits each line into its parts
def read_match_events(path="match_log.txt"):
    events = []

    if not os.path.exists(path):
        return events

    with open(path) as file:
        for line in file:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            # unpacks the 3 parts straight into 3 variables
            number, minute, event = [p.strip() for p in parts]
            events.append({"number": number, "minute": minute, "event": event})

    return events