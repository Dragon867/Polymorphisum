class Lion:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"I am a lion.My name is {self.name}.I am {self.age} years old.")
    
    def makesound(self):
        print("Roar")
        
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"I am a dog.My name is {self.name}.I am {self.age} years old.")
    
    def makesound(self):
        print("Bark")
        
Lion1=Lion("Johnny",20)
Dog1=Dog("Jack" ,5)
    
for animal in(Lion1,Dog1):
    animal.makesound()
    animal.info()