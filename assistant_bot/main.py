from utils.adress_book_manager import AddressBook
from parsing.parser import parse_input
from utils.serialize import *
from handlers.handler import *


def main():
    """
Main contains the basic functionality of the bot assistant application.
It handles user interactions such as adding, modifying and displaying contacts.

Update 0.6 :
   - formatted address book display with emoji
   - added serialize module (for save/load -> to/from file)
   - program structure modules are grouped into folders

Commands:
    - hello : Just a greeting.
    - add <name> <phone> : Adds a new contact.
    - mod <name> <new_phone>: Updates an existing contact.
    - del <name> Deletes an existing contact.
    - phone <name>: Displays the contact's phone number.
    - all: Displays all contacts.
    - clear: Deletes all contacts.  
    - add-b <name> <DD.MM.YYYY> : Adds a birthday date
    - show-b <name> : Shows a birthday date
    - b-days : displays a list of birthdays for the next 7 days
    - exit or close: Exits the program.
  """
    
    DATA = 'book.pkl'
    book = load_from_file(DATA)
    print(book)
    
    print('WELCOME to the ASSISTANT BOT!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        match command:
            case 'hello': 
                print('How can I help you?')
            case 'add': 
                print(add_contact(args, book))
            case 'mod': 
                print(modify_contact(args, book))
            case 'del':
                print(delete_contact(args, book))
            case 'phone':
                print(show_phone(args, book))            
            case 'all':
                print(show_all(book))           
            case 'clear':
                print(clear_all_contacts(book))
            case 'add-b':
                print(add_birthday(args, book))
            case 'show-b':
                print(show_birthday(args, book))
            case 'b-days':
                print(birthdays(args, book))                      
            case 'exit' | 'close':
                save_to_file(book, DATA)
                print('Good bye!\n')
                break
            case _ :
                print('Invalid command')


if __name__ == '__main__':
    main()
