from utils.decorator import decorator_maker



class Contact:

    def __init__(self, name, surname, phone, favorite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favorite = favorite
        self.other_list = []
        self.other_dic = {}

        for value in args:
            self.other_list.append(value)

        for key, value in kwargs.items():
            self.other_dic[key] = value

    def __str__(self):

        other_list_string = ''
        other_dic_string = ''

        def return_word():
            if self.favorite:
                return 'да'
            else:
                return 'нет'

        main_string = f' Имя: {self.name} \n Фамилия: {self.surname} \n Телефон: {self.phone} \n ' \
            f'В избранных: {return_word()} \n Дополнительная информация: \n '

        for item in self.other_list:
            other_list_string += f'\t \t {item} \n'

        for key in self.other_dic.keys():
            other_dic_string += f'\t \t {key} : {self.other_dic[key]} \n'

        return main_string + other_list_string + other_dic_string


class PhoneBook:
    phonebook = []

    def __init__(self, name):
        self.book_name = name

# Декоратор записывает лог запуска метода в файл
    @decorator_maker('log.txt')
    def add_contact(self, name, surname, phone, *args, **kwargs):
        new_contact = Contact(name, surname, phone,  *args, **kwargs)
        self.phonebook.append(new_contact)
        return new_contact

    def show_contacts(self):
        for contact in self.phonebook:
            print(contact)

    def del_contact(self, phone):
        for position, contact in enumerate(self.phonebook):
            if phone in str(contact):
                self.phonebook.pop(position)

    def search_favorite_contact(self):
        for contact in self.phonebook:
            if contact.favorite:
                print(contact)

    def search_contact_by_name(self, name, surname):
        for contact in self.phonebook:
            if name and surname in str(contact):
                print(contact)


if __name__ == '__main__':
    a = PhoneBook('First phonebook')

    a.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    a.add_contact('Allford', 'Jenkin', '+2123482626', telegram='@jenkin', email='jenkin@smith.com')
    a.add_contact('Audley', 'Kingsman', '+2029398907', True, '+12025912173', telegram='@kingsman',
                  email='kingsman@smith.com', test='Kingsman Audley')

    
