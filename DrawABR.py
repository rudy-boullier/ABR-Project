import math

class DrawABR:
    def __init__(self, canvas, node):
        """
        Init the DrawABR classe
        :param canvas: Canvas
        :param node: Node
        """
        self.canvas = canvas
        self.radiusCircle = 20
        self.drawNode(node, None, None, x=250, y=50)

    
    def drawNode(self, node, parent_x, parent_y, x, y):
        """
        Draw the abr
        :param node: Node
        :param parent_x: float
        :param parent_y: float
        :param x: float
        :param y: float
        """
        if node is not None:
            self.canvas.create_oval(x-self.radiusCircle, y-self.radiusCircle, x+self.radiusCircle, y+self.radiusCircle, outline="blue", width=3)
            self.canvas.create_text(x, y, text=node.value, font=("Arial", self.radiusCircle//2), fill="black", anchor="center")
            if parent_x and parent_y:
                start_x = parent_x + self.radiusCircle * math.cos(math.atan2(y - parent_y, x - parent_x))
                start_y = parent_y + self.radiusCircle * math.sin(math.atan2(y - parent_y, x - parent_x))
                end_x = x - self.radiusCircle * math.cos(math.atan2(y - parent_y, x - parent_x))
                end_y = y - self.radiusCircle * math.sin(math.atan2(y - parent_y, x - parent_x))
                self.canvas.create_line(start_x, start_y, end_x, end_y, fill="blue", width=3)
            if node.left:
                left_x, left_y = self.calculateCoordinates(x, y, "left")
                self.drawNode(node.left, x, y, left_x, left_y)
            if node.right:
                right_x, right_y = self.calculateCoordinates(x, y, "right")
                self.drawNode(node.right, x, y, right_x, right_y)


    def calculateCoordinates(self, x, y, direction):
        """
        Calculate the coordinates of node
        :param x: float
        :param y: float
        :return: x and y, float
        """
        r = self.radiusCircle
        if direction == "left":
            x = x - r*2
            y = y + r*2
        elif direction == "right":
            x = x + r*2
            y = y + r*2
        return x, y
