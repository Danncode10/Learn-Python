score = [178, 65, 89, 86, 55, 1000, 91, 64, 891]
highest = 0

for x in score:
    if(x > highest):
        highest = x
        
print(f"The Highest Score is {highest}")