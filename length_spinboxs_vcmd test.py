import tkinter as tk


#限數字,不能是空,小於2字元
def vcmd(spinbox_entry): 
    if str.isdigit(spinbox_entry):
        if len(spinbox_entry) < 3:
            return True
        else:
            return False
    else:
        return False
lambda spinbox_entry: (True if len(spinbox_entry) < 3 else False) if str.isdigit(spinbox_entry) else False

#限數字,小於2字元
def vcmd(spinbox_entry): 
    if str.isdigit(spinbox_entry):
        if len(spinbox_entry) < 3:
                return True
        else:
            return False
    elif spinbox_entry == '':
        return True
    else:
        return False
lambda spinbox_entry: (True if spinbox_entry=='' else (True if len(spinbox_entry) < 3 else False)) if str.isdigit(spinbox_entry) or spinbox_entry=='' else False

#限數字,不能是空
str.isdigit

#限數字
def vcmd(spinbox_entry): 
    if str.isdigit(spinbox_entry) or spinbox_entry=='':
        return True
    else:
        return False
lambda spinbox_entry: True if str.isdigit(spinbox_entry) or spinbox_entry=='' else False



#tk物件
window = tk.Tk()
window.geometry('200x100+600+300')
spinbox = tk.Spinbox(from_=1, to=9, wrap='True', validate='key', validatecommand=(window.register(vcmd), '%P'))
spinbox.grid(row=0, column=0, padx=20, pady=20)



window.mainloop()