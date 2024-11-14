class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def se_presenter(self):
        return "Bonjou, je m'appelle {} et j'ai {} ans.".format(self.name,self.age)

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)


person1 = Person("Mamadou",25)
person2 = Person("Naruto", 17)

print(person1)
print(person2)

print(person1.se_presenter())
print(person2.se_presenter())