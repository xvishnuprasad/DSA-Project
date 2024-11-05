# Data Structures in Python and HTML Server

Welcome to the repository containing implementations of fundamental data structures: **Linked List** and **Stack**. These data structures are implemented using Python and incorporate an HTML server for input and output functionality.

## 📂 Project Structure

- `LinkedList/`
  - `linked_list.py`: Python implementation of a Doubly Linked List.
  - `server.html`: HTML file used for displaying and receiving input for Linked List operations.
  - `server.py`: Python script to connect the Linked List logic with the HTML server.

- `StackUsingArray/`
  - `stack_array.py`: Python implementation of a Stack using an Array.
  - `server.html`: HTML file used for displaying and receiving input for Stack operations using an Array.
  - `server.py`: Python script to connect the Stack Array logic with the HTML server.

- `StackUsingLinkedList/`
  - `stack_linkedlist.py`: Python implementation of a Stack using a Linked List.
  - `server.html`: HTML file used for displaying and receiving input for Stack operations using a Linked List.
  - `server.py`: Python script to connect the Stack Linked List logic with the HTML server.

---

## 📘 Linked List

### Features
- **Doubly Linked List Implementation**
- Supports operations like:
  - Insertion (at the beginning, end, and specific positions)
  - Deletion (from the beginning, end, and specific positions)
- Interfaced with an HTML server for easy interaction and visualization

### Usage
1. Run the `server.py` script to start the HTML server.
2. Use the `server.html` file to input data and perform operations.
3. The results will be displayed on the HTML page.

### Code Snippet
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
