class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            print('Stack is empty.')
        else:
            item_popped = self.stack.pop()
            print(f'Item {item_popped} has been popped.')

    def display_stack(self):
        return f'Current stack: {self.stack}'


def main():
    while True:
        myStack = Stack()
        list_size = int(input('\nHow many elements to push? '))
        for i in range(list_size):
            input_element = input(f'Element {i+1}: ')
            myStack.push(input_element)

        print()
        print(myStack.display_stack())

        print(f'Top element: {myStack.stack[-1]}')      #peeks topmost element remaining

        pop_elements = int(input('\nHow many elements to pop? '))
        for j in range(pop_elements):
            myStack.pop()

        print()
        print(myStack.display_stack())

        print(f'Top element: {myStack.stack[-1]}')      #peeks topmost element remaining

        print()
        choose = input('Try again? [Y] Yes      [Any char] No: ')
        if choose == 'y' or choose == 'Y':
            pass
        else:
            print('\nLoop terminated.')
            break



if __name__ == '__main__':
    main()