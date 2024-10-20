import random

humanChoice = str(input("Enter (r-rock,p-paper,s-scissor): "))
computerChoice = random.randint(0,2)

if(computerChoice == 0):
    computerChoice = str("rock")
elif(computerChoice == 1):
    computerChoice = str("paper")
else:
    computerChoice = str("scissor")
    

if(humanChoice == "r"):
    humanChoice = "rock"
    if(computerChoice == "paper"):
        print(f"You Lose\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    elif(computerChoice == "rock"):
         print(f"Its a Tie\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    else:#scissor
         print(f"You Win\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    
elif(humanChoice == "p"):
    humanChoice = "paper"
    if(computerChoice == "paper"):
        print(f"Its a Tie\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    elif(computerChoice == "rock"):
         print(f"You Win\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    else:#scissor
         print(f"You Lose\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")

else: #scissors
    humanChoice = "scissor"
    if(computerChoice == "paper"):
        print(f"You Win\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    elif(computerChoice == "rock"):
         print(f"You Lose\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
    else:#scissor
         print(f"Its a Tie\n\nYour Choice: {humanChoice}\nComputer Choice: {computerChoice}")
