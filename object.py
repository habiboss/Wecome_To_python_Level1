

class jeans:

    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False

    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False



class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

class vehicle:

    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 #full tank

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('the {} {} goes VROOM!'.format(self.color, self.manuf))
        else:
            print('the {} {} sputters out of gas'.format(self.color, self.manuf))
    
class Car(vehicle): #inherits from vehicle class
    #turn the radio on
    def radio(self):
        print("rockin tunes!")

    #open the window
    def window(self):
        print("Ahhh......fresh air")

class Motorcycle(vehicle):  #inherit the vehicle cass
    #put on the helmet
    def helmet(self):
        print("nice and safe")

class ECar(Car):
    def drive(self):
            print('the {} {} goes sssshhhh!'.format(self.color, self.manuf))
        


if __name__ == "__main__":
    red = shirt()
    crimson = red
    