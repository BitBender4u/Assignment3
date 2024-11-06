# Define the Cat class
class Cat:
    def make_sound(self):
        print("Meow")

# Define the Dog class
class Dog:
    def make_sound(self):
        print("Bark")

# Function to demonstrate polymorphism
def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Call the function with each instance
animal_sound(my_cat)  # Should print "Meow"
animal_sound(my_dog)  # Should print "Bark"
