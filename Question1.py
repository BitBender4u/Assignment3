class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"Car Details:\nMake:{self.make}\nModel:{self.model}\nYear:{self.year}")

M1 = Car("Mercedes", "G63", 2020)
M1.display_info()