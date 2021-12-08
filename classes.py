class myClass():
    def method1(self):
        print("myClass method 1")

    def method2(self, someThing):
        print("myClass method 2" + someThing)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method 1")

    def method2(self, someThing):
        print("anotherClass method 2" + someThing)

def main():
    c = myClass()
    c.method1()
    c.method2("this is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("this is a string")

main()
