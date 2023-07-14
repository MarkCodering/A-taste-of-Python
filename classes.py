class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def select_car(self):
        print("You have selected a", self.color, self.name)
        
    def drive(self):
        print("You are driving a", self.color, self.name)
    
def main():
    car = Car("Tesla", "red")
    car.select_car()
    car.drive()
    
if __name__ == "__main__":
    main()