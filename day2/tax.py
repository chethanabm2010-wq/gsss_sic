# -------------------
# Level 1: Basic Input
# -------------------
name = input("Enter your name: ")
basic_salary = float(input("Enter your basic salary: "))
allowances = float(input("Enter total allowances: "))
bonus = float(input("Enter total bonus: "))

print("\n--- Level 1 Output ---")
print("Name:", name)
print("Basic Salary:", basic_salary)
print("Allowances:", allowances)
print("Bonus:", bonus)

# -------------------
# Level 2: Gross Salary, Standard Deduction, Taxable Income
# -------------------
gross_salary = basic_salary + allowances + bonus
standard_deduction = 50000
taxable_income = gross_salary - standard_deduction

print("\n--- Level 2 Output ---")
print("Gross Salary:", gross_salary)
print("Standard Deduction:", standard_deduction)
print("Taxable Income:", taxable_income)

# -------------------
# Level 3: Tax Calculation (New Tax Regime 2023)
# -------------------
tax = 0

if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

print("\n--- Level 3 Output ---")
print("Calculated Tax (before rebate & cess):", tax)

# -------------------
# Level 4: Section 87A Rebate
# -------------------
if taxable_income <= 700000:
    tax = 0
    print("Rebate applied under Section 87A: Tax Payable = 0")

# -------------------
# Level 5: Health & Education Cess (4%)
# -------------------
cess = tax * 0.04
total_tax = tax + cess

print("\n--- Level 5 Output ---")
print("Tax after rebate:", tax)
print("Health & Education Cess (4%):", cess)

# -------------------
# Level 6: Final Tax Payable
# -------------------
print("\n--- Level 6 Final Output ---")
print("Total Tax Payable:", total_tax)
