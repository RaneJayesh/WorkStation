from Classes.Employee import Employee

# Accountant class
class Accountant(Employee):

    def DoWork(self):
        print("Account " + self.GetFullName() + " is accounting.")

    def PaySalary(self, employees = None):

        if employees == None:
            super().PaySalary()
            return

        for employee in employees:
            employee.PaySalary()