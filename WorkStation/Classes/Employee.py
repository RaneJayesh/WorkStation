
# Employee base class
class Employee(object):

    RaiseAmount = 1.20

    def __init__(self, firstName, lastName, dateOfJoin, salary):
        self.FirstName = firstName
        self.LastName = lastName
        self.DateOfJoin = dateOfJoin
        self.Salary = salary

    def PaySalary(self):
        print("Employee " + self.GetFullName() +  " is been paid Rs. " + str(self.Salary))

    def SetRaiseAmount(self, raiseAmount):
        self.RaiseAmount = raiseAmount

    def IncrementSalary(self):
        self.Salary = self.Salary * self.RaiseAmount

    def GetFullName(self):
        return self.FirstName + " " + self.LastName

    def DoWork(self):
        pass


