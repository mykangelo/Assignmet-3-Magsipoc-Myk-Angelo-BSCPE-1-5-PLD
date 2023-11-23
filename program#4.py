import tkinter as tk
from tkinter import messagebox, font

def calculate_apples():
    try:
        total_money = float(entry_money.get())
        apple_price = float(entry_apple_price.get())

        if total_money < 0 or apple_price <= 0:
            raise ValueError("Please enter valid amounts.")

        num_apples = int(total_money // apple_price)
        remaining_money = total_money % apple_price

        result_text.set(f"You can buy {num_apples} apples. Remaining money: ₱{remaining_money:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
window = tk.Tk()
window.title("Apple Calculator")

# Load the background image
background_image = tk.PhotoImage(file=r"C:\Users\Mykha\OneDrive\Pictures\Saved Pictures\applesfruit.png")

# Set the size of the window to match the background image
window.geometry(f"{background_image.width()}x{background_image.height()}")

# Create a label to hold the background image
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Set background color
window.configure(bg="#e6e6e6")

# Create labels and entry widgets with common styling
common_font = font.Font(family="Arial", size=12, weight="bold")
common_bg = "red"

label_money = tk.Label(window, text="Enter total money (₱):", font=common_font, foreground="white", background=common_bg, bd=2, relief="solid")
label_money.pack(pady=5, anchor='center')

entry_money = tk.Entry(window, font=common_font, foreground="black")
entry_money.pack(pady=5, anchor='center')

label_apple_price = tk.Label(window, text="Enter price of an apple (₱):", font=common_font, foreground="white", background=common_bg, bd=2, relief="solid")
label_apple_price.pack(pady=5, anchor='center')

entry_apple_price = tk.Entry(window, font=common_font, foreground="black")
entry_apple_price.pack(pady=5, anchor='center')

# Create and pack calculate button with custom styling
calculate_button = tk.Button(window, text="Calculate", command=calculate_apples, font=common_font, bg="#4CAF50", fg="white", relief="solid")
calculate_button.pack(pady=10, anchor='center')

# Create and pack result label with larger font size, bold, green background
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 10, "bold"), background="green", foreground="white", bd=2, relief="solid")
result_label.pack(pady=10, anchor='center')

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Start the GUI main loop
window.mainloop()
