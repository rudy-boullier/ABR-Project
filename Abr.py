import math

from Node import Node


def initAbr(values: list):
    abr = Node(values[0])
    addValues(abr, values[1:])
    return abr


def addValues(abr: Node, values: list):
    if len(values) > 0:
        for i in range(len(values)):
            abr.plantAbr(values[i])
    return abr


"""--------------Explor-----------------"""


def prefix(abr: Node):
    if abr is None:
        return []
    return [abr.val] + prefix(abr.left) + prefix(abr.right)


def postfix(abr: Node):
    if abr is None:
        return []
    return postfix(abr.left) + postfix(abr.right) + [abr.val]


def infix(abr: Node):
    if abr is None:
        return []
    return infix(abr.left) + [abr.val] + infix(abr.right)


def width(abr: Node) -> list:
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


def size(abr: Node) -> int:
    if abr is None:
        return 0
    return 1 + size(abr.left) + size(abr.right)


def height(abr: Node) -> int:
    if abr is None:
        return 0
    return 1 + max(height(abr.left), height(abr.right))


def researchAbr(abr: Node, value: float) -> bool:
    if abr is None:
        boolean = False
    elif abr.val == value:
        boolean = True
    elif value < abr.val:
        boolean = researchAbr(abr.left, value)
    else:
        boolean = researchAbr(abr.right, value)
    return boolean


def minAbr(abr: Node) -> float:
    if abr.left is None:
        return math.inf
    return min(abr.val, minAbr(abr.left), minAbr(abr.right))


def maxAbr(abr: Node) -> float:
    if abr.right is None:
        return -math.inf
    return max(abr.val, maxAbr(abr.left), maxAbr(abr.right))


def deleteExtremeRight(abr: Node) -> None:
    if abr is None:
        return None
    if abr.right is not None:
        deleteExtremeRight(abr.right)
    elif abr.left is not None:
        deleteExtremeRight(abr.left)
    else:
        del abr


def deleteExtremeLeft(abr: Node) -> None:
    if abr is None:
        return None
    if abr.left is not None:
        deleteExtremeLeft(abr.left)
    elif abr.right is not None:
        deleteExtremeLeft(abr.right)
    else:
        del abr


def delete_node(node, value):
    if node is None:
        return
    if value < node.value:
        node.left = delete_node(node.left, value)
    elif value > node.value:
        node.right = delete_node(node.right, value)
    else:
        if node.left is None:
            node = node.right
            return node
        elif node.right is None:
            node = node.left
            return node
        smallest = find_smallest(node.right)
        node.value = smallest.value
        node.right = delete_node(node.right, smallest.value)
    return node


def find_smallest(node):
    if node.left is not None:
        return find_smallest(node.left)
    return node
