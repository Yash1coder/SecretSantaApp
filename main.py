'''
import tkinter as tk
from tkinter import messagebox
import random

# Global storage for student preferences
students = []

### Home Page ###
def home_page():
    clear_window()
    tk.Label(root, text="Secret Santa", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Button(root, text="Submit Preferences", width=30, height=2, command=submit_preferences_page).pack(pady=10)
    tk.Button(root, text="Admin Dashboard", width=30, height=2, command=admin_dashboard).pack(pady=10)
    tk.Button(root, text="Help", width=30, height=2, command=help_page).pack(pady=10)
    tk.Button(root, text="Exit", width=30, height=2, command=root.quit).pack(pady=10)


### Submit Preferences Page ###
def submit_preferences_page():
    clear_window()
    
    tk.Label(root, text="Submit Preferences", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Gift Preferences (3 items, comma-separated):").pack()
    gift_entry = tk.Entry(root, width=40)
    gift_entry.pack()

    tk.Label(root, text="Anti-Recommendations (2 items, comma-separated):").pack()
    anti_entry = tk.Entry(root, width=40)
    anti_entry.pack()

    def submit():
        name = name_entry.get().strip()
        gifts = [g.strip() for g in gift_entry.get().split(",")]
        anti_gifts = [ag.strip() for ag in anti_entry.get().split(",")]

        if not name or len(gifts) < 3 or len(anti_gifts) < 2:
            messagebox.showerror("Error", "Please enter a name, 3 gift preferences, and 2 anti-recommendations.")
            return
        
        students.append({"name": name, "gifts": gifts, "anti_gifts": anti_gifts})
        confirmation_page()

    tk.Button(root, text="Submit", width=30, command=submit).pack(pady=10)
    tk.Button(root, text="Back", width=30, command=home_page).pack(pady=10)


### Confirmation Page ###
def confirmation_page():
    clear_window()

    tk.Label(root, text="Preferences Submitted Successfully!", font=("Arial", 16, "bold"), fg="green").pack(pady=20)
    tk.Button(root, text="Return to Home", width=30, command=home_page).pack(pady=10)


### Admin Dashboard ###
def admin_dashboard():
    clear_window()

    tk.Label(root, text="Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

    if not students:
        tk.Label(root, text="No student preferences submitted yet.", font=("Arial", 12)).pack(pady=10)
    else:
        tk.Label(root, text="Student Preferences:", font=("Arial", 12, "bold")).pack()
        for student in students:
            tk.Label(root, text=f"{student['name']}: {', '.join(student['gifts'])}").pack()

    tk.Button(root, text="Run Gift Assignment", width=30, command=assign_secret_santa).pack(pady=10)
    tk.Button(root, text="Back", width=30, command=home_page).pack(pady=10)


### Secret Santa Gift Assignment ###
def assign_secret_santa():
    if len(students) < 2:
        messagebox.showerror("Error", "At least 2 students are required to run Secret Santa.")
        return

    random.shuffle(students)  # Shuffle students for randomness

    assignments = []
    for i in range(len(students)):
        giver = students[i]
        recipient = students[(i + 1) % len(students)]  # Circular assignment

        valid_gifts = [gift for gift in recipient["gifts"] if gift not in giver["anti_gifts"]]
        final_gift = valid_gifts[0] if valid_gifts else recipient["gifts"][0]  # Fallback to first gift if all are excluded

        assignments.append({
            "giver": giver["name"],
            "recipient": recipient["name"],
            "gift": final_gift
        })

    display_assignments(assignments)


### Display Final Assignments ###
def display_assignments(assignments):
    clear_window()

    tk.Label(root, text="Secret Santa Assignments", font=("Arial", 16, "bold")).pack(pady=10)

    for pair in assignments:
        tk.Label(root, text=f"{pair['giver']} → {pair['recipient']} (Gift: {pair['gift']})", font=("Arial", 12)).pack()

    tk.Button(root, text="Return to Admin Dashboard", width=30, command=admin_dashboard).pack(pady=10)


### Help Page ###
def help_page():
    clear_window()

    tk.Label(root, text="Help Guide", font=("Arial", 16, "bold")).pack(pady=10)

    help_text = """
    How to Use the Secret Santa App:

    1. Submit Preferences:
       - Click 'Submit Preferences' on the Home Page.
       - Enter your name.
       - Enter 3 gift preferences.
       - Enter 2 gifts you do NOT want to receive.
       - Click 'Submit' to save your preferences.

    2. Admin Dashboard:
       - Click 'Admin Dashboard' to see student preferences.
       - Click 'Run Gift Assignment' to automatically assign Secret Santas.

    3. Secret Santa Assignments:
       - The system ensures each student gets one recipient.
       - It avoids assigning gifts from the recipient’s anti-recommendation list.

    4. Returning to Home:
       - Click 'Back' on any page to return to the main menu.
    """
    tk.Label(root, text=help_text, justify="left", padx=20).pack()

    tk.Button(root, text="Return to Home", width=30, command=home_page).pack(pady=10)


### Utility Function to Clear Window ###
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Initialize Tkinter Window
root = tk.Tk()
root.title("Secret Santa App")
root.geometry("500x600")

home_page()  # Load home page

root.mainloop()
'''
import tkinter as tk
from tkinter import messagebox
import random

