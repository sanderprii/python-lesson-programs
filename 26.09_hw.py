import time

class Product:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Product: {self.name}")

def make_cream():
    print("To create face cream, we need 4 ingredients: water, glycerin, hyaluronic acid, provitamin B5.")
    mix = int(input("Do you want to mix all the ingredients? Press 1 for yes and 2 for no: "))
    
    if mix == 1:
        print("\nLet's start making the face cream...")
        ingredients = 0
        
        while ingredients < 4:
            print("Adding ingredient...")
            time.sleep(1)
            ingredients += 1
            print(f"Added {ingredients} ingredients out of 4")
        
        print("Face cream is almost ready! Just need to add preservatives.")
        count = float(input("Enter the amount of preservative you want to add (you need to add 0.7ml for a 50ml jar): "))
        
        if count == 0.7:
            print("You entered the correct amount of preservative, mixing the cream...")
            time.sleep(1)
            print("Congratulations, your 50ml face cream is ready!")
        else:
            print("Incorrect amount of preservative. Try again.")
    else:
        print("Okay, we can try later!")

def make_shampoo():
    print("To create shampoo, we need water, coconut oil, provitamin B5, and fragrance.")
    time.sleep(1)
    print("Congratulations, your shampoo is ready!")

def make_serum():
    print("To create serum, we need hyaluronic acid, niacinamide, vitamin C, and antioxidants.")
    time.sleep(1)
    print("Congratulations, your serum is ready!")

def main():
    hello = int(input("Hello! Today you are creating your own cosmetic product. Do you want to start? (yes(1)/no(2)): "))

    if hello == 1:
        remaining_products = {
            1: Product("face cream"), 
            2: Product("shampoo"), 
            3: Product("face serum")
        }
        
        while remaining_products:
            print("\nChoose the product you want to make:")
            for number, product in remaining_products.items():
                product.display()
            
            choice = int(input("Your choice (1 for face cream, 2 for shampoo, 3 for face serum): "))

            if choice in remaining_products:
                if choice == 1:
                    make_cream()
                elif choice == 2:
                    make_shampoo()
                elif choice == 3:
                    make_serum()
                
                del remaining_products[choice]
                
                if remaining_products:
                    another = int(input("Do you want to make something else? (yes(1)/no(2)): "))
                    if another != 1:
                        print("See you next time!")
                        break
                else:
                    print("You made all the products! Great job!")
            else:
                print("Invalid choice, try again.")
    else:
        print("Okay, see you next time!")

main()
