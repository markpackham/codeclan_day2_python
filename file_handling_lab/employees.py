import csv

class Employee:
    def __init__(self, first_name, last_name, hourly_rate, hours_worked, amount_due):
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = int(hours_worked)
        self.amount_due = float(amount_due)
    
    def values(self):
        return [self.first_name, self.last_name, self.hourly_rate, self.hours_worked, self.amount_due]

employees = []

with open("employees.csv", "r") as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, skipinitialspace=True)

    for row in reader:
        current_employee = Employee(*row)
        employees.append(employees)

with open("employees.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    employee = Employee("Jenny","Jones",12.50,40,0)
    writer.writerow(employee.values())