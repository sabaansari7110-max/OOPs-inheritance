class Employee:
    companyy= "ITC"
    name= "default"
     
    def show(self):
        print(f'Employee name {self.name} and salary {self.companyy}')

class coder:
    language= "python"
    def printlanguage(self):
      print(f"Out of all the language here is your language: {self.language}")

class programmer(Employee, coder):
    company= "ITC medi"
    
    def showlanguage(self):
        print(f"Name {self.company} and good with {self.language} language")




a= Employee()
b=programmer()

b.show()
b.printlanguage()
b.showlanguage()

