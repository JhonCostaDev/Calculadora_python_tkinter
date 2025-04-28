import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.configure(bg='gray')

#input camp
display = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Create enter

def click(key):
    default = display.get()
    display.delete(0, tk.END)
    display.insert(0, default + key)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, 'Erro')

def clear():
    display.delete(0, tk.END)


def main():

    # buttons
    # button_1 = tk.Button(window, text='1', width=5, height=2, font=('Arial', 18))
    # button_1.grid(row=1, column=0, padx=5, pady=5)
    buttons = [
        ("C", 1, 0), ("/", 1, 1), ("*", 1, 2), ("-", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), (".", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
        ("0", 5, 1),
    ]

    for (text, row, column) in buttons:
        #
        if text == '=':
            botao = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
        elif text == "C": 
            botao = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18),command=clear)

        else:
            botao = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: click(t))
        
        botao.grid(row=row, column=column, padx=5, pady=5)




    # show window
    window.mainloop()

if __name__ == '__main__':
    main()


