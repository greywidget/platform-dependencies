class Animal:

    _counter = 10000
    animals = []

    def __init__(self, name: str):
        self.name = name.capitalize()
        Animal._counter += 1
        self.counter = Animal._counter
        Animal.animals.append(self)

    def __str__(self):
        return f"{self.counter}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([str(animal) for animal in Animal.animals])
