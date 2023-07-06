from datetime import date
from fields import Name, Phone, Birthday


class Record:
    def __init__(self, name: Name, birthday: Birthday = None):
        self.name = name
        self.phones = []
        self.birthday = None

        if birthday:
            self.birthday = birthday.value

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def set_birthday(self, birthday: Birthday):
        self.birthday = birthday.value

    def remove_birthday(self):
        self.birthday = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday):
        if new_birthday is None:
            self._birthday = None
        else:
            self._birthday = new_birthday

    def days_to_birthday(self) -> int:
        if self.birthday is None:
            return -1

        today = date.today()
        next_birthday = date(today.year, self.birthday.month, self.birthday.day)

        if today > next_birthday:
            next_birthday = date(today.year + 1, self.birthday.month, self.birthday.day)

        days_until_birthday = (next_birthday - today).days
        return days_until_birthday


class RecordIterator:
    def __init__(self, records):
        self.records = records
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.records):
            raise StopIteration
        record = self.records[self.index]
        self.index += 1
        return record
