class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        return "some generic sound"
    def get_info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__unit__(name,age)
        self.breed=breed
    def make_sound(self):
        return"woof!"

dog=Dog("Buddy",3,"Golden retriever")
print(dog.get_info())
print(f"{dog.name}says:{dog.make_sound()}")
   
