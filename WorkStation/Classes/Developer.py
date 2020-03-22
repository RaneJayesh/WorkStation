from Classes.Employee import Employee

# Developer class
class Developer(Employee):
            
    def DoWork(self):
        print("Developer " + self.GetFullName() + " is developing.")