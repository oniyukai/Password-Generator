import random
import tkinter as tk

# 定義函式
def click_generated():
    output_text.insert(0.0, '\n')
    for i in range(int(sets_entry.get())):
        output_text.insert(0.0, ''.join(random.choices(numbers_var.get() + lowercase_var.get() + uppercase_var.get() + symbols_var.get() + 
                                                       additions_entry.get(), k=int(length_entry.get())))+'\n')

# tkinter物件
window = tk.Tk()
window.title('Password Generator GUI v3.1_23.08.06')
window.geometry('614x253+400+300')
window.resizable(False,False)
window.config(bg='#333333')

tk.Label(text='Version 3.1_23.08.06    Made by YUKAI', bg='#333333', fg='#CCFFF7', font=15).grid(row=0, column=0, columnspan=2)
tk.Label(text=' Enter several sets:', bg='#262626', fg='#ffffff', font=15, width=15, anchor='w').grid(row=1, column=0)
sets_entry = tk.Entry(bg='#ffffff', fg='#000000', font=15, width=20, justify='right')
sets_entry.grid(row=1, column=1)
tk.Label(text=' Enter the length:', bg='#262626', fg='#ffffff', font=15, width=15, anchor='w').grid(row=2, column=0)
length_entry = tk.Entry(bg='#ffffff', fg='#000000', font=15, width=20, justify='right')
length_entry.grid(row=2, column=1)

tk.Label(text='Include following characters:', bg='#262626', fg='#ffffff', font=15, width=35).grid(row=3, column=0, columnspan=2)
numbers_var = tk.StringVar()
tk.Checkbutton(text=' 0 - 9', bg='#262626', fg='#ffffff', selectcolor='#000000', font=15, width=10, anchor='w', 
               onvalue='0123456789', offvalue='', variable=numbers_var).grid(row=4, column=0)
lowercase_var = tk.StringVar()
tk.Checkbutton(text=' a - z', bg='#262626', fg='#ffffff', selectcolor='#000000', font=15, width=10, anchor='w', 
               onvalue='abcdefghijklmnopqrstuvwxyz', offvalue='', variable=lowercase_var).grid(row=4, column=1)
uppercase_var = tk.StringVar()
tk.Checkbutton(text=' A - Z', bg='#262626', fg='#ffffff', selectcolor='#000000', font=15, width=10, anchor='w', 
               onvalue='ABCDEFGHIJKLMNOPQRSTUVWXYZ', offvalue='', variable=uppercase_var).grid(row=5, column=0)
symbols_var = tk.StringVar()
tk.Checkbutton(text=' !@#$%^&*', bg='#262626', fg='#ffffff', selectcolor='#000000', font=15, width=10, anchor='w', 
               onvalue='!@#$%^&*', offvalue='', variable=symbols_var).grid(row=5, column=1)
tk.Label(text=' Input additions:', bg='#262626', fg='#ffffff', font=15, width=15, anchor='w').grid(row=6, column=0)
additions_entry = tk.Entry(bg='#ffffff', fg='#000000', font=15, width=20)
additions_entry.grid(row=6, column=1)
tk.Button(text='Generated', bg='#666666', fg='#ffffff',width=10, font=10, command=click_generated).grid(row=7, column=0)
tk.Button(text='Clear', bg='#666666', fg='#ffffff',width=10, font=10, command=lambda: output_text.delete(0.0, 'end')).grid(row=7, column=1)

output_text = tk.Text(bg='#000000', fg='#ffffff', font=10, width=35, height=15, bd=5)
output_text.grid(row=0, column=2, rowspan=8, columnspan=2)


window.mainloop()
