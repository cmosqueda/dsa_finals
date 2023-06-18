class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            print('Queue is empty.')
        else:
            item_dequeued = self.queue.pop(0)
            print(f'Item {item_dequeued} has been dequeued.')

    def display_queue(self):
        return f'Current queue: {self.queue}'


def main():
    while True:
        myQueue = Queue()
        list_size = int(input('\nHow many elements to enqueue? '))
        for i in rang(list_size):
            input_element = input(f'Element {i+1}: ')
            myQueue.enqueue(input_element)

        print()
        print(myQueue.display_queue())

        dequeue_elements = int(input('\nHow many elements to dequeue? '))
        for j in range(dequeue_elements):
            myQueue.dequeue()

        print()
        print(myQueue.display_queue())

        print()
        choose = input('Try again?  [Y] Yes     [Any char] No: ')
        if choose == 'y' or choose == 'Y':
            pass
        else:
            print('\nLoop terminated.')
            break


if __name__ == '__main__':
    main()