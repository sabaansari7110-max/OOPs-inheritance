class Employee:
    company= "ITC"

    def show(self):
        print(f'employee name{self.name} and salary {self.salary}')


class programmer(Employee):
    company= "ITC medi"
    
    def showlanguage(self):
        print(f"name {self.name} and good with {self.language} language")




a= Employee()
b=programmer()
print(a.company,"\n",b.company)
