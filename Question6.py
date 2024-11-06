# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary...")

# Subclass
class Manager(Employee):
    def calculate_salary(self):
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Manager's salary is: ${total_salary}")

# Demonstration of overridden behavior
# Create an instance of Employee
employee = Employee()
employee.calculate_salary()  # Should print the generic message

# Create an instance of Manager
manager = Manager()
manager.calculate_salary()  # Should print the specific calculation for a manager's salary
