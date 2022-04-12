
# Parent class
class User:
    first_name = 'Unknown'
    last_name ='Unknown'
    gender = 'Unknown'
    age = 'Unknown'

    def information(self):
        msg = "\nName: {}\nLast Name: {}\nGender: {}\nAge: {}".format(self.first_name,self.last_name,self.gender,self.age)
        return msg

# This is the first child class instance
class Customer(User):
    first_name = 'Tom'
    last_name = 'Smith'
    gender = 'Male'
    age = '27'

    def information(self):
        msg = "\nMy name is Tom and I love shopping here!"
        return msg 

# This is the second  child class instance

class Employee(User):
    first_name = 'Sherry'
    last_name = 'Johnson'
    gender = 'Female'
    age = '32'

    def information(self):
        msg = "\nMy name is Sherry and I love my current job!"
        return msg

if __name__ == "__main__":
    customer = Customer()
    print(customer.information())
    print(customer.shop())

    
    employee = Employee()
    print(employee.information())
    print(employee.work())

    



    
