from tkinter import *
import Abr
import File


class MainGuiABR:
    def __init__(self, root):
        """
        Init the MainGuiABR class
        :param root: Windows
        """
        self.root = root
        self.root.title("Analyse d'un Arbre Binaire de Recherche")
        self.root.geometry("800x600")

        self.file = File.File()

        menu_abr = LabelFrame(root, text="Option ABR", padx=20, pady=20)
        menu_abr.pack(fill="both", side=LEFT, padx=5, pady=5)

        self.valueSupp = StringVar()
        self.valueSupp.set("")
        self.entree = Entry(menu_abr, textvariable=self.valueSupp, width=5)
        self.entree.pack()

        self.bouton = Button(menu_abr, text="zoom", bg="violet", command=self.checkSuppInput)
        self.bouton.pack()

        self.bouton = Button(menu_abr, text="Del gauche", bg="red",
                             command=lambda: self.abr.supp_extreme_left_value_abr(self.file))
        self.bouton.pack()

        self.bouton = Button(menu_abr, text="Del droite", bg="red",
                             command=lambda: self.abr.supp_extreme_right_value_abr(self.file))
        self.bouton.pack()

        self.valueAdd = StringVar()
        self.valueAdd.set("")
        self.entree = Entry(menu_abr, textvariable=self.valueAdd, width=5)
        self.entree.pack()

        self.bouton = Button(menu_abr, text="Ajoute un noeud", bg="green", command=self.checkAddInput)
        self.bouton.pack()

        self.bouton = Button(menu_abr, text="print exploration", bg="blue", fg="white",
                             command=lambda: self.abr.explo())
        self.bouton.pack()

        self.valueS = StringVar()
        self.valueS.set("")
        self.entree = Entry(menu_abr, textvariable=self.valueS, width=5)
        self.entree.pack()

        self.bouton = Button(menu_abr, text="dans l'abr", bg="blue", fg="white", command=self.checkSearchInput)
        self.bouton.pack()

        self.bouton = Button(menu_abr, text="info", bg="black", fg="white", command=lambda: self.abr.info())
        self.bouton.pack()

        self.bouton = Button(menu_abr, text="équilibrage", bg="yellow", fg="black", command=lambda: self.abr.balancing_abr())
        self.bouton.pack()

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)

        self.abr = Abr.Abr(self.canvas)

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(label="Ouvrir", command=lambda: self.abr.open_abr(self.file))
        self.file_menu.add_command(label="Sauvegarder", command=lambda: self.abr.save_abr(self.file))
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
                    self.abr.supp_value_abr(int(self.valueSupp.get()), self.file)
            except ValueError:
                self.abr.supp_value_abr(float(self.valueSupp.get()), self.file)

    def checkAddInput(self):
        """
        Check the input for add value
        """
        if self.valueAdd.get() == "":
            print("Champ vide, veuillez entrer une valeur valide")
        else:
            try:
                if float(self.valueAdd.get()) == int(self.valueAdd.get()):
                    self.abr.add_value_abr(int(self.valueAdd.get()), self.file)
            except ValueError:
                self.abr.add_value_abr(float(self.valueAdd.get()), self.file)

    def checkSearchInput(self):
        """
        Check the input for search a value
        """
        if self.valueS.get() == "":
            print("Champ vide, veuillez entrer une valeur valide")
        else:
            try:
                if float(self.valueS.get()) == int(self.valueS.get()):
                    self.abr.is_in_abr(int(self.valueS.get()))
            except ValueError:
                self.abr.is_in_abr(float(self.valueS.get()))
