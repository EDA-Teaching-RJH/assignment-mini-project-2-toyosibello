# Developer Journal - My chelsea squad management system

# Overview of what i built
I bulit a system for managing a football squad. In the system you can add any football player you want, promote their squad status, log match events and save the squad to a  CVS file. 

# How it links back to the lectures

I used some of the basics we used in the eariler lectures (2-4), to create the menu that is used in my main.py file and also used 'if'/'elif'/'else' to route each of the choices in my functions

In lecture 6 we were tought how to build up dictionaries using the captains i applied the same logic using 'to_dict()' to turn a player object into a dictionary. I also used 'try'/'except' in 'add_player()' so that the system doesn't crash if you type in a bad status or email, it judt prints out a message and lets you try again

i used the 'cvs' library for writing the roster out, using the 'captains.csv' and the 'csv.DictWriter' examples what we learned in lecture 7. In my 'test_basic.py' follows the same pattern as the 'test_square'/'test_hello' from lecture 8, using one assert for each test. file_io.py uses 'with open(...) as file:' to read and write files. 'save_squad_csv' and 'load_squad_csv' uses 'csv.DictWriter' and 'csv_DictReader' for the roster.  The 'append_match_event' and 'read_match_events' handle the splitting of the match logs.

'Player' is similar to the 'Student' form the lecture 9 but with different filed names. I validate the information in '__init__' and used 'ValueError' if there was an error. I aslo used '@property' and '@setter' for status. 'Forward', 'Midfielder', and 'Goalkeeper' all inherit from 'Player' similar to how 'Engineer' inherited from 'Student'. For the regex i used 're' to check the shirt number and email formats.

# What i struggled with

One of my biggest issues was actually finding the theme of what i was going to make this code about, I used the first ever mini project  as the inspiration for this system simlar to how we made a fleet manager using star trek as the theme i thought to do the same thing but with footall beacuse i love the sport. Another issue i struggled with was, my first email regex only allowed one dot in the domain so it kept rejecting valid email addresses. I wasn't sur why the emails were failing so i printed what the regex was matching to help find the problem then fixed the regex so it could accept domains with more than one part.