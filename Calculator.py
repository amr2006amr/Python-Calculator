import tkinter as tk

root = tk.Tk()
root.title("Calculator")

def button_click(number):
    current = screen.get() # Get current value from the screen
    screen.delete(0, tk.END) # clear the  screen
    screen.insert(0,str(current + str(number)) ) # combine old and new number

def button_clear(): # clear the entire screen
    screen.delete(0, tk.END)

def button_add():
    first_number = screen.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number) # Convert to float to allow decimals
    # Clear the screen for the second number
    screen.delete(0, tk.END)

def button_subtract():
    # Save the first number and set mode to subtraction
    first_number = screen.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    screen.delete(0, tk.END)

def button_multiply():
    # Save the first number and set mode to multiplication
    first_number = screen.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    screen.delete(0, tk.END)

def button_divide():
    # Save the first number and set mode to division
    first_number = screen.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    screen.delete(0, tk.END)

def button_decimal():
    current = screen.get()
    # Check if there is already a decimal point
    if "." not in current:
        screen.insert(tk.END, ".")    

def button_equal():
    # Get the second number from the screen
    second_number = screen.get()
    # Clear the screen to display the result
    screen.delete(0, tk.END)
    
    # Check which operation was stored in the 'math' variable
    if math == "addition":
        screen.insert(0, f_num + float(second_number))

    if math == "subtraction":
        screen.insert(0, f_num - float(second_number))

    if math == "multiplication":
        screen.insert(0, f_num * float(second_number))

    if math == "division":
        # Check to avoid division by zero error
        if float(second_number) != 0:
            screen.insert(0, f_num / float(second_number))
        else:
            screen.insert(0, "Error")    


screen = tk.Entry(root, width=35, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_1.grid(row=1, column=0)
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2.grid(row=1, column=1)
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3.grid(row=1, column=2)
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0) 
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=4, column=1, columnspan=2)

button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_add.grid(row=5, column=0)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_subtract.grid(row=6, column=0)

button_dot = tk.Button(root, text=".", padx=88, pady=20, command=button_decimal)
button_dot.grid(row=6, column=1, columnspan=2)

# Create the Equal button and place it on the screen
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()