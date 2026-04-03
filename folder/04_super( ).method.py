class employee():
    def __init__(self):
     print("constructor of employee:")
    a= 1

class progarmmer(employee):
    def __init__(self):
     print("Constructor of programmer:")
    b= 2

class coder(progarmmer):
    def __init__(self):
     super().__init__()  # its used to add parent and child class 
    print("Constructor od coder: ")
    c=3


# o= employee
# print(o.a)

# o= progarmmer()
# print(o.a, o.b)

o= coder()
print(o.a, o.b, o.c)
