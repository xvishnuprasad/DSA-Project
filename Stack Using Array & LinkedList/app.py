from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Stack implementation using an array
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack.copy()

# Node class for the linked list stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack implementation using a linked list
class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Global instances of both stacks
array_stack = ArrayStack()
linked_list_stack = LinkedListStack()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/array/push', methods=['POST'])
def push_array():
    data = request.json.get('data')
    array_stack.push(data)
    return jsonify(array_stack.display())

@app.route('/array/pop', methods=['POST'])
def pop_array():
    popped = array_stack.pop()
    return jsonify({"popped": popped, "stack": array_stack.display()})

@app.route('/linkedlist/push', methods=['POST'])
def push_linked_list():
    data = request.json.get('data')
    linked_list_stack.push(data)
    return jsonify(linked_list_stack.display())

@app.route('/linkedlist/pop', methods=['POST'])
def pop_linked_list():
    popped = linked_list_stack.pop()
    return jsonify({"popped": popped, "stack": linked_list_stack.display()})

@app.route('/array/display', methods=['GET'])
def display_array():
    return jsonify(array_stack.display())

@app.route('/linkedlist/display', methods=['GET'])
def display_linked_list():
    return jsonify(linked_list_stack.display())

if __name__ == '__main__':
    app.run(debug=True)
