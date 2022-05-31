from collections import UserDict
from typing import List


class Field:
    def __init__(self, value: str) -> None:
        self.value = value.title()


class Name(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Phone(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Record:
    def __init__(self, name: Name, phons: List[Phone] = []) -> None:
        self.name = name
        self.phones = phons

    def change_phone(self, phone: Phone, new_phone: Phone):
        if self.remove_record(phone):
            self.phones.append(new_phone)
            return new_phone

    def remove_record(self, phone: Phone):
        for i, phone in enumerate(self.phones):
            if phone.value == phone.value:
                return self.phones.pop(i)

    def __repr__(self) -> str:
        return f"{self.name.value}:{[p.value for p in self.phones]}"


class AddressBook(UserDict):

    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return """If you write command 'add' please write 'add' 'name' 'number'
If you write command 'change' please write 'change' 'name' 'number'
If you write command 'phone' please write 'phone' 'name'
If you write command 'remove' please write 'remove' 'name' 'number'"""
        except KeyError:
            return "..."
        except TypeError:
            return "..."
    return wrapper


def input_help():
    return """help - output command, that help find command
hello - output command 'How can I help you?' 
add - add contact, use 'add' 'name' 'number'
change - change your contact, use 'change' 'name' 'number'
phone - use 'phone' 'name' that see number this contact
show all - show all your contacts
"""


@input_error
def input_bye(*args):
    return "Good bye"


@input_error
def input_hello(*args):
    return "How can I help you?"


ab = AddressBook()


@input_error
def input_add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, [phone])
    print(rec)
    ab.add_record(rec)
    return f"Contact {rec.name.value.title()} add successful"


@input_error
def input_change(*args):
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec = ab.data[args[0].title()]
    result = rec.change_phone(phone, new_phone)
    if result:
        return f"Contact {rec.name.value.title()} change successful"


@input_error
def input_phone(*args):
    return ab.get(args[0].title())


@input_error
def input_show(*args):
    return "\n".join([f"{v} " for v in ab.values()])


@input_error
def input_remove(*args):
    phone = Phone(args[1])
    rec = ab.data[args[0].title()]
    result = rec.remove_record(phone)
    if result:
        return f"Phone {phone.value} remove successful"


commands = {
    input_hello: "hello",
    input_add: "add",
    input_phone: "phone",
    input_show: "show all",
    input_change: "change",
    input_bye: "good bye",
    input_help: "help",
    input_remove: "remove"
}


def command_parser(user_input1):
    data = []
    command = ""
    for k, v in commands.items():
        if user_input1.startswith(v):
            command = k
            data = user_input1.replace(v, "").split()
        if user_input1 == "":
            main()
    return command, data


@input_error
def main():
    while True:
        user_input = input(">>>")
        user_input1 = user_input.lower()
        command, data = command_parser(user_input1)
        print(command(*data))
        if command == input_bye:
            break


if __name__ == "__main__":
    main()
