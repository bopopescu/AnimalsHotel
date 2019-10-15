class Controller:

    list = []

    def __init__(self, view1, model1):
        self.view1 = view1
        self.model1 = model1
        self.view1.get_file_menu().add_command(label="Delete Item", command=lambda: [view1.hide_window(), view1.update_combobox(model1.get_animal_list())])
        self.view1.get_file_menu().add_command(label="Update Item", command=lambda: [view1.show_update_window(), view1.update_combobox_update_window(model1.get_animal_list())])
        self.view1.get_add_button_add_window().config(command=lambda: model1.add_animal(view1.get_id_text_input_add_window(), view1.get_name_text_input_add_window(), view1.get_type_text_input_add_window().get()))
        self.view1.get_print_button_add_window().config(command=lambda: model1.print_all_animals())
        self.view1.get_delete_button_back_window().config(command=view1.hide_delete_window)
        self.view1.get_delete_button_delete_window().config(command=lambda: [model1.delete_animal_by_id(view1.get_combo_box_delete_animals_window().get()),
                                                                             view1.update_combobox(model1.get_animal_list())])
        self.view1.get_button_back_update_window().config(command=lambda: [view1.hide_update_window(), view1.show_window()])
        self.view1.get_button_update_update_window().config(command= lambda: [model1.update_animal_by_id(view1.get_text_id_update_window(),
                                                                                                        view1.get_text_name_update_window(),
                                                                                                        view1.get_text_type_update_window().get())])
        self.view1.get_add_button_add_window().mainloop()



