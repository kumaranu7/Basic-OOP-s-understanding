class Furniture:
    def __init__(self):
        self.type_of_wood = 'teakwood'
        # self.numberoflegs  = 4
        
class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.numberoflegs  = 4
    def changewoodtype(self, typeofwood):
        self.type_of_wood = typeofwood
    
    def chairdetials(self):
        print("The chair is made up of {} and has {} legs".format(self.type_of_wood, self.numberoflegs))
    
chair = Chair()
print('Do you wish to change woodtype for your chair: Yes/No')
uc = input()
if uc == 'Yes':
    print("Enter the type of wood you would like to use for your chair")
    typeofWood = input()
    chair.changewoodtype(typeofWood)
chair.chairdetials()
        