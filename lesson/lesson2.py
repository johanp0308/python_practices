import string

class animal:
    def __init__(self,color,breed):
        self.breed = breed
        self.color = color
    def run(self):
        print("Running...")
    
    def eat(self):
        print("Eating...")
        
dog = animal()
dog.eat()
dog.bread = "puddle"
dog.age = 5