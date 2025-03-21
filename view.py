import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk

class EntrepriseView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Gestion des Entreprises")
        self.root.configure(fg_color="#c8e7f9")  # Set background color to #c8e7f9

        # les vars
        self.nom_var = ctk.StringVar()
        self.num_registre_var = ctk.StringVar()
        self.adresse_var = ctk.StringVar()
        self.email_var = ctk.StringVar()
        self.telephone_var = ctk.StringVar()
        self.date_inscription_var = ctk.StringVar()
        self.secteur_activite_var = ctk.StringVar()

        self.setup_ui()

    def reset(self):
        self.nom_var.set("")
        self.num_registre_var.set("")
        self.adresse_var.set("")
        self.email_var.set("")
        self.telephone_var.set("")
        self.date_inscription_var.set("")
        self.secteur_activite_var.set("")

    def setup_ui(self):
        # Set background color for labels and entries
        label_bg = "#c8e7f9"
        entry_bg = "#ffffff"  # White background for entries

        ctk.CTkLabel(self.root, text="Nom:", fg_color=label_bg, text_color="black").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.nom_var, fg_color=entry_bg, text_color="black").grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Numéro de Registre:", fg_color=label_bg, text_color="black").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.num_registre_var, fg_color=entry_bg, text_color="black").grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Adresse:", fg_color=label_bg, text_color="black").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.adresse_var, fg_color=entry_bg, text_color="black").grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Email:", fg_color=label_bg, text_color="black").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.email_var, fg_color=entry_bg, text_color="black").grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Téléphone:", fg_color=label_bg, text_color="black").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.telephone_var, fg_color=entry_bg, text_color="black").grid(row=4, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Date d'inscription: (A-M-J)", fg_color=label_bg, text_color="black").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.date_inscription_var, fg_color=entry_bg, text_color="black").grid(row=5, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Secteur d'Activité:", fg_color=label_bg, text_color="black").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self.root, textvariable=self.secteur_activite_var, fg_color=entry_bg, text_color="black").grid(row=6, column=1, padx=10, pady=5)

        ctk.CTkButton(self.root, text="Ajouter Entreprise", command=self.ajouter_entreprise).grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        ctk.CTkButton(self.root, text="Réinitialiser", command=self.reset).grid(row=7, column=2, padx=10, pady=5)

        ctk.CTkLabel(self.root, text="Rechercher:", fg_color=label_bg, text_color="black").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.search_var = ctk.StringVar()
        ctk.CTkEntry(self.root, textvariable=self.search_var, fg_color=entry_bg, text_color="black").grid(row=8, column=1, padx=10, pady=5)

        self.img = ctk.CTkImage(Image.open("img/search.png"))
        self.img3 = ctk.CTkImage(Image.open("img/return.png"))
        ctk.CTkButton(self.root, image=self.img, text="", command=self.rechercher_entreprise, width=30).grid(row=8, column=2, padx=10, pady=5)
        ctk.CTkButton(self.root, image=self.img3, text="", command=self.backup_data, width=30).grid(row=8, column=3, padx=10, pady=5)

        self.img2 = ctk.CTkImage(Image.open("img/confused2.png"))
        ctk.CTkButton(self.root, image=self.img2, text="", command=self.show_message2, width=30).grid(row=0, column=3, padx=10, pady=5)

        # Table
        self.tree = ttk.Treeview(self.root, columns=("Id", "Nom", "Numéro", "Adresse", "Email"), show="headings")
        self.tree.heading("Id", text="Id")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Numéro", text="Numéro")
        self.tree.heading("Adresse", text="Adresse")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

        # Make tree headings bold
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#c8e7f9", foreground="black")

        scrollbar_y = ctk.CTkScrollbar(self.root, orientation="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=9, column=4, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar_y.set)

        ctk.CTkButton(self.root, text="Supprimer Entreprise", command=self.supprimer_entreprise).grid(row=10, column=0, padx=10, pady=5)
        ctk.CTkButton(self.root, text="Afficher Détails", command=self.afficher_details_selection).grid(row=10, column=1, padx=10, pady=5)

    def ajouter_entreprise(self):
        data = (
            self.nom_var.get(),
            self.num_registre_var.get(),
            self.adresse_var.get(),
            self.email_var.get(),
            self.telephone_var.get(),
            self.date_inscription_var.get(),
            self.secteur_activite_var.get()
        )
        for i in data:
            if not i:
                messagebox.showwarning("Erreur", "Tous les champs sont obligatoires.")
                return
        self.controller.ajouter_entreprise(*data)

    def rechercher_entreprise(self):
        critere = self.search_var.get()
        if not critere:
            messagebox.showwarning("Erreur", "Introduisez un nom / numero a rechercher.")
            return
        self.controller.rechercher_entreprise(critere)

    def supprimer_entreprise(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une entreprise à supprimer.")
            return
        entreprise_id = self.tree.item(selected_item, "values")[0]
        self.controller.supprimer_entreprise(entreprise_id)

    def afficher_entreprises(self, entreprises):
        self.tree.delete(*self.tree.get_children())
        for entreprise in entreprises:
            self.tree.insert("", "end", values=entreprise)

    def backup_data(self):
        self.search_var.set('')
        critere = self.search_var.get()
        self.controller.rechercher_entreprise(critere)

    def afficher_resultats_recherche(self, entreprises):
        self.tree.delete(*self.tree.get_children())
        for entreprise in entreprises:
            self.tree.insert("", "end", values=entreprise)

    def afficher_details_selection(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une entreprise a afficher.")
            return

        values = self.tree.item(selected_item, "values")
        if not values:
            messagebox.showwarning("Erreur", "Impossible de récupérer les détails de l'entreprise.")
            return
        detail_window = ctk.CTkToplevel(self.root)
        detail_window.title("Détails de l'Entreprise")
        detail_window.geometry("400x300")
        detail_window.configure(fg_color="#c8e7f9")  # Set background color for the detail window

        labels = [
            "Id:", "Nom de l'Entreprise:", "Numéro de Registre:", "Adresse:",
            "Email:", "Téléphone:", "Date d'Inscription:", "Secteur d'Activité:"
        ]

        for i, label_text in enumerate(labels):
            ctk.CTkLabel(detail_window, text=label_text, font=("Arial", 10, "bold"), fg_color="#c8e7f9", text_color="black").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(detail_window, text=values[i], font=("Arial", 10), fg_color="#c8e7f9", text_color="black").grid(row=i, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkButton(detail_window, text="Fermer", command=detail_window.destroy).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_message2(self):
        messagebox.showinfo(
            "Guide",
            "Cette application vous permet de gérer facilement les enregistrements des entreprises. Vous pouvez :\n\n"
            "- Ajouter une entreprise : Remplissez le formulaire et cliquez sur 'Ajouter Entreprise'.\n"
            "- Rechercher une entreprise : Entrez un critère de recherche (nom ou numéro de registre) et cliquez sur 'Rechercher'.\n"
            "- Supprimer une entreprise : Sélectionnez une ligne dans le tableau et cliquez sur 'Supprimer Entreprise'.\n"
            "- Afficher les détails : Sélectionnez une ligne et cliquez sur 'Afficher Détails' pour consulter toutes les informations de l’entreprise.\n\n"
            "Gérez vos données en toute simplicité ! 🚀"
        )

    def start(self):
        self.root.mainloop()