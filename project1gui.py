import tkinter as tk
from tkinter import messagebox
from project1main import personal_information, candidate_menu, voters

class VoteGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The 2023 Election")
        self.root.geometry("300x300")

        self.vote_menu()

    def clear_window(self):
        """Clears the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def vote_menu(self):
        """Creates the vote menu."""
        self.clear_window()

        header = tk.Label(self.root, text="Vote Menu")
        header.pack()

        vote_button_frame = tk.Frame(self.root)
        vote_button_frame.pack(fill=tk.X)
        vote_button = tk.Button(vote_button_frame, text="Vote", command=self.personal_info_menu)
        vote_button.pack(side=tk.TOP, pady=10, anchor=tk.CENTER)

        exit_button_frame = tk.Frame(self.root)
        exit_button_frame.pack(fill=tk.X)
        exit_button = tk.Button(exit_button_frame, text="Exit", command=self.show_vote_tally)
        exit_button.pack(side=tk.TOP, pady=10, anchor=tk.CENTER)

    def personal_info_menu(self):
        """Creates the personal information menu."""
        self.clear_window()

        header = tk.Label(self.root, text="Personal Information")
        header.pack()

        first_name_label = tk.Label(self.root, text="First Name")
        first_name_label.pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()

        last_name_label = tk.Label(self.root, text="Last Name")
        last_name_label.pack()
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack()

        age_label = tk.Label(self.root, text="Age")
        age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        back_button = tk.Button(self.root, text="Back", command=self.vote_menu)
        back_button.pack(side=tk.LEFT, padx=10)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_personal_info)
        submit_button.pack(side=tk.RIGHT, padx=10)

    def submit_personal_info(self):
        """Submits the personal information and proceeds to the candidate menu."""
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        try:
            age = int(self.age_entry.get())
            if age <= 17:
                messagebox.showerror("Error", "Voter must be 18 or older.")
                self.vote_menu()
                return
            self.voter_id = f"{first_name.lower()}_{last_name.lower()}"
            if not personal_information(first_name, last_name, age):
                messagebox.showerror("Error", "You have already voted.")
                self.vote_menu()
            else:
                self.candidate_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")
            self.vote_menu()  

    def candidate_menu(self):
        """Creates the candidate menu."""
        self.clear_window()

        header = tk.Label(self.root, text="Candidate Menu")
        header.pack()


        self.candidate_var = tk.StringVar(value="none")

        jane_radio = tk.Radiobutton(self.root, text="Jane", variable=self.candidate_var, value="Jane")
        jane_radio.pack()

        john_radio = tk.Radiobutton(self.root, text="John", variable=self.candidate_var, value="John")
        john_radio.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_vote)
        submit_button.pack(side=tk.BOTTOM, padx=10)

    def submit_vote(self):
        """Submits the vote and returns to the vote menu."""
        candidate = self.candidate_var.get()
        candidate_menu(self.voter_id, candidate)
        self.vote_menu()

    def show_vote_tally(self):
        """Displays the final tally of votes and exits the program."""
        John = sum(1 for voter in voters.values() if voter['vote'] == 'John')
        Jane = sum(1 for voter in voters.values() if voter['vote'] == 'Jane')
        messagebox.showinfo("Final Tally", f"John: {John}\nJane: {Jane}")
        self.root.destroy()

if __name__ == "__main__":
    app = VoteGUI()
    app.root.mainloop()