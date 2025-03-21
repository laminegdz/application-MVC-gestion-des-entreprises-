from model import EntrepriseModel
from tkinter import messagebox
from view import EntrepriseView


class EntrepriseController:
    def __init__(self):
        self.model = EntrepriseModel()
        self.view = EntrepriseView(self)
        self.model.create_table()
        self.afficher_entreprises()

    def ajouter_entreprise(self, nom, num_registre, adresse, email, telephone, date_inscription, secteur_activite):
        try:
            self.model.ajouter_entreprise(nom, num_registre, adresse, email, telephone, date_inscription, secteur_activite)
            self.afficher_entreprises()
            self.view.nom_var.set("")
            self.view.num_registre_var.set("")
            self.view.adresse_var.set("")
            self.view.email_var.set("")
            self.view.telephone_var.set("")
            self.view.date_inscription_var.set("")
            self.view.secteur_activite_var.set("")
            messagebox.showinfo("Succès", "Entreprise ajoutée avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def supprimer_entreprise(self, entreprise_id):
        try:
            self.model.supprimer_entreprise(entreprise_id)
            self.afficher_entreprises()
            messagebox.showinfo("Succès", "Entreprise supprimée avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def afficher_entreprises(self):
        entreprises = self.model.lire_entreprises()
        self.view.afficher_entreprises(entreprises)

    def rechercher_entreprise(self, critere):
        try:
            entreprises = self.model.rechercher_entreprise(critere)
            
            if not entreprises:  # Si aucune entreprise n'est trouvée
                messagebox.showwarning("Résultat de la recherche", "Aucune entreprise trouvée.")
            else:
                self.view.afficher_resultats_recherche(entreprises)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de la recherche : {e}")


    def run(self):
        self.view.start()