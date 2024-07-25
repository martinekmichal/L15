# interface segragation


from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class Ostriche(Bird):
    def fly(self):
        raise Exception("Ostriche is not flying")

    def walk(self):
        print("Ostriche is walking")

class Eagle(Bird):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")

try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostriche()
    obj2.walk()
    obj2.fly()
except Exception as e:
    print(e)

    