class Node:
    """
    A class representing a node of an ABR.
    ...
    Attributes
    ----------
    val : float
        the value of the node
    """
    def __init__(self, value):
        """
        Parameters
        ----------
        :param value: float
        """
        self.val = value
        self.left = None
        self.right = None

    def plantAbr(self, value: float):
        """
        Plant a new node in the ABR.
        Parameters
        ----------
        :param value: float
        """
        if self is None:
            return Node(value)
        elif value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.plantAbr(value)
        # the value go to the right if the value is greater or egal than the value of the node
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.plantAbr(value)
        return self
