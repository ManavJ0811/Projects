import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("340x400")
root.resizable(False, False)

# Entry widget to show expression
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief="sunken", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to update expression
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),# button name , row, column
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]
# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear(AC) button
tk.Button(root, text='C', width=23, height=2, font=('Arial', 14), command=clear).grid(row=5, column=0, columnspan=4)

# Running the GUI loop
root.mainloop()