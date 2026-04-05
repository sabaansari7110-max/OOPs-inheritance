# Classs 'pets' from a 'Animals' and from create a class 'Dog' from 'Pets'. Add a meethod 'Bark' to class 'Dog"

class Animals:
    pass          # we pass to show syntax the code.

class pets(Animals):
    pass

class dog(pets):

    @staticmethod
    def bark():
     print("Bow Bow!")


d= dog()
d.bark()
