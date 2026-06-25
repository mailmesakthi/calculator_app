import tkinter as tk

def click(btn):
    entry.insert(tk.END, btn)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

row = 1
col = 0

for b in buttons:
    if b == "=":
        tk.Button(root, text=b, width=5, command=calculate).grid(row=row, column=col)
    elif b == "C":
        tk.Button(root, text=b, width=5, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=b, width=5, command=lambda x=b: click(x)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()