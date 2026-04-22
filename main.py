
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = 0
        self.new_age(age)

    def get_age(self):
        return self._age
    
    def new_age(self, new_age):
        if new_age < 0:
            print('Error: Age cannot be negative')
        
        else:
            self._age = new_age
        

dog1 = Dog('Lex', -1)
dog1.new_age(3)
print(dog1.get_age())
