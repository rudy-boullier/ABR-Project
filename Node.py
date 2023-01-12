class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def plantAbr(self, value: float):
        if self is None:
            return Node(value)
        elif value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.plantAbr(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.plantAbr(value)
        return self
