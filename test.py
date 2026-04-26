# OOP Practice Project

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass
    
    @abstractmethod
    def calculate_discount(self):
        pass


class Product(Payment):
    def __init__(self,name,id,price):
        self.__name = name
        self.__id = id
        self.__price = price
    

    # Getter
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def get_price(self):
        return self.__price
    

    #Setter
    def set_name(self,name):
        if(len(name) == 0):
            print("Empty Name is not Acceptable")
        else: self.__name = name
    
    def set_id(self,id):
        if(id <= None):
            print("You Enter Empty/Invalid id")
        else: self.__id = id
    
    def set_price(self,price):
        if(price <= 0 ):
            print("You Entered Invalid Price")
        else: self.__price = price
        

    def process_payment(self):
        print("Process Done for Product class.")

    
    def calculate_discount(self):
        print(f"You got 5% of discount and your Total price is {self.get_price()}-{self.get_price()*0.05} taka")


class Electronics(Product):
    def __init__(self, name, id, price,warranty):
        super().__init__(name, id, price)
        self.__warranty = warranty

    
    def process_payment(self):
        print("Process Done for Electronics class.")\
        
    def calculate_discount(self):
        price = self.get_price()
        discounted_price = price - (price * 0.1)
        print(f"Electronics: 10% discount applied. Total: {discounted_price} taka")


class Clothing(Product):
    def __init__(self, name, id, price,size):
        super().__init__(name, id, price)
        self.__size = size
    
    def process_payment(self):
        print("Process Done for Clothing class.")

    def calculate_discount(self):
        price = self.get_price()
        discounted_price = price - (price * 0.2)
        print(f"Clothing: 20% discount applied. Total: {discounted_price} taka")



# object 

elec = Electronics("Laptop", 457, 80000, "1 Year")
cloth = Clothing("Shirt", 441, 1500, 42)

elec.process_payment()
elec.calculate_discount()

print("-" * 20)

cloth.process_payment()
cloth.calculate_discount()

