class Car:
    def __init__(self):
        self.carfare = {'Hatchback':30, 'Sedan':50, 'SUV':100}
        
    def Displaycarinfo(self):
        print("Fare of following available cars (per day):")
        print("Hatchback: $", self.carfare['Hatchback']) 
        print("Sedan: $",self.carfare['Sedan']) 
        print("SUV: $", self.carfare['SUV'])   
        
    def calculate(self, typeofCar, numberofDays):
        return self.carfare[typeofCar] * numberofDays
    
car = Car()

while True:
    print("Enter 1 to display car rental information")
    print("Enter 2 to select the type of car for rental")
    print("Enter 3 to exit")
    userchoice =  int(input())
    if userchoice is 1:
        car.Displaycarinfo()
    elif userchoice is 2:
        print("Enter the number of days you would like to rent")
        numberofDays = int(input())
        print("Enter the type of car for rent")
        cartype = input()
        fare = car.calculate(cartype, numberofDays)
        print("Your total fare is: $", fare)
        print('Thank You for using our shitty serivice')
    elif userchoice is 3:
        exit()