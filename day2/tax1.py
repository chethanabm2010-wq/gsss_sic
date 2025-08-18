# Level 1: Basic Input and Salary Calculation

# Step 1: Accept Employee Inputs

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Monthly Salary (Rs): "))
special_allowances = float(input("Enter Special Allowances (Monthly) (Rs): "))
bonus_percentage = float(input("Enter Annual Bonus Percentage (% of Gross Salary): "))

# Step 2: Calculate Gross Monthly and Annual Salary
gross_monthly_salary = basic_salary + special_allowances
annual_bonus = (gross_monthly_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

# Step 3: Display Results
print("\n===== Employee Salary Details =====")
print(f"Name               : {name}")
print(f"Employee ID        : {emp_id}")
print(f"Gross Monthly Salary: Rs {gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary: Rs {annual_gross_salary:,.2f}")
