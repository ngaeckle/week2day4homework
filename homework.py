class Cart():
    def __init__(self):
        self.inventory = []


    def add_info(self, item):
        self.inventory.append(item)

    def del_info(self, item):
        self.inventory.remove(item)

    def show_info(self):
        print(self.inventory)
my_cart = Cart()
def main():
    while True:
        choice = input("What would you like to do? Show/Add/Delete or Quit? ")
        if choice.lower() == "show":
            my_cart.show_info()
        elif choice.lower() == "add":
            item = input("what would you like to add? ")
            my_cart.add_info(item)
        elif choice.lower() == "delete":
            item = input("What would you like to delete? ")
            my_cart.del_info(item)
        else:
            print("You chose to quit")
            break
    my_cart.show_info()
main()
        

"""
Write a python class which has two methods get_string and print_string. get_String accept a string from the user and print_string prints the string in upper case

"""

class Form():

    def __init__(self):
        pass

    def print_string(string):
        print(string.upper())
    
    def get_string():
        return Form.print_string(input("Give me a string: "))
    
Form.get_string()





