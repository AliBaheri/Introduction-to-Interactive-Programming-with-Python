import random
def number_to_name(number):
    if   number == 0: return "rock"
    elif number == 1: return "Spock"
    elif number == 2: return "paper"
    elif number == 3: return "lizard"
    elif number == 4: return "scissors"
    else: return None

def name_to_number(name):
    if name == "rock":     return 0
    elif name == "Spock":  return 1
    elif name == "paper":  return 2
    elif name == "lizard": return 3
    elif name == "scissors":return 4
    else: return None

def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    score = (player_number - comp_number) % 5

    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number)

    #print "Score was:", difference # XXX

    if   score == 0: print "Player and computer tie!"
    elif score <= 2: print "Player wins!"
    else: print "Computer wins!"

    print
    
rpsls("paper")
rpsls("lizard")

