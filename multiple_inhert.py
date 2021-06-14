class os:
    item = True
    name = 'gtxforce'
class hdd:
    website = 'www.nvidiax.com'
    name = 'gtxffd'
    
    #order matters of class
class gamers(hdd,os):
    def __init__(self):
        if self.item is True:
            print("The gamers love {} and they can contact at {}".format(self.name, self.website))
            
th = gamers()


#this is multiple level inhertiance
class whisky:
    item = 'jd'
    
class age(whisky):
    duration = 23
    
class customer(age):
    def __init__(self):
        self.age = 18
        print("This {} whisky is {} old and can be consumed by people above {} years of age".format(self.item, self.duration, self.age))
        
cust = customer()
    
#when making protected your class and derived class has access to that., private means access to just your class not even your derived class
#public - member_name
#protected - _member_name
#private - __member_name

class Car:
    wheels = 4
    _color = 'red'
    __yom = 2020 #here name mangling happens (i.e. it is being stored as _Car__yom)
    
class audi(Car):
    def __init__(self):
        print("this is my dream car color", self._color)
car = Car()
print(car.wheels)
audii = audi()
# print("the yom for car is", car.__yom)  #even though this statement is right it still throws error becoz it is in private state

#this is the correct way
print("the yom of car is: ", car._Car__yom)
