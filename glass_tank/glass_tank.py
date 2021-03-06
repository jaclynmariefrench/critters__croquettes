from datetime import date

class Snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"

simon = Snake("Simon", "Copperhead", "rats")
steve = Snake("Steve", "Python", "rabbits")
sassy = Snake("Sassy", "Cobra", "rats")