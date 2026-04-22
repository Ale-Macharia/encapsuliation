
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class dog(animal):
    def speak(self):
        print('woof !!')

class cat(animal):
    def speak(self):
        print('meowwww @@@')


dog1 = dog('Lilian', 4)
cat1 = cat('puss', 1)

cat1.speak()
print(cat1.age)
