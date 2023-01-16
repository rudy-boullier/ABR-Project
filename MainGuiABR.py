from tkinter import *
import ABR as abr
import Node as n
import File as f

class MainGuiABR:
    def __init__(self, root):
        """
        Init the MainGuiABR class
        :param root: Windows
        """
        self.root = root
        self.root.title("Analyse d'un Arbre Binaire de Recherche")
        self.root.geometry("800x600")

        self.file = f.File()

        menuABR = LabelFrame(root, text="Option ABR", padx=20, pady=20)
        menuABR.pack(fill="both", side=LEFT, padx=5, pady=5)

        self.valueSupp = StringVar()
        self.valueSupp.set("")
        self.entree = Entry(menuABR, textvariable=self.valueSupp, width=5)
        self.entree.pack()

        self.bouton=Button(menuABR, text="Del noeud", bg="red", command=self.checkSuppInput)
        self.bouton.pack()

        self.bouton=Button(menuABR, text="Del gauche", bg="red", command=lambda:self.abr.suppExtremeLeftValueABR(self.file))
        self.bouton.pack()

        self.bouton=Button(menuABR, text="Del droite", bg="red", command=lambda:self.abr.suppExtremeRightValueABR(self.file))
        self.bouton.pack()

        self.valueAdd = StringVar()
        self.valueAdd.set("")
        self.entree = Entry(menuABR, textvariable=self.valueAdd, width=5)
        self.entree.pack()

        self.bouton=Button(menuABR, text="Ajoute un noeud", bg="green", command=self.checkAddInput)
        self.bouton.pack()

        self.bouton=Button(menuABR, text="print exploration", bg="blue", fg="white", command=lambda:self.abr.explo())
        self.bouton.pack()

        self.valueS = StringVar()
        self.valueS.set("")
        self.entree = Entry(menuABR, textvariable=self.valueS, width=5)
        self.entree.pack()

        self.bouton=Button(menuABR, text="dans l'abr", bg="blue", fg="white", command=self.checkSearchInput)
        self.bouton.pack()

        self.bouton=Button(menuABR, text="info", bg="black", fg="white", command=lambda:self.abr.info())
        self.bouton.pack()

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)

        self.abr = abr.ABR(self.canvas)

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(label="Ouvrir", command=lambda:self.abr.openABR(self.file))
        self.file_menu.add_command(label="Sauvegarder", command=lambda:self.abr.saveABR(self.file))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=self.root.quit)


    def checkSuppInput(self):
        """
        Check the input for supp value
        """
        if self.valueSupp.get() == "":
            print("Champ vide, veuillez entrer une valeur valide")
        else:
            try:
                if float(self.valueSupp.get()) == int(self.valueSupp.get()):
                    self.abr.suppValueABR(int(self.valueSupp.get()), self.file)
            except:
                self.abr.suppValueABR(float(self.valueSupp.get()), self.file)


    def checkAddInput(self):
        """
        Check the input for add value
        """
        if self.valueAdd.get() == "":
            print("Champ vide, veuillez entrer une valeur valide")
        else:
            try:
                if float(self.valueAdd.get()) == int(self.valueAdd.get()):
                    self.abr.addValueABR(int(self.valueAdd.get()), self.file)
            except:
                self.abr.addValueABR(float(self.valueAdd.get()), self.file)


    def checkSearchInput(self):
        """
        Check the input for search a value
        """
        if self.valueS.get() == "":
            print("Champ vide, veuillez entrer une valeur valide")
        else:
            try:
                if float(self.valueS.get()) == int(self.valueS.get()):
                    self.abr.isInABR(int(self.valueS.get()))
            except:
                self.abr.isInABR(float(self.valueS.get()))

