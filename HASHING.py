SIZE = 10
phonebook = [None] * SIZE

def add_client():
    client_id = int(input("Enter Client ID: "))
    name = input("Enter Client Name: ")
    number = input("Enter Telephone Number: ")
    record = [client_id, name, number]

    index = client_id % SIZE

    for i in range(SIZE):
        new_index = (index + i) % SIZE
        if phonebook[new_index] is None:
            phonebook[new_index] = record
            print(f"Client added at index {new_index}.")
            return
    print("Phonebook is full! Cannot add more clients.")

def search_client():
    client_id = int(input("Enter Client ID to search: "))
    index = client_id % SIZE

    for i in range(SIZE):
        new_index = (index + i) % SIZE
        if phonebook[new_index] is None:
            break
        if phonebook[new_index][0] == client_id:
            print(f"Client found at index {new_index}: {phonebook[new_index]}")
            return
    print("Client not found.")

def display_phonebook():
    print("\nPhonebook Contents:")
    for i in range(SIZE):
        print(f"Index {i}: {phonebook[i]}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Client")
        print("2. Search Client")
        print("3. Display Phonebook")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            search_client()
        elif choice == '3':
            display_phonebook()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
