#from: Inheritance and Composition: A Python OOP Guide
#available in: https://realpython.com/inheritance-composition-python/


import hr
import employees
import productivity
import contacts


# You can now modify the program to assign some addresses to the employees:


manager = employees.Manager(1, 'Mary Poppins', 3000)
#applying Composition
manager.address = contacts.Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)
secretary = employees.Secretary(2, 'John Smith', 1500)
#applying Composition
secretary.address = contacts.Address(
    '67 Paperwork Ave.',
    'Manchester',
    'NH',
    '03101'
)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
"""payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])"""