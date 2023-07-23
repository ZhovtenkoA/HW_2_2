from datetime import datetime as dt, timedelta
from collections import UserList
import pickle
from info import *
import os
from visualization import *


class AddressBook(UserList):
    def __init__(self, view):
        super().__init__()
        self.counter = -1
        self.view = view
        self.index = 0

    def __next__(self):
        if self.index < len(self.data):
            contact = self.data[self.index]
            self.index += 1
            return contact
        else:
            raise StopIteration

    def __iter__(self):
        return self


    def __setitem__(self, index, record):
        self.data[index] = {'name': record.name,
                            'phones': record.phones,
                            'birthday': record.birthday,
                            'email': record.email}

    def __getitem__(self, index):
        return self.data[index]

    def log(self, action):
        current_time = dt.strftime(dt.now(), '%H:%M:%S')
        message = f'[{current_time}] {action}'
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')

    def add(self, record):
        account = {'name': record.name,
                   'phones': record.phones,
                   'birthday': record.birthday,
                   'email': record.email,
                   'status': record.status,
                   'note': record.note}
        self.data.append(account)
        self.view.show_info(f"Contact {record.name} has been added.")
        self.log(f"Contact {record.name} has been added.")

    def save(self, file_name):
        with open(file_name + '.bin', 'wb') as file:
            pickle.dump(self.data, file)
        self.log("Addressbook has been saved!")
        self.view.show_info("Addressbook has been saved! Great job")


    def load(self, file_name):
        if not os.path.exists(file_name + '.bin'):
            self.view.show_error(f"File {file_name}.bin does not exist!")
            self.log('Addressbook has been created!')
            return []
        with open(file_name + '.bin', 'rb') as file:
            self.data = pickle.load(file)
        self.view.show_info("Addressbook has been loaded! Great job")
        self.log("Addressbook has been loaded!")
        return self.data


    def search(self, pattern, category):
        result = []
        category_new = category.strip().lower().replace(' ', '')
        pattern_new = pattern.strip().lower().replace(' ', '')

        for account in self.data:
            if category_new == 'phones':
                for phone in account['phones']:
                    if phone.lower().startswith(pattern_new):
                        result.append(account)
            elif account[category_new].lower().replace(' ', '') == pattern_new:
                result.append(account)

        if not result:
            self.view.show_error('There is no such contact in address book!')
        else:
            return result

    def edit(self, contact_name, parameter, new_value):
        names = []
        try:
            for account in self.data:
                names.append(account['name'])
                if account['name'] == contact_name:
                    if parameter == 'birthday':
                        new_value = Birthday(new_value, '%d/%m/%Y')
                    account[parameter] = new_value
                    self.view.show_info(
                        f"{parameter} for {contact_name} has been updated!")
                    self.log(
                        f"{parameter} for {contact_name} has been updated!")
                    return
            if contact_name not in names:
                self.view.show_error(
                    f"There is no {contact_name} in address book!")
        except KeyError:
            self.view.show_error(f"{parameter} is not a valid parameter!")

    def remove(self, contact_name):
        for account in self.data:
            if account['name'] == contact_name:
                self.data.remove(account)
                self.view.show_info(
                    f"{contact_name} has been removed from address book!")
                self.log(f"{contact_name} has been removed from address book!")
                return
        self.view.show_error(f"There is no {contact_name} in address book!")

    def congratulate(self):
        today = dt.now().date()
        week_start = today - timedelta(today.weekday())
        week_end = week_start + timedelta(6)
        result = []
        for account in self.data:
            if account['birthday'] and week_start <= account['birthday'].date() <= week_end:
                result.append(account)
        if not result:
            self.view.show_info("There are no birthdays this week!")
        else:
            for account in result:
                self.view.show_info(
                    f"{account['name']}'s birthday is on {account['birthday'].strftime('%d/%m/%Y')}!")

