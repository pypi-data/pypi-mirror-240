class Pystachios:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} tiene {self.age} años"
