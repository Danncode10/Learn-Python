row1 = ["▫️","▫️","▫️"]
row2 = ["▫️","▫️","▫️"]
row3 = ["▫️","▫️","▫️"]

board = [row1,row2,row3]

print(f"\t 1     2     3")
print(f"1\t{row1}\n2\t{row2}\n3\t{row3}")

pos = str(input("Enter Position : "))

cols = int(pos[0])
rows = int(pos[1])

board[rows-1][cols-1] = "X"


print(f"\t 1     2     3")
print(f"1\t{row1}\n2\t{row2}\n3\t{row3}")











