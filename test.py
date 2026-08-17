from models import Forward, Midfielder, Goalkeeper

# checks a forward can be created with the right name
def test_create_forward():
    player = Forward("Kylian Mbappe", "9", "Captain", "mbappe@realmadridfc.co.uk")
    assert player.name == "Kylian Mbappe"

# checks scoring a goal increases the goal count
def test_score_goal():
    player = Forward("Kylian Mbappe", "9", "Captain", "mbappe@realmadridfc.co.uk")
    player.score_goal()
    assert player.goals_scored == 1

# checks making an assist increases the assist count
def test_make_assist():
    player = Midfielder("Kevin Debruyne", "17", "Starting XI", "debruyne@napolifc.co.uk")
    player.make_assist()
    assert player.assists == 1

# checks keeping a clean sheet increases the clean sheet count
def test_clean_sheet():
    player = Goalkeeper("Manuel Neuer", "1", "Vice-Captain", "neuer@bayernmunichfc.co.uk")
    player.keep_clean_sheet()
    assert player.clean_sheets == 1

# checks promoting a player moves them up a status
def test_promote():
    player = Midfielder("Paul Pogba", "6", "Rotation Player", "pogba@acmonacofc.co.uk")
    player.promote()
    assert player.status == "Starting XI"

# checks a stat can be set directly, not just incremented
def test_set_stat():
    player = Forward("Kylian Mbappe", "9", "Captain", "mbappe@realmadridfc.co.uk")
    player.set_stat(20)
    assert player.goals_scored == 20