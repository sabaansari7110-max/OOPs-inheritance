class employee:
    a= 9

    @classmethod
    def show(cls):
        print(f"The class attribute of 'a' is {cls.a}")


e= employee()
e.a= 45

e.show()