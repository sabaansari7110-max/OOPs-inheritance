class employee():
    a= 1

class progarmmer(employee):
    b= 2

class coder(progarmmer):
    c=3


o= employee
print(o.a) # prints the "a" attribute
#print(o.b) show an erroe as there is no "b" attribute in employee class.

o= progarmmer()
print(o.a, o.b)

o= coder()
print(o.a, o.b, o.c)
