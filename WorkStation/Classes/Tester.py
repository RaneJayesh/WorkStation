from Classes.Employee import Employee

# Tester class
class Tester(Employee):
    
    def DoWork(self):
        print("Tester " + self.GetFullName() + " is testing.")


