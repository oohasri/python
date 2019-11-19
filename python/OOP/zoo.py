class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, name):
        self.animals.append(name)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal)
class Animal:
    def __init__(self, name, age, health_level=9, happiness=9):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness = happiness
    def display_info(self):
        print(self.name, self.age, self.health_level, self.happiness)       
    def feed(self):
        self.health_level +=10
        self.happiness +=10
        print(self.name, self.age, self.health_level, self.happiness)       
class Tiger(Animal):
    def __init__(self, name, age, color, health_level=10, happiness=10):
        super().__init__(name, age, health_level, happiness)
        # print("name is",name)
        self.color = color
        # self.name = name
        # self.age = age
class Bear(Animal):
    def __init__(self,  name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        super().__init__(name, age, health_level=10, happiness=10)
class Camel(Animal):
    def __init__(self,  name, age, height, health_level=7, happiness=7):
        self.name = name
        self.height = height
        self.age = age
        super().__init__(name, age,health_level=20, happiness=20)

zoo1 = Zoo("John's Zoo")
tiger = Tiger("Tig", 3, "orange")
bear = Bear("Teddy", 5, 56)
camel = Camel("Cam", 2, 100)
camel.feed()
tiger.feed()
bear.feed()
zoo1.add_animal(tiger.name)
zoo1.add_animal(bear.name)
zoo1.add_animal(camel.name)
zoo1.print_all_info()