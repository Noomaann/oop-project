from abc import ABC,abstractmethod

class Product(ABC):

    def __init__(self,id,stock,price):
        self.__product_id = id
        self.__stock = stock
        self.__base_price = price

    #getter
    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__base_price

    #setter
    def set_stock(self,amount):
        if(amount <= 0):
            print("You Entered Invalid Amount of Stock")
        else:
            self.__stock+=amount
    
    def set_price(self,price):
        if(price < 0):
            print("You Entered Invalid ammount of Price")
        else:
            self.__base_price = price


    @abstractmethod
    def show_details(self):
        pass
    
    @abstractmethod
    def calculate_discount(self):
        pass



class Saree(Product):
    def __init__(self,id,stock,price,fabric_type):
        super().__init__(id,stock,price)
        self.__febric_type = fabric_type
    
    def show_details(self):
        print(f"Saree ache {self.get_stock()} Piece")
    
    def calculate_discount(self):
        print(f"Saree er upore 5% Discount deyar por apnr Taka ashe {(self.get_price())-self.get_price()*0.05} Taka")

        



class Panjabi(Product):
    def __init__(self, id, stock, price,size):
        super().__init__(id, stock, price)
        self.__size = size 

    def show_details(self):
        print(f"Panjabi ache {self.get_stock()} Piece")
    
    def calculate_discount(self):
        print(f"Panjabi er upore 10% Discount deyar por apnr Taka ashe {(self.get_price())-self.get_price()*0.1} Taka")



class ThreePiece(Product):
    def __init__(self,id,stock,price,color):
        super().__init__(id,stock,price)
        self.__color = color
    
    def show_details(self):
        print(f"Three Piece ache {self.get_stock()} Piece")

    def calculate_discount(self):
        print(f"Three Piece er upore Flat 300 taka Discount deyar por apnr Taka ashe {(self.get_price())-300} Taka")

        

# --- অবজেক্ট তৈরি এবং টেস্ট করা ---

objA = Saree(101, 10, 2000, "Jamdani")
objB = Panjabi(102, 12, 1500, 40)
objC = ThreePiece(103, 15, 2500, "Red")

print("--- ইনভেন্টরি ডিটেইলস ---")
objA.show_details()
objA.calculate_discount()

print("\n")
objB.show_details()
objB.calculate_discount()

print("\n")

objC.show_details()
objC.calculate_discount()