class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self):
        salary = float(input("Enter salary: "))
        hours_worked = float(input("Enter hours worked: "))

        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary / 50)
            total_salary = overtime_amount + salary
            return total_salary
        else:
            return 0

    def emp_assign_department(self, department):
        self.emp_department = department

    def print_employee_details(self):
        return f"{self.emp_name} {self.emp_id} {self.emp_salary} {self.emp_department}"


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")

print(emp1.print_employee_details())

emp1.emp_assign_department("HR")

print(emp1.print_employee_details())

total_salary = emp1.calculate_emp_salary()
print(f"Total Salary: {total_salary}")
