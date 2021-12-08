import time
hungry = True


while(hungry):
    print ("opening the front door")
    #front_door = open('c:/Users/AlhousseiniDiakite/Documents/pythonCode/front_door.txt', 'r')
    front_door = ['welcome here', 'hi im here', 'pizza order']
    if "pizza order" in front_door:
        print("pizza is here")
        hungry = False
    else:
        print("Not yet")

    print('Closing the front door')
    #front_door.close()

    time.sleep(1)