from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

    def update(self, name=None, phone=None, email=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, new_name=None, new_phone=None, new_email=None):
        contact = self.find_contact(name)
        if contact:
            contact.update(new_name, new_phone, new_email)
            return True
        return False

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def get_contacts(self):
        return self.contacts

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        # Labels and entry fields using ttk
        self.name_label = Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.name_entry = Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.phone_label = Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.phone_entry = Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky=E)

        self.email_label = Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.email_entry = Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=E)

        # Buttons using ttk
        self.add_button = Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.search_button = Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=3, column=1, padx=5, pady=5, sticky=E)

        self.update_button = Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.delete_button = Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)

        self.view_button = Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)

        # Text box to display contacts using Text from tkinter
        self.contacts_text = Text(root, height=10, width=40)
        self.contacts_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            new_contact = Contact(name, phone, email)
            self.contact_book.add_contact(new_contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter all fields.")

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.contact_book.find_contact(name)
        if contact:
            self.phone_entry.delete(0, END)
            self.phone_entry.insert(END, contact.phone)
            self.email_entry.delete(0, END)
            self.email_entry.insert(END, contact.email)
        else:
            messagebox.showinfo("Not Found", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        new_phone = self.phone_entry.get()
        new_email = self.email_entry.get()
        if self.contact_book.update_contact(name, phone=new_phone, email=new_email):
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if self.contact_book.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.email_entry.delete(0, END)
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def view_contacts(self):
        self.contacts_text.delete(1.0, END)
        contacts = self.contact_book.get_contacts()
        if contacts:
            for contact in contacts:
                self.contacts_text.insert(END, f"{contact}\n")
        else:
            self.contacts_text.insert(END, "No contacts to display.")

if __name__ == "__main__":
    root = Tk()
    app = ContactBookApp(root)
    root.mainloop()
