from os import O_EXCL


def main():


    #f = open("c:/Users/AlhousseiniDiakite/Documents/pythonCode/textfile.txt", "w+")
    f = open('front_door.txt', 'a')
    #for i in range(10):
     #   f.write("this is a line" + str(i) + "\r\n")
      #  f.close()

    if f.mode == 'r':
       # contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)
        #print(contents)
