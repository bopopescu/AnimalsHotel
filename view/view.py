from tkinter import *
from tkinter.ttk import *


class View:

    def __init__(self):
        self.window = Tk()
        self.delete_window = Tk()
        self.update_window = Tk()

        self.window.title("Add New Pet")
        self.delete_window.title("Delete Pet")
        self.update_window.title("Update Pet")

        self.window.geometry("300x300")
        self.delete_window.geometry("300x300")
        self.update_window.geometry("300x300")

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="Actions", menu=self.file_menu)

        self.label_id_add_window = Label(self.window, text="ID")
        self.label_pet_add_window = Label(self.window, text="Pet Name")
        self.label_type_add_window = Label(self.window, text="Pet Type")

        self.label_pet_add_window.grid(row=0, sticky=E)
        self.label_type_add_window.grid(row=1, sticky=E)
        self.label_id_add_window.grid(row=2, sticky=E)

        self.label_id_update_window = Label(self.update_window, text="ID")
        self.label_name_update_window = Label(self.update_window, text="Name")
        self.label_type_update_window = Label(self.update_window, text="Type")
        self.label_id_update_window.grid(row=0, column=0, sticky=E)
        self.label_name_update_window.grid(row=1, column=0, sticky=E)
        self.label_type_update_window.grid(row=2, column=0, sticky=E)

        self.id_text_input_add_window = Text(self.window, height=1, width=20)
        self.name_text_input_add_window = Text(self.window, height=1, width=20)
        self.type_text_input_add_window = Combobox(self.window, values=["Cat", "Dog", "Hamster", "Mouse",
                                                                   "Fish", "Hedgehog", "Parrot",
                                                                   "Tortoise", "Snake"])
        self.name_text_input_add_window.grid(row=0, column=1, sticky=E)
        self.type_text_input_add_window.grid(row=1, column=1, sticky=E)
        self.id_text_input_add_window.grid(row=2, column=1, sticky=E)

        self.text_name_update_window = Text(self.update_window, height=1, width=20)
        self.text_name_update_window.grid(row=1, column=1, sticky=E)
        self.text_type_update_window = Combobox(self.update_window, values=["Cat", "Dog", "Hamster", "Mouse",
                                                                   "Fish", "Hedgehog", "Parrot",
                                                                   "Tortoise", "Snake"])
        self.text_type_update_window.grid(row=2, column=1, sticky=E)

        self.add_button_add_window = Button(self.window, text="Add")
        self.print_button_add_window = Button(self.window, text="Print")
        self.add_button_add_window.grid(row=3, column=0)
        self.print_button_add_window.grid(row=3, column=1)

        self.label_name_delete_window = Label(self.delete_window, text="Pet ID")
        self.label_name_delete_window.grid(row=1, column=0, sticky=E)

        self.button_back_window = Button(self.delete_window, text="Back")
        self.button_delete_window = Button(self.delete_window, text="Delete")
        self.button_delete_window.grid(row=1, column=2, sticky=E)
        self.button_back_window.grid(row=2, column=2, sticky=E)

        self.combo_box_delete_animals_window = Combobox(self.delete_window)
        self.combo_box_delete_animals_window.grid(row=1, column=1, sticky=E)

        self.combo_box_update_animals_window = Combobox(self.update_window)
        self.combo_box_update_animals_window.grid(row=0, column=1, sticky=E)

        self.button_back_update_window = Button(self.update_window, text="Back")
        self.button_back_update_window.grid(row=3, column=0, sticky=E)

        self.button_update_update_window = Button(self.update_window, text="Update")
        self.button_update_update_window.grid(row=3, column=1, sticky=E)

        self.delete_window.withdraw()
        self.update_window.withdraw()

    def get_add_button_add_window(self):
        return self.add_button_add_window

    def get_print_button_add_window(self):
        return self.print_button_add_window

    def get_button_back_update_window(self):
        return self.button_back_update_window

    def get_button_update_update_window(self):
        return self.button_update_update_window

    def get_window(self):
        return self.window

    def get_id_text_input_add_window(self):
        return self.id_text_input_add_window.get("1.0", END)

    def get_name_text_input_add_window(self):
        return self.name_text_input_add_window.get("1.0", END)

    def get_type_text_input_add_window(self):
        return self.type_text_input_add_window

    def get_text_id_update_window(self):
        return self.combo_box_update_animals_window.get()

    def get_text_name_update_window(self):
        return self.text_name_update_window.get("1.0", END)

    def get_text_type_update_window(self):
        return self.text_type_update_window

    def get_file_menu(self):
        return self.file_menu

    def hide_window(self):
        self.window.withdraw()
        self.delete_window.update()
        self.delete_window.deiconify()

    def show_window(self):
        self.window.update()
        self.window.deiconify()
        self.delete_window.withdraw()

    def hide_delete_window(self):
        self.delete_window.withdraw()
        self.window.update()
        self.window.deiconify()

    def show_delete_window(self):
        self.delete_window.update()
        self.delete_window.deiconify()
        self.window.withdraw()

    def hide_update_window(self):
        self.update_window.withdraw()
        self.window.update()
        self.window.deiconify()

    def show_update_window(self):
        self.update_window.update()
        self.update_window.deiconify()
        self.window.withdraw()

    def get_label_name_delete_window(self):
        return self.label_name_delete_window

    def get_delete_button_back_window(self):
        return self.button_back_window

    def get_delete_button_delete_window(self):
        return self.button_delete_window

    def get_combo_box_delete_animals_window(self):
        return self.combo_box_delete_animals_window

    def update_combobox(self, list1):
        self.combo_box_delete_animals_window.config(values=list1)

    def update_combobox_update_window(self, list1):
        self.combo_box_update_animals_window.config(values=list1)

