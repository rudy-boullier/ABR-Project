from tkinter import filedialog

class File:
    def __init__(self):
        """
        Init the File classe
        """
        self.data = []

        
    def openDataFile(self):
        """
        Function to read data from file and return it as a list of data
        :return: data, list of float
        """
        filepath = filedialog.askopenfilename(title = "Ouvrir un ABR", filetypes = [('txt files', '.txt'), ('all files', '.*')])
        if filepath != "":
            self.data = []
            with open(filepath, "r") as file:
                fileData = file.read()
                for v in fileData.split(","):
                    self.data.append(int(v))
        return self.data


    def saveFileDataABR(self, tree):
        """
        Save the data in file
        :param tree: Node
        """
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            dataNode = self.readTree(tree)
            array_str = ','.join(str(x) for x in dataNode)
            file.write(array_str)
                
            file.close()
        else:
            print("Le fichier n'a pas été sauvegardé.")
            return


    def readTree(self, node):
        """
        Read the tree value
        :param node: Node
        :return: array, array of float
        """
        if node is None:
            return []
        return [node.value] + self.readTree(node.left) + self.readTree(node.right)


    def updateData(self, tree):
        """
        Update the Data 
        :param tree: Node
        """
        self.data = self.readTree(tree)
        
