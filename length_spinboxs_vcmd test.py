import tkinter as tk

#限數字,不能是空,小於2字元
def vcmd(spinbox_entry):
    return str.isdigit(spinbox_entry) and len(spinbox_entry) < 3
lambda spinbox_entry: str.isdigit(spinbox_entry) and len(spinbox_entry) < 3

#限數字,小於2字元
def vcmd(spinbox_entry): 
    return str.isdigit(spinbox_entry) and len(spinbox_entry) < 3 or spinbox_entry == ''
lambda spinbox_entry: str.isdigit(spinbox_entry) and len(spinbox_entry) < 3 or spinbox_entry == ''

#限數字,不能是空
str.isdigit

#限數字
def vcmd(spinbox_entry):
    return str.isdigit(spinbox_entry) or spinbox_entry==''
lambda spinbox_entry: str.isdigit(spinbox_entry) or spinbox_entry==''



def main():
    window = tk.Tk()
    window.geometry('200x100+600+300')
    spinbox = tk.Spinbox(from_=1, to=9, wrap='True', validate='key', validatecommand=(window.register(vcmd), '%P'))
    spinbox.grid(row=0, column=0, padx=20, pady=20)

    window.mainloop()

if __name__ == '__main__':
    main()