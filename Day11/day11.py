class Employee:
    def __init__(self,  emp_name, emp_id, emp_salary, emp_department):
        self.emp_name= emp_name
        self.emp_id = emp_id
        self.emp_salary= emp_salary
        self.emp_department= emp_department

    def calculate_emp_salary():
            pass

    def emp_assign_department(self, department):
        self.emp_department = department
           


    def print_employee_details(self):
             return f"{self.emp_name}{self.emp_id} {self.emp_salary}{self.emp_department}"

emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")

print(emp1.print_employee_details())

emp1.emp_assign_department("HR")

print(emp1.print_employee_details())
        