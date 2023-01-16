class Node:
    """
    A class representing a node of an ABR.
    ...
    Attributes
    ----------
    value : float | int     the value of the node
    """
    def __init__(self, value):
        """
        Parameters
        ----------
        :param value: float | int
        """
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: float | int):
        """
        Insert a new node in the ABR.
        Parameters
        ----------
        :param value: float | int
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        # the value go to the right if the value is greater or egal than the value of the node
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
