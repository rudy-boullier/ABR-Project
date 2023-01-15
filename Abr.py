from Node import Node

'''-------------------------------------- Add --------------------------------------'''


def initAbr(values: list) -> Node:
    """
    Create an abr tree from a list of values
    :param values: list of float
    :return: Node, an abr tree
    """
    abr = Node(values[0])
    addValues(abr, values[1:])
    return abr


def addValues(abr: Node, values: list) -> Node:
    """
    Add values to an abr tree
    :param abr: Node
    :param values: list of float
    :return: Node
    """
    if len(values) > 0:
        for i in range(len(values)):
            abr.plantAbr(values[i])
    return abr


'''-------------------------------------- Delete --------------------------------------'''


def deleteExtremeRight(abr: Node) -> None:
    """
    Delete the extreme right node of an abr tree
    :param abr: Node
    :return: None
    """
    if abr is None:
        return None
    if abr.right is not None:
        deleteExtremeRight(abr.right)
    elif abr.left is not None:
        deleteExtremeRight(abr.left)
    else:
        del abr


def deleteExtremeLeft(abr: Node) -> None:
    """
    Delete the extreme left node of an abr tree
    :param abr: Node
    :return: None
    """
    if abr is None:
        return None
    if abr.left is not None:
        deleteExtremeLeft(abr.left)
    elif abr.right is not None:
        deleteExtremeLeft(abr.right)
    else:
        del abr


def delete_node(node: Node, value: float) -> Node | None:
    """
    Delete a node in an abr tree, the node is the first node with the value, if the value doesn't exist, nothing is done
    When a node is deleted, minval of the right subtree is used to replace the deleted node
    :param node: Node
    :param value: float
    :return: Node | None
    """
    if node is None:
        return
    if value != node.val:
        researchNode(node, value)
    else:
        if node.left is None:
            node = node.right
            return node
        elif node.right is None:
            node = node.left
            return node
        smallest = minAbr(node.right)
        node.value = smallest.val
        node.right = delete_node(node.right, smallest.val)
    return node


def delete_node2(node: Node, value: float) -> Node | None:
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
    node.left = delete_node(node.left, biggest.val)
    return node


'''------------------------------------ Explorations --------------------------------------'''


def prefix(abr: Node) -> list:
    """
    Prefix exploration of an abr tree. First, the root is explored, then the left subtree and finally the right subtree
    :param abr: Node
    :return: list of nodes
    """
    if abr is None:
        return []
    return [abr.val] + prefix(abr.left) + prefix(abr.right)


def postfix(abr: Node) -> list:
    """
    Postfix exploration of an abr tree. First, the left subtree is explored, then the right subtree and finally the root
    :param abr: Node
    :return: list of nodes
    """
    if abr is None:
        return []
    return postfix(abr.left) + postfix(abr.right) + [abr.val]


def infix(abr: Node) -> list:
    """
    Infix exploration of an abr tree. First, the left subtree is explored, then the root and finally the right subtree
    :param abr: Node
    :return: list of nodes
    """
    if abr is None:
        return []
    return infix(abr.left) + [abr.val] + infix(abr.right)


def width(abr: Node) -> list:
    """
    Width exploration of an abr tree. We explore the tree level by level, from left to right
    :param abr: Node
    :return: list of nodes
    """
    pile = [abr]
    results = []
    while len(pile):
        node = pile.pop(0)
        results.append(node.val)
        if node.left is not None:
            pile.append(node.left)
        if node.right is not None:
            pile.append(node.right)
    return results


def researchVal(abr: Node, value: float) -> bool:
    """
    Research a value in an abr tree, return True if the value is in the tree, False otherwise
    :param abr: Node
    :param value: float
    :return: bool
    """
    if abr is None:
        boolean = False
    elif abr.val == value:
        boolean = True
    elif value < abr.val:
        boolean = researchVal(abr.left, value)
    else:
        boolean = researchVal(abr.right, value)
    return boolean


def researchNode(abr: Node, value: float) -> Node | None:
    """
    Research a node in an abr tree, return the node if the value is in the tree, None otherwise
    :param abr: Node
    :param value: float
    :return: Node | None
    """
    if abr is None:
        return
    elif abr.val == value:
        return abr
    elif value < abr.val:
        return researchNode(abr.left, value)
    else:
        return researchNode(abr.right, value)


def countVal(abr: Node, value: float) -> int:
    """
    Count the number of times a value appears in an abr tree.
    (when the same value exist in abr tree, the second value go to the right)
    :param abr: Node
    :param value: float
    :return: int
    """
    tmp = 0
    if abr is None:
        return tmp
    while abr.val is not None:
        if abr.val == value:
            tmp = 1 + countVal(abr.right, value)
        elif value < abr.val:
            tmp = countVal(abr.left, value)
        else:
            tmp = countVal(abr.right, value)
    return tmp


'''-------------------------------------- Features --------------------------------------'''


def size(abr: Node) -> int:
    """
    Return the size of an abr tree, the size is the number of nodes in the tree
    :param abr: Node
    :return: int
    """
    if abr is None:
        return 0
    return 1 + size(abr.left) + size(abr.right)


def height(abr: Node) -> int:
    """
    Return the height of an abr tree, the height is the number of edges in the longest path from the root to a leaf
    :param abr: Node
    :return: int
    """
    if abr is None:
        return 0
    return 1 + max(height(abr.left), height(abr.right))


def minAbr(abr: Node) -> Node:
    """
    Return the node with the minimum value in an abr tree
    :param abr: Node
    :return: Node
    """
    if abr.left is not None:
        return minAbr(abr.left)
    return abr


def maxAbr(abr: Node) -> Node:
    """
    Return the node with the maximum value in an abr tree
    :param abr: Node
    :return: Node
    """
    if abr.right is not None:
        return maxAbr(abr.right)
    return abr


def biggestGap(abr: Node) -> float:
    """
    Return the biggest gap between two nodes (max value and min value) in an abr tree
    :param abr: Node
    :return: float
    """
    if abr is None:
        return 0
    return maxAbr(abr).val - minAbr(abr).val


def sumAbr(abr: Node) -> int:
    """
    Return the sum of all values in an abr tree
    :param abr: Node
    :return: int
    """
    if abr is None:
        return 0
    return abr.val + sumAbr(abr.left) + sumAbr(abr.right)


def average(abr: Node) -> float:
    """
    Return the average of all values in an abr tree
    :param abr: Node
    :return: float
    """
    return sumAbr(abr) / size(abr)
