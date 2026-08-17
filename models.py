import re

VALID_STATUSES = [
    "Reserve", "Squad Player", "Rotation Player",
    "Starting XI", "Vice-Captain", "Captain",
]

# basic email + shirt number checks
EMAIL_PATTERN = re.compile(r"^\S+@\S+\.\S+$")
PLAYER_NUMBER_PATTERN = re.compile(r"^([1-9][0-9]?)$")  # 1-99, no leading zero

# A base class for any player in the squad
class Player:
    def __init__(self, name, number, status, email, team="Chelsea"):
        if not name:
            raise ValueError("Missing name")

        if not re.match(PLAYER_NUMBER_PATTERN, number):
            raise ValueError(f"'{number}' doesn't look like a valid shirt number (should be 1-99)")

        if not re.match(EMAIL_PATTERN, email):
            raise ValueError(f"'{email}' doesn't look like a valid email")

        self.name = name.strip().title()
        self.number = number
        self.email = email
        self.team = team
        self._status = None
        self.status = status

    # getter for status
    @property
    def status(self):
        return self._status

    # setter, checks it's an actual valid status before allowing it
    @status.setter
    def status(self, value):
        if value not in VALID_STATUSES:
            raise ValueError(f"'{value}' is not a valid squad status")
        self._status = value

    # bump up to the next status, unless already at the top
    def promote(self):
        current_index = VALID_STATUSES.index(self._status)
        if current_index + 1 < len(VALID_STATUSES):
            self._status = VALID_STATUSES[current_index + 1]
        return self._status
    
    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "status": self.status,
            "email": self.email,
            "team": self.team,
            "role": self.__class__.__name__,
            "stat": 0  # overridden by each subclass
        }

    def __str__(self):
        return f"{self.status} #{self.number} {self.name} - {self.team}"

# forward - tracked by goals scored
class Forward(Player):
    def __init__(self, name, number, status, email, goals_scored=0, team="Chelsea"):
        # super() = run Player's __init__ first
        super().__init__(name, number, status, email, team)
        self.goals_scored = goals_scored

    def score_goal(self):
        self.goals_scored += 1
        return self.goals_scored

    def set_stat(self, value):
        self.goals_scored = value

    def to_dict(self):
        data = super().to_dict()
        data["stat"] = self.goals_scored
        return data

    def __str__(self):
        return f"{super().__str__()} - Forward, {self.goals_scored} goals"

# midfielder - tracked by assists
class Midfielder(Player):
    def __init__(self, name, number, status, email, assists=0, team="Chelsea"):
        super().__init__(name, number, status, email, team)
        self.assists = assists

    def make_assist(self):
        self.assists += 1
        return self.assists

    def set_stat(self, value):
        self.assists = value

    def to_dict(self):
        data = super().to_dict()
        data["stat"] = self.assists
        return data

    def __str__(self):
        return f"{super().__str__()} - Midfielder, {self.assists} assists"

# goalkeeper - tracked by clean sheets
class Goalkeeper(Player):
    def __init__(self, name, number, status, email, clean_sheets=0, team="Chelsea"):
        super().__init__(name, number, status, email, team)
        self.clean_sheets = clean_sheets

    def keep_clean_sheet(self):
        self.clean_sheets += 1
        return self.clean_sheets

    def set_stat(self, value):
        self.clean_sheets = value

    def to_dict(self):
        data = super().to_dict()
        data["stat"] = self.clean_sheets
        return data

    def __str__(self):
        return f"{super().__str__()} - Goalkeeper, {self.clean_sheets} clean sheets"