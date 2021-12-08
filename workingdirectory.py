import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("Item exist: " + str(path.exists("front_door.txt")))
    print("Item is a file: " + str(path.isfile("front_door.txt")))
    print("Item is a directory: " + str(path.isdir("front_door.txt")))

    print("Item path: " + str(path.realpath("front_door.txt")))
    print("Item path and name: " + str(path.split(path.relpath("front_door.txt"))))

    #get modification time
    t = time.ctime(path.getmtime("front_door.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("")))


    # get how long the file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(""))
    print("it has been" + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()

   