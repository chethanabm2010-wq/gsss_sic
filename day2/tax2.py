# Level 2: Taxable Income Calculation

# Step 1: Accept Inputs
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Monthly Salary (Rs): "))
special_allowances = float(input("Enter Special Allowances (Monthly) (Rs): "))
bonus_percentage = float(input("Enter Annual Bonus Percentage (% of Gross Salary): "))

# Step 2: Constants
STANDARD_DEDUCTION = 50000  # As per New Tax Regime 2023

# Step 3: Calculate Gross Salaries
gross_monthly_salary = basic_salary + special_allowances
annual_bonus = (gross_monthly_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

# Step 4: Calculate Taxable Income 
taxable_income = annual_gross_salary - STANDARD_DEDUCTION
if taxable_income < 0:
    taxable_income = 0  # Taxable income cannot be negative

# Step 5: Display Output
print("\n===== Employee Salary Details =====")
print(f"Name               : {name}")
print(f"Employee ID        : {emp_id}")
print(f"Gross Monthly Salary: Rs {gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary: Rs {annual_gross_salary:,.2f}")
print(f"Standard Deduction : Rs {STANDARD_DEDUCTION:,.2f}")
print(f"Taxable Income     : Rs {taxable_income:,.2f}")
