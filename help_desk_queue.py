# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front: 
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if not self.front: 
            self.rear = None
        return removed_value

    def peek(self):
        if not self.front:
            return None
        return self.front.value

    def print_queue(self):
        current = self.front
        if not current:
            print("(empty)")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"Helped: {customer}")
            else:
                print("No customers in the queue.")

        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers in the queue.")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

#a stack is the right choice for undo/redo because it works in a last-In, first-Out way. The last action a user does should be the first one undone. For example, if someone types several names, the most recent name should be removed first when they hit undo. Using a stack, each action is added to the top and removed from the top, which matches how undo and redo operations need to work.
#a queue is better for a help desk because it works in a first-In, first-Out way. The first person to ask for help should be served first. Queues keep requests in order, so everyone gets help in the order they arrived. While Python lists can be used for stacks and queues, the way we use them is different. Stacks only add or remove from the end, and queues add at one end and remove from the other. This makes stacks and queues easier to use for these taks.