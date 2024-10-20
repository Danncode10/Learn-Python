height = [180, 124, 165, 173, 189, 169, 146]
average = 0
i = 0

for x in  height:
    i+=1
    average = round((average + x)/i,2)
    print(average)
    
print(f"\nFinal Average = {average}")