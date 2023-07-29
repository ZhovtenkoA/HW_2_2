from AddressBook import *
from visualization import MyView


class Bot:
    def __init__(self):
        self.view = MyView()
        self.book = AddressBook(self.view)

    def add_record(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        self.book.add(record)

    def search_record(self):
        self.view.display_categories()
        category = input("Search category: ")
        pattern = input("Search pattern: ")
        search_result = self.book.search(pattern, category)
        self.view.display_found_contacts(search_result)

    def edit_record(self):
        contact_name = input("Contact name: ")
        parameter = input(
            "Which parameter to edit(name, phones, birthday, status, email, note): "
        ).strip()
        new_value = input("New Value: ")
        self.book.edit(contact_name, parameter, new_value)

    def remove_record(self):
        pattern = input("Remove (contact name or phone): ")
        self.book.remove(pattern)

    def save_record(self):
        file_name = input("File name: ")
        self.book.save(file_name)

    def load_record(self):
        file_name = input("File name: ")
        self.book.load(file_name)

    def congratulate_someone(self):
        self.book.congratulate()

    def view_record(self):
        self.view.display_contacts(self.book)

    def handle(self, action):
        if action == "add":
            self.add_record()
        elif action == "search":
            self.search_record()
        elif action == "edit":
            self.edit_record()
        elif action == "remove":
            self.remove_record()
        elif action == "save":
            self.save_record()
        elif action == "load":
            self.load_record()
        elif action == "congratulate":
            self.congratulate_someone()
        elif action == "view":
            self.view_record()
        elif action == "exit":
            pass
        else:
            print("There is no such command!")
