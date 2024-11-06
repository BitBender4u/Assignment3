# Engine class
class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

# Car class
class Car:
    def __init__(self):
        # Car has an engine attribute, which is an instance of Engine
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Demonstration
# Create a Car instance
my_car = Car()

# Use Car methods to control the engine
my_car.start_engine()  # Should print "Engine started."
my_car.stop_engine()   # Should print "Engine stopped."
