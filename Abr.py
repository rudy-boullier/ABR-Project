import DrawABR as d
import Node as node

class ABR:
    def __init__(self, canvas):
        """
        Init the ABR classe
        :param canvas: Canvas
        """
        self.tree = None
        self.canvas = canvas

    '''-------------------------------------- Add --------------------------------------'''

    def createABR(self, data):
        """
        Create an abr tree from a list of values
        :param data: list of float
        :return: Node, an abr tree
        """
        for value in data:
            if self.tree is None:
                self.tree = node.Node(value)
            else:
                self.tree.insert(value)
        return self.tree


    def addValueABR(self, value, file):
        """
        Add value to an abr tree
        :param value: float
        :param file: File
        """
        if self.tree is None:
            self.tree = node.Node(value)
        else:
            self.tree.insert(value)
        file.updateData(self.tree)
        self.updateDisplayABR(self.canvas)

    '''-------------------------------------- Delete --------------------------------------'''

    def suppValueABR(self, value, file):
        """
        Delete a node in an abr tree
        :param value: float
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.removeNode(self.tree, value)
            file.updateData(self.tree)
            self.updateDisplayABR(self.canvas)


    def findMinNode(self, node):
        """
        Find the min for remove node
        :param node: Node
        """
        if node.left is not None:
            return self.findMinNode(node.left)
        return node

            
    def removeNode(self, node, value):
        """
        Delete a node in an abr tree, the node is the first node with the value, if the value doesn't exist, nothing is done
        When a node is deleted, minval of the right subtree is used to replace the deleted node
        :param node: Node
        :param value: float
        :return: Node | None
        """
        if node is None:
            return None
        if value < node.value:
            node.left = self.removeNode(node.left, value)
        elif value > node.value:
            node.right = self.removeNode(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            minNode = self.findMinNode(node.right)
            node.value = minNode.value
            node.right = self.removeNode(node.right, minNode.value)
        return node


    def removeNode2(self, node, value): # not implemented
        """
        Delete a node in an abr tree, the node is the first node with the value, if the value doesn't exist, nothing is done
        When a node is deleted, maxval of the left subtree is used to replace the deleted node
        :param node: Node
        :param value: float
        :return: Node | None
        """
        if node is None:
            return
        if value != node.val:
            tmp = researchNode(node, value)
            if tmp is not None:
                node = tmp
        if node.left is None:
            node = node.right
            return node
        elif node.right is None:
            node = node.left
            return node
        biggest = maxAbr(node.left)
        node.value = biggest.val
        node.left = removeNode2(node.left, biggest.val)
        return node


    def suppExtremeRightValueABR(self, file):
        """
        Execute the delete of extreme right node in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.deleteExtremeRight(self.tree)
            file.updateData(self.tree)
            self.updateDisplayABR(self.canvas)

            
    def deleteExtremeRight(self, node):
        """
        Delete the extreme right node of an abr tree
        :param abr: Node
        :return: node
        """
        if node.right is None:
            return node.left
        node.right = self.deleteExtremeRight(node.right)
        return node


    def suppExtremeLeftValueABR(self, file):
        """
        Execute the delete of extreme left node in an abr tree
        :param file: File
        """
        if self.tree is not None:
            self.tree = self.deleteExtremeLeft(self.tree)
            file.updateData(self.tree)
            self.updateDisplayABR(self.canvas)


    def deleteExtremeLeft(self, node):
        """
        Delete the extreme left node of an abr tree
        :param node: Node
        :return: node
        """
        if node.left is None:
            return node.right
        node.left = self.deleteExtremeLeft(node.left)
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

    def prefix(self, node):
        """
        Prefix exploration of an abr tree. First, the root is explored, then the left subtree and finally the right subtree
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return [node.value] + self.prefix(node.left) + self.prefix(node.right)


    def postfix(self, node):
        """
        Postfix exploration of an abr tree. First, the left subtree is explored, then the right subtree and finally the root
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return self.postfix(node.left) + self.postfix(node.right) + [node.value]


    def infix(self, node):
        """
        Infix exploration of an abr tree. First, the left subtree is explored, then the root and finally the right subtree
        :param node: Node
        :return: list of nodes
        """
        if node is None:
            return []
        return self.infix(node.left) + [node.value] + self.infix(node.right)


    def width(self, node):
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


    def isInABR(self, value):
        """
        Display information if the value is in abr
        """
        print("Dans l'abr : ", self.researchVal(self.tree, value))
        print("Le noeud : ", self.researchNode(self.tree, value))
        print("Nombre d'occurence dans l'abr : ", self.countVal(self.tree, value))

    def researchVal(self, node, value):
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
            boolean = self.researchVal(node.left, value)
        else:
            boolean = self.researchVal(node.right, value)
        return boolean


    def researchNode(self, node, value):
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
            return self.researchNode(node.left, value)
        else:
            return self.researchNode(node.right, value)


    def countVal(self, node, value):
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
        stack = [self.tree]
        while stack:
            node = stack.pop()
            if node.value == value:
                count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

    '''-------------------------------------- Features --------------------------------------'''

    def info(self):
        """
        Display information about the abr
        """
        print("Nombre de noeuds : ", self.size(self.tree))
        print("Hauteur de l'arbre : ", self.height(self.tree))
        print("Valeur min :", self.minAbr(self.tree))
        print("Valeur max :", self.maxAbr(self.tree))
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


    def minAbr(self, node):
        """
        Return the node with the minimum value in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return None
        if node.left is not None:
            return self.minAbr(node.left)
        return node.value


    def maxAbr(self, node):
        """
        Return the node with the maximum value in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return None
        if node.right is not None:
            return self.maxAbr(node.right)
        return node.value


    def biggestGap(self, node):
        """
        Return the biggest gap between two nodes (max value and min value) in an abr tree
        :param node: Node
        :return: float
        """
        if node is None:
            return 0
        return self.maxAbr(node) - self.minAbr(node)


    def sumAbr(self, node):
        """
        Return the sum of all values in an abr tree
        :param node: Node
        :return: int
        """
        if node is None:
            return 0
        return node.value + self.sumAbr(node.left) + self.sumAbr(node.right)


    def average(self, node):
        """
        Return the average of all values in an abr tree
        :param node: Node
        :return: float
        """
        if node is None:
            return None
        return self.sumAbr(node) / self.size(node)

    '''-------------------------------------- Other --------------------------------------'''

    def openABR(self, file):
        """
        Execute the open abr
        :param file: File
        """
        data = file.openDataFile()
        self.tree = None
        self.tree = self.createABR(data)
        self.updateDisplayABR(self.canvas)


    def saveABR(self, file):
        """
        Execute the save abr
        :param file: File
        """
        file.saveFileDataABR(self.tree)

            
    def updateDisplayABR(self, canvas):
        """
        Execute the update of the display abr
        :param canvas: Canvas
        """
        canvas.delete("all")
        d.DrawABR(canvas, self.tree)
        canvas.update()

