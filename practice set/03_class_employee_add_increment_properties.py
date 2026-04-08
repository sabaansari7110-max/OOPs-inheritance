# Class 'employee' and add salary and increment properties to it.
'''
 A method 'salaryAfterIncrement' method with a @ property decorator with a setter which
 changes the values of increment based on the salary. 
'''

class employee:
    salary= 234
    increment= 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary + (self.increment/100))


    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment= ((salary/self.salary) -1)*100



e= employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement= 280.8
print(e.increment)
