from Classes.Employee import Employee

class Developer(Employee):
            
    def DoWork(self):
        print("Developer " + self.GetFullName() + " is developing.")
    


