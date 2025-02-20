class Car:
    def __init__(self, maker, model, price):
        self.car_maker = maker
        self.car_model = model
        self.car_price = price
    def get_maker(self):
        return self.car_maker
    def get_model(self):
        return self.car_model
    def get_price(self):
        return self.car_price
        
    def update_price(self):
        self.updated_price = self.car_price

class Dealer:
    def __init__(self, address, inventory):
        self.deal_address = address
        self.deal_inventory = [ ]
        
    def show_cars(self):
        print("Current Inventory \n")
        for car in self.deal_inventory:
            print (car)
           
    def add_car(self):
        car_num = int(input("How many cars do you want to add?: "))
        for num in range(car_num):
            print("Car-#", num + 1)
            maker = str(input("Maker: "))
            model = str(input("Model: "))
            price = int(input("Price: $"))
            car = Car(maker, model, price)
            self.deal_inventory.append(car)

    
    def remove_car(self):
        car_num = int(input("How many cars to remove?: "))
        for i in range(car_num):
            model = input("Model to remove: ")
            found = False
            for car in self.deal_inventory:
                if car.get_model() == model:
                    self.deal_inventory.remove(car)
                    found = True

    def update_price(self):
        print("Update price for a model \n")
        model = str(input("Model for update: "))
        price = int(input("New price: $"))
        Car.update_price(self)
       

    def total_value(self):
        total = 0
        for car in self.deal_inventory:
            total = total + self.car_price
        print("The total value in inventory: ", total)
        
                      
                        



def main():
    address = input("Dealer address: ")
    inventory = ("Current Inventory \n")
    dealer = Dealer(address, inventory)
    dealer.add_car()
    ("Current Inventory \n")
    dealer.show_cars()
    dealer.remove_car()
    dealer.show_cars()
    dealer.update_price()
    dealer.show_cars()
    dealer.total_value()
main()
            
        






