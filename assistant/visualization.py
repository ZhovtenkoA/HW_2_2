from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def display_commands(self, commands):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_found_contacts(self, contacts):
        pass

    @abstractmethod
    def display_categories(self):
        pass

    @abstractmethod
    def display_hello(self):
        pass

    @abstractmethod
    def display_bye(self):
        pass

    @abstractmethod
    def show_info(self, message):
        pass

    @abstractmethod
    def show_error(self, message):
        pass


class MyView(View):
    def display_commands(self):
        self.commands = [
            "Add",
            "Search",
            "Edit",
            "Load",
            "Remove",
            "Save",
            "Congratulate",
            "View",
            "Exit",
        ]
        print("List of available commands:")
        for command in self.commands:
            print(f"-{command}")

    def display_contacts(self, address_book):
        address_book_iter = iter(address_book)
        print("List of contacts:")
        print("__________________________________________________")
        for contact in address_book_iter:
            print(f"Name: {contact['name']}")
            print(f"Phones: {', '.join(contact['phones'])}")
            print(f"Birthday: {contact['birthday']}")
            print(f"Email: {contact['email']}")
            print(f"Type of relationship: {contact['status']}")
            print(f"Note: {contact['note']}")
            print("__________________________________________________")

    def display_found_contacts(self, contacts):
        if contacts:
            result = []
            print("List of contacts:")
            print("__________________________________________________")
            for contact in contacts:
                if contact["birthday"]:
                    birth = contact["birthday"].strftime("%d/%m/%Y")
                else:
                    birth = ""
                if contact["phones"]:
                    new_value = []
                    for phone in contact["phones"]:
                        if phone:
                            new_value.append(phone)
                    phone = ", ".join(new_value)
                else:
                    phone = ""
                result.append(
                    f"Name: {contact['name']} \nPhones: {phone} \nBirthday: {birth} \nEmail: {contact['email']} \nStatus: {contact['status']} \nNote: {contact['note']}"
                )
                print(f"\n".join(result))
                print("__________________________________________________")
        else:
            print("There are no contacts found.")

    def display_categories(self):
        self.categories = ["Name", "Phones", "Birthday", "Email", "Status", "Note"]
        print("There are following categories:")
        for category in self.categories:
            print(f"-{category}")

    def display_hello(self):
        print(
            "Hello. I am your contact-assistant. What should I do with your contacts?"
        )

    def display_bye(self):
        print("Good bye. See you next time!")

    def show_info(self, message):
        print(message)

    def show_error(self, message):
        print(message)
