from flask import Flask, render_template, request, redirect

# Doubly Linked List Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append an element to the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Method to insert an element at a specific position
    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:  # Insert at the head
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        index = 0
        while current and index < position - 1:
            current = current.next
            index += 1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    # Method to delete an element by its value
    def delete(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if current is None:
            print("Element not found")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:  # If deleting the head node
            self.head = current.next

    # Method to display the list elements
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create Flask app
app = Flask(__name__)

# Initialize the doubly linked list and add some initial data
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

# Define the route to display the linked list and accept input for adding, inserting, and deleting
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'add_element' in request.form:
            # Add new element to the list (append)
            element = request.form['element']
            dll.append(int(element))
        
        elif 'insert_element' in request.form:
            # Insert element at a specific position
            element = request.form['insert_element']
            position = request.form['position']
            dll.insert_at(int(element), int(position))

        elif 'delete_element' in request.form:
            # Delete element by value
            element = request.form['delete_element']
            dll.delete(int(element))

        return redirect('/')  # Redirect to the home page to refresh

    # Display the linked list
    linked_list_data = dll.display()
    return render_template('index.html', linked_list_data=linked_list_data)

if __name__ == '__main__':
    app.run(debug=True)
