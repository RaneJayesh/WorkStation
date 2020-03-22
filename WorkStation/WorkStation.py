import datetime
from Classes.Developer import Developer
from Classes.Tester import Tester
from Classes.Accountant import Accountant

employee1 = Developer("Jayesh", "Rane", datetime.datetime(2018, 1, 1), 17_500)
employee2 = Tester("Sayali", "Rane", datetime.datetime(2017, 4, 5), 50_000)
employee3 = Accountant("Dhanashree", "Rane", datetime.datetime(2019, 3, 4), 30_000)

employees = [employee1, employee2, employee3]

employee1.PaySalary()
employee2.PaySalary()
employee3.PaySalary(employees)

employee1.DoWork()
employee2.DoWork()
employee3.DoWork()

employee1.SetRaiseAmount(1.30)

employee1.IncrementSalary()
employee2.IncrementSalary()

employee1.PaySalary()
employee2.PaySalary()