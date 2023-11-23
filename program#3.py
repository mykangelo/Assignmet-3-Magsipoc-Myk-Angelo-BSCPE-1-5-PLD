import tkinter as tk
from tkinter import ttk

def fruits_cashier(fruit_name, quantity_var):
    try:
        quantity = int(quantity_var.get())
        if quantity < 0:
            raise ValueError("Please enter a non-negative number.")
        return quantity
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
        return None

def calculate_total_amount(num_apples, num_oranges, apple_price, orange_price):
    return num_apples * apple_price + num_oranges * orange_price

def calculate_button_click():
    selected_fruit = fruits_var.get()
    
    num_apples = fruits_cashier("apple", apple_quantity_var) if selected_fruit in ["Apple", "Both"] else 0
    num_oranges = fruits_cashier("orange", orange_quantity_var) if selected_fruit in ["Orange", "Both"] else 0

    if num_apples is not None and num_oranges is not None:
        total_amount = calculate_total_amount(num_apples, num_oranges, 20, 25)
        result_label.config(text=f"Total amount to pay: {total_amount:.2f} Pesos", background="yellow")



root = tk.Tk()
root.title("Fruits Cashier")

background_image = tk.PhotoImage(file=r"C:\Users\Mykha\OneDrive\Pictures\Saved Pictures\appleorange.png")

background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"), relief="ridge", padding=10, borderwidth=2, background="#4CAF50", foreground="green")
style.configure("TLabel", font=("Helvetica", 12, "bold"), padding=10, borderwidth=2, relief="solid", foreground="white")

apple_quantity_var = tk.StringVar()
orange_quantity_var = tk.StringVar()

fruits_var = tk.StringVar()
fruits_menu = ttk.OptionMenu(root, fruits_var, "Select Fruit", "Apple", "Orange", "Both")
fruits_menu.grid(column=0, row=0, columnspan=2, pady=10)

apple_frame = ttk.Frame(root, padding="10")
apple_frame.grid(column=0, row=1, padx=10, pady=10)

apple_label = ttk.Label(apple_frame, text="How many apples do you want to buy?", font=("Helvetica", 12, "bold"))
apple_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

apple_entry = ttk.Entry(apple_frame, textvariable=apple_quantity_var)
apple_entry.grid(column=1, row=0, padx=10)

orange_frame = ttk.Frame(root, padding="10")
orange_frame.grid(column=1, row=1, padx=10, pady=10)

orange_label = ttk.Label(orange_frame, text="How many oranges do you want to buy?", font=("Helvetica", 12, "bold"))
orange_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

orange_entry = ttk.Entry(orange_frame, textvariable=orange_quantity_var)
orange_entry.grid(column=1, row=0, padx=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_button_click, style="TButton")
calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold", ), foreground="red")
result_label.grid(column=0, row=3, columnspan=2)

def hide_widgets(frame):
    frame.grid_remove()
    entry = frame.winfo_children()[1]
    entry.delete(0, tk.END)

hide_widgets(orange_frame)
hide_widgets(apple_frame)

def on_fruit_change(*args):
    selected_fruit = fruits_var.get()
    
    if selected_fruit == "Apple":
        hide_widgets(orange_frame)
        apple_frame.grid()
    elif selected_fruit == "Orange":
        hide_widgets(apple_frame)
        orange_frame.grid()
    elif selected_fruit == "Both":
        apple_frame.grid()
        orange_frame.grid()

    apple_label.configure(background="red" if selected_fruit in ["Apple", "Both"] else root.cget("bg"))
    orange_label.configure(background="orange" if selected_fruit in ["Orange", "Both"] else root.cget("bg"))

fruits_var.trace("w", on_fruit_change)

root.mainloop()
