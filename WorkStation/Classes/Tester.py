from Classes.Employee import Employee

class Tester(Employee):
    
    def DoWork(self):
        print("Tester " + self.GetFullName() + " is testing.")


