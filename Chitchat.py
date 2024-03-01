

import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText

class LoginSignupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login or Signup")

        self.label = tk.Label(root, text="Choose an option:")
        self.label.pack(pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.signup_button = tk.Button(root, text="Signup", command=self.signup)
        self.signup_button.pack(pady=5)

    def login(self):
        messagebox.showinfo("Login", "You clicked on Login.")

    def signup(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Signup")

        self.signup_label = tk.Label(signup_window, text="Enter your phone number or email address:")
        self.signup_label.pack(pady=10)

        self.signup_entry = tk.Entry(signup_window)
        self.signup_entry.pack(pady=10)

        self.submit_button = tk.Button(signup_window, text="Submit", command=self.send_otp)
        self.submit_button.pack(pady=10)

    def send_otp(self):
        user_input = self.signup_entry.get()

        # Placeholder values, replace with your email credentials
        email_sender = "your_email@gmail.com"
        email_password = "your_email_password"

        try:
            otp = self.generate_otp()
            self.send_email(user_input, otp, email_sender, email_password)

            # Close the signup window and open the OTP verification window
            self.open_otp_verification_window(otp, user_input)
        except Exception as e:
            messagebox.showerror("Error", f"Error sending OTP: {str(e)}")

    def generate_otp(self):
        # In a real application, you would use a more secure method to generate OTP
        # For simplicity, using a fixed value here
        return "123456"

    def send_email(self, to_address, otp, sender_email, sender_password):
        subject = "OTP for Signup"
        body = f"Your OTP for signup: {otp}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_address

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_address, msg.as_string())

    def open_otp_verification_window(self, otp, user_input):
        otp_verification_window = tk.Toplevel(self.root)
        otp_verification_window.title("OTP Verification")

        self.otp_label = tk.Label(otp_verification_window, text="Enter the OTP received:")
        self.otp_label.pack(pady=10)

        self.otp_entry = tk.Entry(otp_verification_window)
        self.otp_entry.pack(pady=10)

        self.verify_button = tk.Button(otp_verification_window, text="Verify", command=lambda: self.verify_otp(otp, user_input))
        self.verify_button.pack(pady=10)

    def verify_otp(self, expected_otp, user_input):
        entered_otp = self.otp_entry.get()

        if entered_otp == expected_otp:
            messagebox.showinfo("OTP Verified", f"OTP verification successful for {user_input}.")
        else:
            messagebox.showerror("Invalid OTP", "Entered OTP is not valid. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSignupApp(root)
    root.mainloop()

import time

class ChitChatApp:
    def __init__(self):
        print("Welcome to Chit Chat!")
        time.sleep(2)

    def ask_username(self):
        self.username = input("Enter your username: ")

    def ask_permissions(self):
        print(f"Hi {self.username}! Chit Chat would like to request the following permissions:")
        permissions = ["Contacts", "Camera", "Location", "Maps", "Microphone", "Photos"]

        for permission in permissions:
            response = input(f"Allow Chit Chat to access {permission}? (yes/no): ")
            if response.lower() != 'yes':
                print(f"Permission denied for {permission}. Chit Chat may not work correctly.")

    def search_contacts(self):
        search_query = input("Enter a contact name to search: ")
        print(f"Searching contacts for: {search_query}")

    def run(self):
        self.ask_username()
        self.ask_permissions()
        self.search_contacts()

import tkinter as tk
from tkinter import scrolledtext, Button

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chit Chat")
        self.master.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Chat box
        self.chat_box = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=10)
        self.chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Microphone and Camera buttons
        self.microphone_button = Button(self.master, text="Microphone", command=self.toggle_microphone)
        self.microphone_button.grid(row=1, column=0, padx=10, pady=10)

        self.camera_button = Button(self.master, text="Camera", command=self.toggle_camera)
        self.camera_button.grid(row=1, column=1, padx=10, pady=10)

        # Text entry for typing messages
        self.message_entry = tk.Entry(self.master, width=40)
        self.message_entry.grid(row=1, column=2, padx=10, pady=10)

        # Send button
        self.send_button = Button(self.master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=3, padx=10, pady=10)

    def toggle_microphone(self):
        print("Microphone toggled")

    def toggle_camera(self):
        print("Camera toggled")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_box.insert(tk.END, f"You: {message}\n")
            self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()


