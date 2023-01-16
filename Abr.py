import DrawABR as Draw
import Node


class Abr:
    def __init__(self, canvas):
        """
        Init the ABR classe
        :param canvas: Canvas
        """
        self.tree = None
        self.canvas = canvas

    '''-------------------------------------- Add --------------------------------------'''

    def create_abr(self, data):
        """
        Create an abr tree from a list of values
        :param data: list of float
        :return: Node, an abr tree
        """
        for value in data:
            if self.tree is None:
                self.tree = Node.Node(value)
            else:
                self.tree.insert(value)
        return self.tree

    def add_value_abr(self, value: float, file):
        """
        Add value to an abr tree
        :param value: float
        :param file: File
        """
        if self.tree is None:
            self.tree = Node.Node(value)
        else:
            self.tree.insert(value)
        file.updateData(self.tree)
        self.update_display_abr(self.canvas)

    '''-------------------------------------- Delete --------------------------------------'''

    def supp_value_abr(self, value: float, file):
        """
        Delete a node in an abr tree
        :param value: float
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.remove_node(self.tree, value)
            file.updateData(self.tree)
            self.update_display_abr(self.canvas)

    def remove_node(self, node: Node, value: float) -> Node:
        """
        Delete a node in an abr tree, the node is the first node with the value
        When a node is deleted, minval of the right subtree is used to replace the deleted node
        :param node: Node
        :param value: float
        :return: Node | None
        """
        if node is None:
            return None
        if value != node.val:
            tmp = self.research_node(node, value)
            if tmp is not None:
                node = tmp
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        min_node = self.min_abr(node.right)
        node.value = min_node.value
        node.right = self.remove_node(node.right, node.value)
        return node

    def remove_node2(self, node: Node, value: float):  # not implemented
        """
        Delete a node in an abr tree, the node is the first node with the value
        When a node is deleted, maxval of the left subtree is used to replace the deleted node
        :param node: Node
        :param value: float
        :return: Node | None
        """
        if node is None:
            return
        if value != node.val:
            tmp = self.research_node(node, value)
            if tmp is not None:
                node = tmp
        if node.left is None:
            node = node.right
            return node
        elif node.right is None:
            node = node.left
            return node
        biggest = self.max_abr(node.left)
        node.value = biggest.val
        node.left = self.remove_node2(node.left, biggest.val)
        return node

    '''---------- extreme node ----------'''
    def supp_extreme_right_value_abr(self, file):
        """
        Execute to delete of extreme right node in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.delete_extreme_right(self.tree)
            file.updateData(self.tree)
            self.update_display_abr(self.canvas)

    def delete_extreme_right(self, node: Node) -> Node:
        """
        Delete the extreme right node of an abr tree
        :param node:
        :return: node
        """
        if node.right is None:
            return node.left
        node.right = self.delete_extreme_right(node.right)
        return node

    def supp_extreme_left_value_abr(self, file):
        """
        Execute to delete of extreme left node in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.delete_extreme_left(self.tree)
            file.updateData(self.tree)
            self.update_display_abr(self.canvas)

    def delete_extreme_left(self, node):
        """
        Delete the extreme left node of an abr tree
        :param node: Node
        :return: node
        """
        if node.left is None:
            return node.right
        node.left = self.delete_extreme_left(node.left)
        return node

    '''---------- extreme leaf ----------'''

    def supp_extreme_right_leaf_abr(self, file):
        """
        Execute to delete of extreme right leaf in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.delete_extreme_right_leaf(self.tree)
            file.updateData(self.tree)
            self.update_display_abr(self.canvas)

    def delete_extreme_right_leaf(self, node: Node) -> Node:
        """
        Delete the extreme right leaf of an abr tree
        :param node:
        :return: Node
        """
        if node.right is None:
            return node.left
        if node.right.left is None and node.right.right is None:
            node.right = None
            return node
        node.right = self.delete_extreme_right_leaf(node.right)
        return node

    def supp_extreme_left_leaf_abr(self, file):
        """
        Execute to delete of extreme left leaf in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.delete_extreme_left_leaf(self.tree)
            file.updateData(self.tree)
            self.update_display_abr(self.canvas)

    def delete_extreme_left_leaf(self, node: Node) -> Node:
        """
        Delete the extreme left leaf of an abr tree
        :param node:
        :return: Node
        """
        if node.left is None:
            return node.right
        if node.left.left is None and node.left.right is None:
            node.left = None
            return node
        node.left = self.delete_extreme_left_leaf(node.left)
        return node

    '''------------------------------------ Explorations --------------------------------------'''

    def explo(self):
        """
        Display type of exploration
        """
        print("Prefix: ", self.prefix(self.tree))
        print("Postfix: ", self.postfix(self.tree))
        print("Infix: ", self.infix(self.tree))
        print("Width: ", self.width(self.tree))

    def prefix(self, node: Node) -> list:
        """
        Prefix exploration of an abr tree. First, the root is explored,
        then the left subtree and finally the right subtree
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return [node.value] + self.prefix(node.left) + self.prefix(node.right)

    def postfix(self, node: Node) -> list:
        """
        Postfix exploration of an abr tree. First, the left subtree is explored,
        then the right subtree and finally the root
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return self.postfix(node.left) + self.postfix(node.right) + [node.value]

    def infix(self, node: Node) -> list:
        """
        Infix exploration of an abr tree. First, the left subtree is explored,
        then the root and finally the right subtree
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return self.infix(node.left) + [node.value] + self.infix(node.right)

    def width(self, node: Node) -> list:
        """
        Width exploration of an abr tree. We explore the tree level by level, from left to right
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        pile = [node]
        results = []
        while len(pile):
            node = pile.pop(0)
            results.append(node.value)
            if node.left is not None:
                pile.append(node.left)
            if node.right is not None:
                pile.append(node.right)
        return results

    def is_in_abr(self, value):
        """
        Display information if the value is in abr
        """
        print("Dans l'abr : ", self.research_val(self.tree, value))
        print("Le noeud : ", self.research_node(self.tree, value))
        print("Nombre d'occurence dans l'abr : ", self.countVal(self.tree, value))

    def research_val(self, node, value):
        """
        Research a value in an abr tree, return True if the value is in the tree, False otherwise
        :param node: Node
        :param value: float
        :return: bool
        """
        if node is None:
            boolean = False
        elif node.value == value:
            boolean = True
        elif value < node.value:
            boolean = self.research_val(node.left, value)
        else:
            boolean = self.research_val(node.right, value)
        return boolean

    def research_node(self, node: Node, value: float) -> Node:
        """
        Research a node in an abr tree, return the node if the value is in the tree, None otherwise
        :param node: Node
        :param value: float
        :return: Node | None
        """
        if node is None:
            return
        elif node.value == value:
            return node
        elif value < node.value:
            return self.research_node(node.left, value)
        else:
            return self.research_node(node.right, value)

    def countVal(self, node: Node, value: float) -> int:
        """
        Count the number of times a value appears in an abr tree.
        (when the same value exist in abr tree, the second value go to the right)
        :param node: Node
        :param value: float
        :return: int
        """
        if self.tree is None:
            return 0
        count = 0
        while node is not None:
            if node.value == value:
                count += 1
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return count

    '''-------------------------------------- Features --------------------------------------'''

    def info(self):
        """
        Display information about the abr
        """
        print("Nombre de noeuds : ", self.size(self.tree))
        print("Hauteur de l'arbre : ", self.height(self.tree))
        print("Valeur min :", self.min_abr(self.tree))
        print("Valeur max :", self.max_abr(self.tree))
        print("Le plus grand écart entre deux noeuds : ", self.biggestGap(self.tree))
        print("Somme des noeuds : ", self.sumAbr(self.tree))
        print("Moyenne de tout les noeuds : ", self.average(self.tree))

    def size(self, node):
        """
        Return the size of an abr tree, the size is the number of nodes in the tree
        :param node: Node
        :return: int
        """
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        """
        Return the height of an abr tree, the height is the number of edges in the longest path from the root to a leaf
        :param node: Node
        :return: int
        """
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def min_abr(self, node: Node) -> Node:
        """
        Return the node with the minimum value in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return None
        if node.left is not None:
            return self.min_abr(node.left)

    def max_abr(self, node: Node) -> Node:
        """
        Return the node with the maximum value in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return None
        if node.right is not None:
            return self.max_abr(node.right)

    def biggestGap(self, node):
        """
        Return the biggest gap between two nodes (max value and min value) in an abr tree
        :param node: Node
        :return: float
        """
        if node is None:
            return 0
        return self.max_abr(node) - self.min_abr(node)

    def sumAbr(self, node: Node) -> float:
        """
        Return the sum of all values in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return 0
        return node.value + self.sumAbr(node.left) + self.sumAbr(node.right)

    def average(self, node: Node) -> float | None:
        """
        Return the average of all values in an abr tree
        :param node: Node
        :return: float | None
        """
        if node is None:
            return
        return self.sumAbr(node) / self.size(node)

    '''-------------------------------------- Other --------------------------------------'''

    def open_abr(self, file):
        """
        Execute the open abr
        :param file: File
        """
        data = file.openDataFile()
        self.tree = None
        self.tree = self.create_abr(data)
        self.update_display_abr(self.canvas)

    def save_abr(self, file):
        """
        Execute the save abr
        :param file: File
        """
        file.saveFileDataABR(self.tree)

    def update_display_abr(self, canvas):
        """
        Execute the update of the display abr
        :param canvas: Canvas
        """
        canvas.delete("all")
        Draw.DrawABR(canvas, self.tree)
        canvas.update()

    def balancing_abr(self):
        """
        Execute the balancing of the abr each node ad the same number of children
        """
        self.tree = self.balancing(self.tree)
        self.update_display_abr(self.canvas)

    def balancing(self, node: Node) -> Node:
        """
        Return a balanced abr tree
        :param node: Node
        :return: Node
        """
        if node is None:
            return None
        if self.height(node.left) > self.height(node.right):
            node.right = self.balancing(node.right)
            node = self.rotate_left(node)
        elif self.height(node.left) < self.height(node.right):
            node.left = self.balancing(node.left)
            node = self.rotate_right(node)
        node.left = self.balancing(node.left)
        node.right = self.balancing(node.right)
        return node

    def rotate_left(self, node: Node) -> Node:
        """
        Rotate a node to the left
        :param node: Node
        :return: Node
        """
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        return tmp

    def rotate_right(self, node: Node) -> Node:
        """
        Rotate a node to the right
        :param node: Node
        :return: Node
        """
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        return tmp
