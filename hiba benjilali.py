import tkinter as tk
from tkinter import messagebox
import re


class Contact:
    def __init__(self, nom, telephone):
        self.nom = nom
        self.telephone = telephone

    def __str__(self):
        return f"{self.nom}: {self.telephone}"

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = []
        self.entries = {}
        self.create_gui()

    def create_gui(self):
        for i, label in enumerate(["nom:", "telephone:"]):
            tk.Label(self.root, text=label, fg="#333").grid(row=i, column=0)
            entry = tk.Entry(self.root, width=30)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[label[:-1]] = entry

        tk.Button(self.root, text="ajouter Contact", command=self.add_contact,  bg="brown").grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="supprimer", command=self.supprimer_contact, bg="brown").grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="modifier", command=self.modifier_contact, bg="brown").grid(row=4, column=1, padx=10, pady=10)

    def add_contact(self):
        nom, telephone = self.entries["nom"].get(), self.entries["telephone"].get()
        if nom and telephone:
            if re.match("^[0-9]+$", telephone) and len(telephone) >= 10:
                contact = Contact(nom, telephone)
                self.contacts.append(contact)
                self.listbox.insert(tk.END, str(contact))
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "le numero de téléphone doit être une valeur numérique comportant au moins 10 chiffres")
        else:
            messagebox.showwarning("Input Error", "Les champs nom et téléphone doivent être remplis")

    def supprimer_contact(self):
        index = self.listbox.curselection()
        if index:
            del self.contacts[index[0]]
            self.listbox.delete(index)

    def modifier_contact(self):
        index = self.listbox.curselection()
        if index:
            contact = self.contacts[index[0]]
            self.clear_entries()
            self.entries["nom"].insert(0, contact.nom)
            self.entries["telephone"].insert(0, contact.telephone)
            tk.Button(self.root, text="Sauvegarder les modifications", command=lambda: self.save_changes(index),  bg="brown").grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def save_changes(self, index):
        nom, telephone = self.entries["nom"].get(), self.entries["telephone"].get()
        if nom and telephone:
            if re.match("^[0-9]+$", telephone) and len(telephone) >= 10:
                contact = Contact(nom, telephone)
                self.contacts[index[0]] = contact
                self.listbox.delete(index)
                self.listbox.insert(index, str(contact))
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "le numero de téléphone doit être une valeur numérique comportant au moins 10 chiffres")
        else:
            messagebox.showwarning("Input Error", "Les champs nom et téléphone doivent être remplis")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Manager")
        self.configure(bg="#f0f0f0")
        self.contact_manager = ContactManager(self)
        self.mainloop()

        
if __name__ == "__main__":
    app = Application()