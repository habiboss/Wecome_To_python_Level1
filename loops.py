for x in range(5, 10):
    #if(x == 7): break
    #print(str(x) + "its a break")
    if (x % 2 == 0): continue
    print(str(x) + "continue")


days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for i,d in enumerate(days):
    print(i, d)


