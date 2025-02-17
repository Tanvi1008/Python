import instaloader
import tkinter as tk
from tkinter import messagebox


def fetch_instagram_details():
    username = entry_username.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        details = (f"Username: {profile.username}\n"
                   f"Full Name: {profile.full_name}\n"
                   f"Followers: {profile.followers}\n"
                   f"Following: {profile.followees}\n"
                   f"Bio: {profile.biography}")
        messagebox.showinfo("Instagram Details", details)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch details: {e}")


# GUI Setup
root = tk.Tk()
root.title("Instagram User Details")
root.geometry("400x300")

tk.Label(root, text="Enter Instagram Username:").pack(pady=10)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

tk.Button(root, text="Fetch Details", command=fetch_instagram_details).pack(pady=20)

root.mainloop()
