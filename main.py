import datetime
import random
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
import pywhatkit
import webbrowser

# File:
excel_file_path = r"D:\Projects'23\Bday Final\test1.xlsx"
df = pd.read_excel(excel_file_path)

class BirthdayReminderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Reminder")

        # Define the country code here
        self.country_code = '+'  # Add your country code here

        self.label = tk.Label(root, text="BIRTHDAY Reminder", font=("Helvetica", 16))
        self.label.pack()

        self.label_today = tk.Label(root, text=f"TODAY: {datetime.datetime.now().strftime('%d/%m/%Y')}", font=("Helvetica", 12))
        self.label_today.pack()

        self.button_show_birthdays = tk.Button(root, text="Show Today's Birthdays", command=self.show_birthdays)
        self.button_show_birthdays.pack()

    def show_birthdays(self):
        # Ask if the user has logged into WhatsApp Web
        is_logged_in = self.confirm_logged_in()
        if is_logged_in:
            self.root.withdraw()  # Hide the main window

            # Create a new window to display birthday names and buttons
            self.birthday_window = tk.Toplevel()
            self.birthday_window.title("Birthday People")

            bday_numbers, bday_wishes = get_birthday_info(df)
            for name in bday_wishes.keys():
                tk.Label(self.birthday_window, text=f"{name} has a birthday today!").pack()
                tk.Button(self.birthday_window, text="Send Wishes", command=lambda n=name: self.send_whatsapp_wishes(n)).pack()

            # Add the "WISH ALL" button after showing birthdays
            self.button_wish_all = tk.Button(self.birthday_window, text="WISH ALL", command=self.wish_all)
            self.button_wish_all.pack()

    def send_whatsapp_wishes(self, name):
        bday_wishes = get_birthday_info(df)[1]

        # Retrieve the phone number directly from the DataFrame
        number = df.loc[df['NAME'] == name, 'NUMBER'].iloc[0]
        message = bday_wishes[name]

        # Close the birthday window after clicking the button
        self.birthday_window.destroy()

        # Move the rest of the logic to another method
        self.schedule_whatsapp_message(number, message)

    def wish_all(self):
        self.birthday_window.destroy()  # Close the birthday window after clicking the button

        bday_numbers, bday_wishes = get_birthday_info(df)

        total_messages = len(bday_wishes)
        approximate_time = total_messages * 35  # Assuming 3 seconds per message

        response = messagebox.askyesno("Wish All Confirmation", f"You are about to send wishes to {total_messages} people. Approximate time to finish: {approximate_time} seconds. Do you want to proceed?")
        if response:
            start_time = time.time()
            for name in bday_wishes.keys():
                self.send_whatsapp_wishes(name)
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Wish All Completion", f"All wishes sent successfully. Time taken: {elapsed_time:.2f} seconds.")

    def confirm_logged_in(self):
        response = messagebox.askyesno("WhatsApp Web Confirmation", "Have you logged into WhatsApp Web today?")
        if not response:
            self.redirect_to_whatsapp_web()
        return response

    def redirect_to_whatsapp_web(self):
        messagebox.showinfo("Redirecting", "You will be redirected to WhatsApp Web. Please log in and return to the application.")
        webbrowser.open("https://web.whatsapp.com")

    def schedule_whatsapp_message(self, number, message):
        try:
            full_number = self.country_code + str(number)
            now = datetime.datetime.now()
            scheduled_time = now + datetime.timedelta(minutes=1)  # Delay of one minute
            pywhatkit.sendwhatmsg(full_number, message, scheduled_time.hour, scheduled_time.minute, 15, True, 2)
            # pywhatkit.sendwhats_image(full_number, image_bday)  # Uncomment if needed
            time.sleep(3)
            messagebox.showinfo("Birthday Reminder", f"Message sent successfully for {full_number}.")
        except Exception as e:
            messagebox.showerror("Birthday Reminder", f"Failed to schedule a message to {number}: {str(e)}")

def get_birthday_info(df):
    today = datetime.datetime.now()
    name = df['NAME']
    date = df['DOB']
    year = df['YEAR']
    numbers = df['NUMBER']
    age = [] # calculating age
    bday_numbers = [] # to store birthday people numbers
    bday_wishes = {}

    thisyear = today.strftime("%Y")
    dob_input = today.strftime("%d/%m")

    for k in year: # age
        ageyear = int(thisyear) - k
        age.append(ageyear)

    for i, j in enumerate(date): # fetching who's bday
        if dob_input == j:
            store = i
            number_store = numbers[store]
            bday_numbers.append(number_store)
            message = [
                f"Wishing You A Very Happy Birthday {name[store]}! May All Your Dreams Come True On This Auspicious {age[store]}th Birthday",
                f"{age[store]}th Is A Perfect Age {name[store]}. You're Just Old Enough To Recognize Your Mistakes, But Still Young Enough To Make Some More. Happy Birthday!",
                f"Congratulations {name[store]} On Your {age[store]}th Birthday! Wishing You A Truly Fabulous Day."
            ]
            rd_msg = random.choice(message)
            bday_wishes[name[store]] = rd_msg

    return bday_numbers, bday_wishes

if __name__ == "__main__":
    image_bday = r"bday_wish1.jpg"  # Update with the actual path to your birthday image

    root = tk.Tk()
    gui = BirthdayReminderGUI(root)
    root.mainloop()
