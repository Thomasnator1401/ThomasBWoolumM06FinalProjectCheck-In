class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Dictionary
my_dict = {'name': 'Thomas', 'age': 29, 'city': 'Centerville', 'state': 'Indiana'}

from tkinter import Tk, Label, Button

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Team 5 of the Final Project - Software Development - Python")

        self.label = Label(master, text="This is our GUI for the Team 5 of the Final Project - Software Development - Python")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyGUI(root)
root.mainloop()

