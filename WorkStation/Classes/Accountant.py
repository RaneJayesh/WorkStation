from Classes.Employee import Employee

class Accountant(Employee):

    def PaySalary(self, employees = None):

        if employees == None:
            super.PaySalary(Accountant, self)
            return

        for employee in employees:
            employee.PaySalary()