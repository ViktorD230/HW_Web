from typing import List
from abc import ABC, abstractmethod


class BaseView(ABC):
    @abstractmethod
    def display_message(self, message: str) -> None:
        pass

    @abstractmethod
    def display_contacts(self, contacts: List[str]) -> None:
        pass

    @abstractmethod
    def display_commands(self) -> None:
        pass


class ConsoleView(BaseView):
    def display_message(self, message: str) -> None:
        print(message)

    def display_contacts(self, contacts: List[str]) -> None:
        for contact in contacts:
            print(contact)

    def display_commands(self) -> None:
        commands = [
            "Commands:",
            " hello",
            " add <name> <phone1> <phone2> ...",
            " change <name> <old_phone> <new_phone>",
            " phone <name>",
            " show all",
            " birthday <name> <dd-mm-yyyy>",
            " paginate <page_size>",
            " search <query>",
            " close/exit/good bye",
        ]
        print("\n".join(commands))
