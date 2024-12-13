import random
import tkinter as tk
import webbrowser

max_sets = 9 #生成一次密碼最大組數,預設為9
max_sections = 3 #密碼結構最大分節(段)數,預設為3
max_length = 9 #密碼結構各分節(段)最大長度,預設為9


# 定義函式
def click_generate_password():
    text_output.insert(0.0, '\n')
    characters = [chkbtn_numbers_var[i].get() + chkbtn_lowercase_var[i].get() + chkbtn_uppercase_var[i].get() + 
                  chkbtn_symbols_var[i].get() + entry_include[i].get() for i in range(scale_sections.get())]
    boolean_error = False
    for i in range(scale_sections.get()):
        if characters[i] == '':
            text_output.insert(0.0, f'Error: uncompleted settings (section {i+1})\n')
            boolean_error = True
    try:
        if spinbox_length_cmd() > 99:
            text_output.insert(0.0, f'Error: too large of total length\n')
            boolean_error = True
    except ValueError:
        text_output.insert(0.0, f'Error: wrong input of length \n')
        boolean_error = True
    if boolean_error is True:
        return
    for i in range(scale_sets.get()):
        text_output.insert(0.0, '\n')
        for j in range(scale_sections.get()-1, -1, -1):
            text_output.insert(0.0, ''.join(random.choices(characters[j], k=int(spinbox_length[j].get()))))

def click_clear_settings():
    scale_sets.set(1)
    scale_sections.set(1)
    for i in range(max_sections):
        spinbox_length_var[i].set(1)
        chkbtn_numbers[i].deselect()
        chkbtn_lowercase[i].deselect()
        chkbtn_uppercase[i].deselect()
        chkbtn_symbols[i].deselect()
        entry_include[i].delete(0,'end')

def click_about():
    menu_window.entryconfig('About', state='disabled')
    window_about = tk.Tk()
    window_about.title('About Password Generator')
    window_about.geometry(f'320x100+{int((window.winfo_screenwidth() - 500)/2)}+{int((window.winfo_screenheight() - 450)/2)}')
    window_about.resizable(False,False)
    label_info = tk.Label(window_about, bitmap='info') #資訊小圖示
    label_info.place(relx=0.1, rely=0.2)
    label_about = tk.Label(window_about, text='Password Generator GUI\nVersion 4.0.pre_23.08.05', justify='left')
    label_about.place(relx=0.2, rely=0.1)
    def click_github():
        webbrowser.get('windows-default').open_new('https://github.com/oniyukai/Password-Generator')
    button_github = tk.Button(window_about, text='github.com', relief='groove', command=click_github)
    button_github.place(relx=0.2, rely=0.6)
    def click_exit():
        menu_window.entryconfig('About', state='normal')
        window_about.destroy()
    button_exit = tk.Button(window_about, text='　　Exit　　', relief='solid', command=click_exit)
    button_exit.place(relx=0.6, rely=0.6)

def scale_sections_cmd(i):
    label_sections_var.set(f'Several of Sections: 　　　{scale_sections.get()}')
    for i in range(max_sections-1, scale_sections.get()-1, -1):
        spinbox_length[i].config(state='disabled')
        chkbtn_numbers[i].config(state='disabled')
        chkbtn_lowercase[i].config(state='disabled')
        chkbtn_uppercase[i].config(state='disabled')
        chkbtn_symbols[i].config(state='disabled')
        entry_include[i].config(state='disabled')
    for i in range(1, scale_sections.get()):
        spinbox_length[i].config(state='normal')
        chkbtn_numbers[i].config(state='normal')
        chkbtn_lowercase[i].config(state='normal')
        chkbtn_uppercase[i].config(state='normal')
        chkbtn_symbols[i].config(state='normal')
        entry_include[i].config(state='normal')
    spinbox_length_cmd()

def spinbox_length_cmd():
    sum_length = sum([int(spinbox_length[i].get()) for i in range(scale_sections.get())])
    if sum_length < 1:
        label_length_var.set(f'Length of Sections: (total: 00)')
    elif sum_length < 10:
        label_length_var.set(f'Length of Sections: (total: 0{sum_length})')
    elif sum_length < 100:
        label_length_var.set(f'Length of Sections: (total: {sum_length})')
    else:
        label_length_var.set(f'Length of Sections: (total: 99)')
    return sum_length


# tkinter物件
window = tk.Tk() #設定主視窗
window.title('Password Generator GUI v4.0.pre_23.08.05')
window.geometry(f'{665+(max_sections-3)*49}x275+{int((window.winfo_screenwidth()-800)/2)}+{int((window.winfo_screenheight()-500)/2)}')
window.resizable(False,False)

