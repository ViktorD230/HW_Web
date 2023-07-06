from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, number):
        super().__init__(Field)
        self.number = number

    def __str__(self):
        return self.number

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError


class Birthday(Field):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid date format. Please use the format: DD-MM-YYYY")
        try:
            datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use the format: DD-MM-YYYY")
