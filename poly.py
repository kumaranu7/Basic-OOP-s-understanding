class employee:
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 40
    def display_number_of_working_hours(self):
        print(self.number_of_working_hours)
        
class Trainee(employee):
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 45
    
    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours() #after using super you can use the attributes of base class
        
emp = employee()
emp.set_number_of_working_hours()
print('No. of working hours', end = ' ')
emp.display_number_of_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours()
print('No. of working hours', end = ' ')
trainee.display_number_of_working_hours()

trainee.reset_number_of_working_hours()
print('No. of working hours after reset', end = ' ')
trainee.display_number_of_working_hours()
