import random

special = {'monday':'chicken', 'tuesday':'rice','wednesday':'beans',
           'thursday':'beef','friday':'omellete','saturday':'bread','sunday':'butter'}

def food_day(food):
    choose = special[food]
    for choo in choose:
        print(choo)
    #put a for loop here
    #special.remove(food)
    #print(special)


food_day("monday")

dirty = True #state of the pan
scrub_count = 0 #number of scrubs
try:
    while (dirty):
        scrub_count += 1
        print("scrub the pan{}".format(scrub_count))
        print("rinse&check if the pan is clean")
except:
    print("error")
else:
    
    if not random.randint(0, 9):
        print("All clean")
        dirty = False 
    else:
        print("still dirty")