year = int(input("Enter Year: "))
isLeap = False

running = ""

# while(not(running == "q")):
#     if(year % 4 == 0):
#         if(year % 100 == 0):
#             if(year % 400 == 0):
#                 isLeap = True
#             else:
#                 isLeap = False
#         else:       
#             isLeap = True 
#     else:
#         isLeap = False

#     #Print

#     if(isLeap == True):
#         print("It is Leap Year.")
#     else:
#         print("It is not a Leap Year.")
        
#     running = str(input("Type any key to continue or press 'q' to quit: "))
    
    
    #Answer:
    
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")