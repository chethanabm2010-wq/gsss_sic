# Level 3: Tax and Rebate Calculation

# Step 1: Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Monthly Salary (Rs): "))
special_allowances = float(input("Enter Special Allowances (Monthly) (Rs): "))
bonus_percentage = float(input("Enter Annual Bonus Percentage (% of Gross Salary): "))

# Step 2: Constants
STANDARD_DEDUCTION = 50000
CESS_RATE = 0.04  # 4% cess

# Step 3: Calculate Gross Salaries
gross_monthly_salary = basic_salary + special_allowances
annual_bonus = (gross_monthly_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

# Step 4: Calculate Taxable Income
taxable_income = annual_gross_salary - STANDARD_DEDUCTION
if taxable_income < 0:
    taxable_income = 0

# Step 5: Tax calculation as per New Tax Regime (2023)
def calculate_tax(taxable):
    tax = 0
    remaining = taxable

    if remaining > 1500000:
        tax += (remaining - 1500000) * 0.30
        remaining = 1500000
    if remaining > 1200000:
        tax += (remaining - 1200000) * 0.20
        remaining = 1200000
    if remaining > 900000:
        tax += (remaining - 900000) * 0.15
        remaining = 900000
    if remaining > 600000:
        tax += (remaining - 600000) * 0.10
        remaining = 600000
    if remaining > 300000:
        tax += (remaining - 300000) * 0.05

    return tax

# Step 6: Apply rebate under Section 87A if eligible
if taxable_income <= 700000:
    tax_payable = 0
else:
    base_tax = calculate_tax(taxable_income)
    cess = base_tax * CESS_RATE
    tax_payable = base_tax + cess

# Step 7: Net Salary
net_salary = annual_gross_salary - tax_payable

# Step 8: Display breakdown
print("\n===== Employee Tax Calculation (New Tax Regime 2023) =====")
print(f"Name                 : {name}")
print(f"Employee ID          : {emp_id}")
print(f"Gross Monthly Salary : Rs {gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary  : Rs {annual_gross_salary:,.2f}")
print(f"Standard Deduction   : Rs {STANDARD_DEDUCTION:,.2f}")
print(f"Taxable Income       : Rs {taxable_income:,.2f}")

if taxable_income <= 700000:
    print("Tax Slabs Applied    : Eligible for Section 87A Rebate → Tax Payable = 0")
else:
    print(f"Base Tax (before cess): Rs {base_tax:,.2f}")
    print(f"Health & Edu. Cess 4% : Rs {cess:,.2f}")
    print(f"Total Tax Payable    : Rs {tax_payable:,.2f}")

print(f"Net Annual Salary    : Rs {net_salary:,.2f}")

