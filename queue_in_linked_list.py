class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0


    def iterate(self):
        current_item = self.front
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val


    def getLength(self):
        temp = self.front
        count = 0

        while(temp):
            count += 1
            temp = temp.next

        return count
    

    def enqueue(self, data):
        node = Node(data)
        if self.rear == None:
            self.front = node  #instantiation
            self.rear = self.front
        else:
            self.rear.next = node
            self.rear = self.rear.next


    def dequeue(self):
        if self.front == None:
            return None
        else:
            val_return = self.front.data
            self.front = self.front.next
            return val_return


def main():
    items = Queue()
    while True:
        print(
'''
Select option:
[a] Enqueue item
[b] Dequeue rear item
[c] Get Length
[d] Display
[any char] Exit
'''
            )
        choice = input("Enter choice here: ")
        if (choice == 'a' or choice == 'A'):
            add_elements = int(input("How many elements to enqueue? "))
            for i in range(add_elements):
                add_item = input(f"Element #{i + 1}: ")
                items.enqueue(add_item)

        elif (choice == 'b' or choice == 'B'):
            remove_elements = int(input("How many elements to dequeue? "))
            for j in range(remove_elements):
                items.dequeue()

        elif (choice == 'c' or choice == 'C'):
            print(f"Size of linked list: {items.getLength()}")

        elif (choice == 'd' or choice == 'D'):
            print("Display items: ")
            for val in items.iterate():
                print(val)

            print("\nfront.data:", items.front.data)
            print("\nrear.data", items.rear.data)

        else:
            print("Loop terminated.")
            break
            
if __name__ == "_main_":
    main()