class Node:     #create node object
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:      #create object for singly linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self): #method to iterate linked list
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):    #append items on linked list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def remove_head(self):  #remove item from head
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None


def main():
    items = singly_linked_list()

    while True:
        print('''
        Select option:
        [a] Add items to linked list
        [b] Remove items from head of linked list
        [any char] Exit
        '''
        )
        choice = input("Enter choice: ")

        if (choice == 'a' or choice == 'A'):
            add_elements = int(input("\nHow many items to add? "))
            for i in range(add_elements):
                add_item = input(f"Element #{i + 1}: ")
                items.append_item(add_item)

            print("\nIterate items in linked list: ")
            for val in items.iterate_item():
                print(val)

            print("\nhead.data: ",items.head.data)
            print("\ntail.data: ",items.tail.data)


        elif (choice == 'b' or choice == 'B'):
            remove_elements = int(input("\nHow many elements to remove? "))
            for j in range(remove_elements):
                items.remove_head()

            print("\nIterate current items in linked list: ")
            for val in items.iterate_item():
                print(val)

            print("\nhead.data: ",items.head.data)
            print("\ntail.data: ",items.tail.data)


        else:
            print("Loop terminated.")
            break

if __name__ == "__main__":
    main()