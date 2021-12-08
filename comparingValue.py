import time
#Environmental Variables

#input of the first values
value1 = [1, 2, 3, 4, 5, 6, 7, 8]
#input of the second values
value2 = [1, 2, 3, 4, 5, 6, 7, 9]

def errorLog(param1):
    # open or create errorLog.txt for viewing unequal values and comments
    errorLog = open('error.txt', 'w+')
    # write in the log
    for i in param1:
        errorLog.write(str(i))

def comparevalue():
    a = set(value1)
    b = set(value2)
    if a == b:
        print("These values are all equal without doubt")
        return True
    else:
        print("Sorry, Seems you do have unequal values, don't worry i will highlight them for you")
        return False

#Launches the program
if __name__ == "__main__":
    list_difference = []
    #Compares the length values of A and B if of equal length in list
    if len(value1) == len(value2):
        #calls the function and check if it return false
        if comparevalue() == False:
            time.sleep(2)
            print("Creating errorLog file")
            errorLog(param1="")
            time.sleep(2)
            print("Generating Value")
            for item in value1:
                if item not in value2:
                    list_difference.append(item)
                
            print(list_difference)
            errorLog(list_difference)
                        
                        #print("hola")
    else:
        if len(value1) < len(value2):
            print("Sorry values in list 1 is not equal to value in list 2, Thank you")
        else:
            print("Sorry values in a list 2 is not equal to value in list 1, Thank you")

