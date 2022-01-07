### Simple Rock Paper Scissors by Benjamin J.

# Import required modules
import random

print("This is random luck rock paper scissors game")

# Add wins and losses counters
wins = 0
losses = 0

while True:
    # Make initial "val" value for the while loop.
    val = ""
    while val != True:
        inp = input("Choose Rock, Paper, Scissor or stats to show stats: ").lower()
        
        # Check that input is valid with try, except and a dict.
        a = {"rock":True, "paper":True, "scissor":True, "stats":0}
        try:
            val = a[inp]
            if val == 0:
                # Print stats if input is stats and go through the while loop again
                print(f"You have won {wins} time(s) and lost {losses} time(s) this session!\n")
        except Exception as e:
            # Print exception if "inp" isnt rock, paper, scissor or stats.
            print("Invalid input")

    # Generate a random number
    res = random.randint(1, 3)
    # Turn that number into something meaningful.
    rps = {1:"rock", 2:"paper", 3:"scissor"}
    res = rps[res]
    
    # Make win conditions
    win = {"rock":"paper", "paper":"scissor", "scissor":"rock"}

    if res == win[inp]:
        # Print lose screen and add 1 to losses.
        print(f"You lose, I chose {res.capitalize()}!\n")
        losses+=1
    elif res == inp:
        # Print tie screen.
        print(f"It's a tie! We both chose {res.capitalize()}.\n")
    else:
        # Print win screen and add 1 to wins.
        print(f"You win, I chose {res.capitalize()} :(\n")
        wins+=1
