
# Here is the creation of the first parent class.
class User:
    name = 'No Name Provided'
    email = ' '
    password = 'abdc567'
    account_number = 0

# Here is the creation of a child class that will inherit from 'User'(parent)
class Employee(User):
    hourly_pay = 15.00
    department = 'All Departments'
    
# Second child class that will also inherit from the 'User'(parent)
class Customer(User):
    address = ' '
    mailing_list = True
    customer_number = 0
    
