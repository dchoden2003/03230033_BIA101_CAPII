class Employee:
    def __init__(self, name, salary, pf_contribution=0, gis_contribution=0, education_allowance=0,organization_type="Private",is_contract_employee=False):
        self.name = name
        self.salary = salary
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.education_allowance = education_allowance
        self.organization_type = organization_type
        self.is_contract_employee = is_contract_employee
# defining the class employee.
# the init is used to initialize the attributes of the object.

class PersonalIncomeTax:  #calculate tax
    def __init__(self, employee):
        self.employee = employee

    def calculate_taxable_income(self):
        if self.employee.organization_type.lower() == 'government':# if the organization is government the PF contribution is excluded.
            taxable_income = self.employee.salary - self.employee.gis_contribution - self.employee.education_allowance
        else:
            if self.employee.is_contract_employee:
                taxable_income = self.employee.salary - self.employee.gis_contribution
            else:
                taxable_income = self.employee.salary - self.employee.pf_contribution - self.employee.gis_contribution - self.employee.education_allowance
        return max(0, taxable_income)# in private and when it is not a contract, PF is included as a deduction.

    def calculate_tax(self):
        taxable_income = self.calculate_taxable_income()
        income_slab = [(300000, 0), (400000, 0.1), (650000, 0.15), (1000000, 0.2), (1500000, 0.25), (float('inf'), 0.3)]
  # this line depicts the tuble representing an income slab and tax rate.
        tax = 0
        for slab, rate in income_slab:
            if taxable_income <= 0:
                break
            if taxable_income <= slab:
                tax += taxable_income * rate
                break
            else:
                tax += slab * rate
                taxable_income -= slab
        return tax

# surcharge is the additional fee added to goods of goods and services.
    def apply_surcharge(self, tax):  #Apply surcharge if the tax amount is greater than or equal to 1,000,000.
        if tax >= 1000000:
            surcharge = tax * 0.10 # if tax is >= 1000000 multiply tax by 10%
            return tax + surcharge
        return tax # if the tax is <1000000 returns tax without surcharge.

# user input to let the user enter their own amount with preference.
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
pf_contribution = float(input("Enter PF contribution: "))
gis_contribution = float(input("Enter GIS contribution: "))
education_allowance = float(input("Enter education allowance: "))
organization_type = input("Enter organization type (Government/Private/Corporate): ")
is_contract_employee_input = input("Is the employee a contract employee? (yes/no): ")


employee = Employee(name, salary, pf_contribution, gis_contribution, education_allowance, organization_type)
employee.is_contract_employee = is_contract_employee_input.lower() == 'yes'
calculator = PersonalIncomeTax(employee)
taxable_income = calculator.calculate_taxable_income()
print("Taxable Income:", taxable_income)
tax = calculator.calculate_tax()
tax_with_surcharge = calculator.apply_surcharge(tax)
print("PIT:", tax_with_surcharge)