menu_window = tk.Menu() #設定選單列
menu_window.add_command(label='Generate Password', command=click_generate_password)
menu_window.add_command(label='Clear Output', command=lambda: text_output.delete(1.0,'end'))
menu_window.add_command(label='Clear Settings', command=click_clear_settings)
menu_window.add_command(label='About', command=click_about)
window.config(menu=menu_window)


label_sets_var = tk.StringVar()
label_sets_var.set(f'Several of Sets: 　　　　　1')
label_sets = tk.Label(textvariable=label_sets_var)
label_sets.grid(row=0, column=0, padx=10, sticky=tk.W)
scale_sets = tk.Scale(from_=1, to=max_sets, showvalue=False, length=max_sections*40, orient='horizontal', 
                      command=lambda i: label_sets_var.set(f'Several of Sets: 　　　　　{scale_sets.get()}'))
scale_sets.grid(row=0, column=1, padx=25, sticky=tk.E)

label_sections_var = tk.StringVar()
label_sections = tk.Label(textvariable=label_sections_var)
label_sections.grid(row=1, column=0, padx=10, sticky=tk.W)
scale_sections = tk.Scale(from_=1, to=max_sections, showvalue=False, length=max_sections*40, orient='horizontal', command=scale_sections_cmd)
scale_sections.grid(row=1, column=1, padx=25, sticky=tk.E)

label_length_var = tk.StringVar()
label_length = tk.Label(textvariable=label_length_var)
label_length.grid(row=2, column=0, padx=10, sticky=tk.W)
frame_length = tk.Frame(window)
frame_length.grid(row=2, column=1, padx=15, sticky=tk.E)
spinbox_length_var = []
spinbox_length = []
for i in range(max_sections):
    spinbox_length_var.append(tk.StringVar())
    spinbox_length.append(tk.Spinbox(frame_length, from_=1, to=max_length, wrap='True', relief='flat', justify='center', width=2, font='Arial', 
                                     textvariable=spinbox_length_var[i], command=spinbox_length_cmd))
    spinbox_length[i].grid(row=0, column=i, padx=7)

labelframe_include = tk.LabelFrame(text='Include')
labelframe_include.grid(row=3, column=0, padx=5, columnspan=2, sticky=tk.E)
include_labels = (' Numbers (0-9)', ' Lowercase Characters (a-z)', ' Uppercase Characters (A-Z)', ' !@#$%^&*', ' Input additions:')
for i in range(5):
    label_include = tk.Label(labelframe_include, text=include_labels[i])
    label_include.grid(row=i, column=0,pady=3, sticky=tk.W)
chkbtn_numbers_var = []
chkbtn_numbers = []
chkbtn_lowercase_var = []
chkbtn_lowercase = []
chkbtn_uppercase_var = []
chkbtn_uppercase = []
chkbtn_symbols_var = []
chkbtn_symbols = []
entry_include = []
for i in range(max_sections):
    chkbtn_numbers_var.append(tk.StringVar())
    chkbtn_numbers.append(tk.Checkbutton(labelframe_include, onvalue='0123456789', offvalue='', variable=chkbtn_numbers_var[i]))
    chkbtn_numbers[i].grid(row=0, column=i+1)
    chkbtn_lowercase_var.append(tk.StringVar())
    chkbtn_lowercase.append(tk.Checkbutton(labelframe_include, onvalue='abcdefghijklmnopqrstuvwxyz', offvalue='', variable=chkbtn_lowercase_var[i]))
    chkbtn_lowercase[i].grid(row=1, column=i+1)
    chkbtn_uppercase_var.append(tk.StringVar())
    chkbtn_uppercase.append(tk.Checkbutton(labelframe_include, onvalue='ABCDEFGHIJKLMNOPQRSTUVWXYZ', offvalue='', variable=chkbtn_uppercase_var[i]))
    chkbtn_uppercase[i].grid(row=2, column=i+1)
    chkbtn_symbols_var.append(tk.StringVar())
    chkbtn_symbols.append(tk.Checkbutton(labelframe_include, onvalue='!@#$%^&*', offvalue='', variable=chkbtn_symbols_var[i]))
    chkbtn_symbols[i].grid(row=3, column=i+1)
    entry_include.append(tk.Entry(labelframe_include, width=5, relief='flat'))
    entry_include[i].grid(row=4, column=i+1, padx=5)

frame_output = tk.Frame(pady=5)
frame_output.grid(row=0, column=2, rowspan=4)
scrollbar_output = tk.Scrollbar(frame_output)
scrollbar_output.pack(side='right', fill='y')
text_output = tk.Text(frame_output, width=40, height=20, relief='flat', yscrollcommand=scrollbar_output.set)
text_output.pack()
scrollbar_output.config(command=text_output.yview)



scale_sections_cmd(i)
window.mainloop()