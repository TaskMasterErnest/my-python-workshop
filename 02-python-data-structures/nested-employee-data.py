"""
A program to loop over some employee data and make it presentable.
"""

# employee data
employees = [["John Mckee", 38, "Marketing"], ["Lisa Crawford", 29, "Sales"], ["Sujan Patel", 33, "HR"]]

# looping through data
for employee in employees:
  print("Name: {}\nAge: {}\nDepartment: {}".format(employee[0], employee[1], employee[2]))
  print("-" * 20)

# for Lisa only
employee = employees[1]
print(employee)
print("Name: {}\nAge: {}\nDepartment: {}".format(employee[0], employee[1], employee[2]))
print("-" * 20)