# Global storage for student preferences
students = []

### Home Page ###
def home_page():
    clear_window()
    tk.Label(root, text="Secret Santa", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Button(root, text="Submit Preferences", width=30, height=2, command=submit_preferences_page).pack(pady=10)
    tk.Button(root, text="Admin Dashboard", width=30, height=2, command=admin_dashboard).pack(pady=10)
    tk.Button(root, text="Help", width=30, height=2, command=help_page).pack(pady=10)
    tk.Button(root, text="Exit", width=30, height=2, command=root.quit).pack(pady=10)


### Submit Preferences Page ###
def submit_preferences_page():
    clear_window()
    
    tk.Label(root, text="Submit Preferences", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Gift Preferences (3 items, comma-separated):").pack()
    gift_entry = tk.Entry(root, width=40)
    gift_entry.pack()

    tk.Label(root, text="Anti-Recommendations (2 items, comma-separated):").pack()
    anti_entry = tk.Entry(root, width=40)
    anti_entry.pack()

    def submit():
        name = name_entry.get().strip()
        gifts = [g.strip() for g in gift_entry.get().split(",")]
        anti_gifts = [ag.strip() for ag in anti_entry.get().split(",")]

        if not name or len(gifts) < 3 or len(anti_gifts) < 2:
            messagebox.showerror("Error", "Please enter a name, 3 gift preferences, and 2 anti-recommendations.")
            return
        
        students.append({"name": name, "gifts": gifts, "anti_gifts": anti_gifts})
        confirmation_page()

    tk.Button(root, text="Submit", width=30, command=submit).pack(pady=10)
    tk.Button(root, text="Back", width=30, command=home_page).pack(pady=10)


### Confirmation Page ###
def confirmation_page():
    clear_window()
    
    tk.Label(root, text="Preferences Submitted Successfully!", font=("Arial", 16, "bold"), fg="green").pack(pady=20)
    tk.Button(root, text="Return to Home", width=30, command=home_page).pack(pady=10)


### Admin Dashboard ###
def admin_dashboard():
    clear_window()

    tk.Label(root, text="Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(root, text="Manage Preferences", width=30, command=manage_preferences_page).pack(pady=10)
    tk.Button(root, text="Gift Assignment", width=30, command=gift_assignment_page).pack(pady=10)
    tk.Button(root, text="Back to Home", width=30, command=home_page).pack(pady=10)


### Manage Preferences Page ###
def manage_preferences_page():
    clear_window()
    
    tk.Label(root, text="Manage Preferences", font=("Arial", 16, "bold")).pack(pady=10)

    if not students:
        tk.Label(root, text="No preferences submitted yet.").pack(pady=10)
    else:
        for student in students:
            tk.Label(root, text=f"{student['name']} - Gifts: {', '.join(student['gifts'])}").pack()

    tk.Button(root, text="Back to Admin Dashboard", width=30, command=admin_dashboard).pack(pady=10)


### Gift Assignment Page ###
def gift_assignment_page():
    clear_window()

    tk.Label(root, text="Gift Assignment", font=("Arial", 16, "bold")).pack(pady=10)

    if len(students) < 2:
        tk.Label(root, text="Not enough students to run Secret Santa.").pack(pady=10)
        tk.Button(root, text="Back to Admin Dashboard", width=30, command=admin_dashboard).pack(pady=10)
        return

    random.shuffle(students)  # Shuffle students

    assignments = []
    for i in range(len(students)):
        giver = students[i]
        recipient = students[(i + 1) % len(students)]  # Circular assignment

        valid_gifts = [gift for gift in recipient["gifts"] if gift not in giver["anti_gifts"]]
        final_gift = valid_gifts[0] if valid_gifts else recipient["gifts"][0]

        assignments.append({
            "giver": giver["name"],
            "recipient": recipient["name"],
            "gift": final_gift
        })

    for pair in assignments:
        tk.Label(root, text=f"{pair['giver']} → {pair['recipient']} (Gift: {pair['gift']})").pack()

    tk.Button(root, text="Back to Admin Dashboard", width=30, command=admin_dashboard).pack(pady=10)


### Help Page ###
def help_page():
    clear_window()

    tk.Label(root, text="Help", font=("Arial", 16, "bold")).pack(pady=10)

    help_text = """
    How to Use the Secret Santa App:

    1. Submit Preferences:
       - Click 'Submit Preferences' on the Home Page.
       - Enter your name.
       - Enter 3 gift preferences.
       - Enter 2 gifts you do NOT want to receive.
       - Click 'Submit' to save your preferences.

    2. Admin Dashboard:
       - Click 'Admin Dashboard' to go to the Admin Panel.
       - Choose 'Manage Preferences' to view student entries.
       - Choose 'Gift Assignment' to generate Secret Santa pairs.

    3. Returning to Home:
       - Click 'Back' on any page to return to the main menu.
    """
    tk.Label(root, text=help_text, justify="left", padx=20).pack()

    tk.Button(root, text="Return to Home", width=30, command=home_page).pack(pady=10)


### Utility Function to Clear Window ###
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Initialize Tkinter Window
root = tk.Tk()
root.title("Secret Santa App")
root.geometry("500x600")

home_page()  # Load home page

root.mainloop()
