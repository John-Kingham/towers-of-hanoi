from node import Node


class Stack:
    """
    A stack of values.
    """

    def __init__(self, name, limit=1000):
        """
        Creates a new ``Stack`` with a size limit of ``limit`.
        """
        self.top_item = None
        self.name = name
        self.size = 0
        self.limit = limit

    def push(self, value):
        """
        Pushes ``value`` onto the top of the stack.
        """
        if self.has_space() is False:
            print("Cannot push as the stack has no space.")
        else:
            new_top = Node(value)
            new_top.set_next_node(self.top_item)
            self.top_item = new_top
            self.size += 1

    def pop(self):
        """
        Removes and returns the value at the top of the stack, or None.
        """
        if self.is_empty():
            print("Cannot pop as the stack is empty.")
            return None
        else:
            old_top = self.top_item
            self.top_item = old_top.get_next_node()
            self.size -= 1
            return old_top.get_value()

    def peek(self):
        """
        Returns the value at the top of the stack, but doesn't remove it.
        """
        if self.is_empty():
            print("Cannot peek as the stack is empty.")
            return None
        else:
            return self.top_item.get_value()

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.limit

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    # returns a string representation of the stack
    def to_string(self):
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        return f"{self.get_name()} Stack: {print_list}"
