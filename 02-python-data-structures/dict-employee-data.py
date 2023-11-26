"""
A program to loop over some employee data and make it presentable.
"""

# employee data
employees = [
  {
    "Name": "John Mckee",
    "Age": 38,
    "Department": "Marketing"
  },
  {
    "Name": "Lisa Crawford",
    "Age": 29,
    "Department": "Sales"
  },
  {
    "Name": "Sujan Patel",
    "Age": 33,
    "Department": "HR"
  },
]

# looping through data
for employee in employees:
  print("Name: {}\nAge: {}\nDepartment: {}".format(employee["Name"], employee["Age"], employee["Department"]))
  print("-" * 20)

# for Sujan only
employee = employees[2]
print("Name: {}\nAge: {}\nDepartment: {}".format(employee["Name"], employee["Age"], employee["Department"]))
print("-" * 20)