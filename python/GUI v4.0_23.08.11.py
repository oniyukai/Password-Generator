import random, webbrowser, sys
import tkinter as tk
from tkinter import ttk

max_sets = 9 #生成一次密碼最大組數,預設為9
max_sections = 3 #密碼結構最大分節(段)數,預設為3
max_length = 9 #密碼結構各分節(段)最大長度,預設為9


def generate_password_cmd(): #輸出密碼並計算總長度
    output_text.insert(0.0, '\n')
    characters = [''.join((include_chkbtnss_varss[i][j].get() for j in range(4))) + include_entrys[i].get() for i in range(sections_scale.get())]
    length_spinboxs_bools = tuple(True if length_spinboxs[i].get() == '' else False for i in range(sections_scale.get()))
    for i in range(sections_scale.get()):
        length_spinboxs[i].insert(0, 0) if length_spinboxs[i].get() == '' else ...
        characters[i] += ' ' if characters[i] == '' else ''
    for i in range(sets_scale.get()):
        output_text.insert(0.0, '\n')
        for j in range(sections_scale.get()-1, -1, -1):
            output_text.insert(0.0, ''.join(random.choices(characters[j], k=int(length_spinboxs[j].get()))))
    for i in range(sections_scale.get()):
        length_spinboxs[i].delete(0, 'end') if length_spinboxs_bools[i] == True else ...
    length_spinboxs_cmd() #計算總長度並將第兩位的零刪除

def clear_settings_cmd(): #歸零所有選項
    sets_scale.set(1)
    sections_scale.set(max_sections)
    sections_scale_cmd()
    for i in range(max_sections):
        length_spinboxs[i].delete(0, 'end')
        length_spinboxs[i].insert(0, 1)
        for j in range(4):
            include_chkbtnss[i][j].deselect()
        include_entrys[i].delete(0, 'end')
    sections_scale.set(1)

def about_cmd(): #關閉'About'功能，開啟'about_window'視窗
    window_menu.entryconfig('About', state='disabled')
    def about_window_exit():
        window_menu.entryconfig('About', state='normal')
        about_window.destroy()
    about_window = tk.Tk()
    about_window.title('About Password Generator')
    about_window.geometry(f'320x100+{int((about_window.winfo_screenwidth() - 500)/2)}+{int((about_window.winfo_screenheight() - 450)/2)}')
    about_window.resizable(False,False)
    about_window.protocol('WM_DELETE_WINDOW', func=about_window_exit)
    tk.Label(about_window, bitmap='info').place(relx=0.1, rely=0.2)
    tk.Label(about_window, text='Password Generator GUI\nVersion 4.0_23.08.11', justify='left').place(relx=0.2, rely=0.1)
    ttk.Button(about_window, text='github.com', 
               command=lambda: webbrowser.get('windows-default').open_new('https://github.com/oniyukai/Password-Generator')).place(relx=0.2, rely=0.6)
    ttk.Button(about_window, text='Exit', command=about_window_exit, style='style.TButton', 
               ttk_style=ttk.Style(about_window).configure('style.TButton', background='blue', activebackground='red')).place(relx=0.6, rely=0.6)

def sections_scale_cmd(i=...): #開關輸入內容
    sections_label_var.set(f'Several of Sections: 　　　{sections_scale.get()}')
    for i in range(max_sections-1, sections_scale.get()-1, -1):
        length_spinboxs[i].config(state='disabled')
        for j in range(4):
            include_chkbtnss[i][j].config(state='disabled')
        include_entrys[i].config(state='disabled')
    for i in range(1, sections_scale.get()):
        length_spinboxs[i].config(state='normal')
        for j in range(4):
            include_chkbtnss[i][j].config(state='normal')
        include_entrys[i].config(state='normal')
    length_spinboxs_cmd() #並計算總長度並將第兩位的零刪除

def length_spinboxs_cmd(): #計算總長度並將第兩位的零刪除
    length_spinboxs_bools = tuple(True if length_spinboxs[i].get() == '' else False for i in range(sections_scale.get()))
    for i in range(sections_scale.get()):
        length_spinboxs[i].insert(0, 0) if length_spinboxs[i].get() == '' else ...
    length_spinboxs_sum = sum([int(length_spinboxs[i].get()) for i in range(sections_scale.get())])
    if len(str(length_spinboxs_sum)) == 1:
        length_label_var.set(f'Length of Sections: (total: 0{length_spinboxs_sum})')
    else:
        length_label_var.set(f'Length of Sections: (total: {length_spinboxs_sum})')
    for i in range(sections_scale.get()):
        length_spinboxs[i].delete(0, 'end') if length_spinboxs_bools[i] == True else ...
        (length_spinboxs[i].delete(0, 1) if int(length_spinboxs[i].get()) < 10 else ...) if len(length_spinboxs[i].get()) == 2 else ...

def length_spinboxs_vcmd(length_spinboxs_entry): #限輸入數字並小於2字元
    if str.isdigit(length_spinboxs_entry):
        if len(length_spinboxs_entry) < 3:
                return True
        else:
            return False
    elif length_spinboxs_entry == '':
        return True
    else:
        return False


#主視窗設定
window = tk.Tk()
window.title('Password Generator GUI v4.0_23.08.11')
window.geometry(f'{668+(max_sections-3)*49}x275+{int((window.winfo_screenwidth()-800)/2)}+{int((window.winfo_screenheight()-500)/2)}')
window.resizable(False,False)
window.protocol('WM_DELETE_WINDOW', func=lambda: sys.exit())

#選單列
window_menu = tk.Menu()
window_menu.add_command(label='Generate Password', command=generate_password_cmd)
window_menu.add_command(label='Clear Output', command=lambda: output_text.delete(0.0,'end'))
window_menu.add_command(label='Clear Settings', command=clear_settings_cmd)
window_menu.add_command(label='About', command=about_cmd)
window.config(menu=window_menu)

#主視窗物件
##問幾組
sets_label_var = tk.StringVar()
sets_label_var.set(f'Several of Sets: 　　　　　1')
tk.Label(textvariable=sets_label_var).grid(row=0, column=0, padx=10, sticky=tk.W)
sets_scale = tk.Scale(from_=1, to=max_sets, showvalue=False, length=max_sections*49-18, orient='horizontal', 
                      command=lambda i: sets_label_var.set(f'Several of Sets: 　　　　　{sets_scale.get()}'))
sets_scale.grid(row=0, column=1, padx=20, sticky=tk.E)

##問幾段
sections_label_var = tk.StringVar()
tk.Label(textvariable=sections_label_var).grid(row=1, column=0, padx=10, sticky=tk.W)
sections_scale = tk.Scale(from_=1, to=max_sections, showvalue=False, length=max_sections*49-18, orient='horizontal', 
                          command=sections_scale_cmd)
sections_scale.grid(row=1, column=1, padx=20, sticky=tk.E)

##問多長
length_label_var = tk.StringVar()
tk.Label(textvariable=length_label_var).grid(row=2, column=0, padx=10, sticky=tk.W)
length_frame = tk.Frame()
length_frame.grid(row=2, column=1, padx=15, sticky=tk.E)
length_spinboxs = []
for i in range(max_sections):
    length_spinboxs.append(tk.Spinbox(length_frame, from_=0, to=max_length, wrap='True', relief='flat', justify='center', width=2, font='Arial', 
                                      command=length_spinboxs_cmd, validatecommand=(window.register(length_spinboxs_vcmd), '%P'), validate='key'))
    length_spinboxs[i].grid(row=0, column=i, padx=7)

##問字符
include_labelframe = ttk.LabelFrame(text='Include')
include_labelframe.grid(row=3, column=0, padx=5, columnspan=2, sticky=tk.E)
include_labels = (' Numbers (0-9)', ' Lowercase Characters (a-z)', ' Uppercase Characters (A-Z)', ' !@#$%^&*', ' Input additions:')
for i in range(5):
    tk.Label(include_labelframe, text=include_labels[i]).grid(row=i, column=0,pady=3, sticky=tk.W)
include_chkbtnss_varss = [] #[[第1行第1列, 第1行第2列...], [[第2行第1列, [第2行第2列...]...]
include_chkbtnss = []
include_chkbtnss_onvalues = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*') #(第1列, 第2列...)
include_entrys = []
for i in range(max_sections):
    include_chkbtnss_varss.append([])
    include_chkbtnss.append([])
    for j in range(4):
        include_chkbtnss_varss[i].append(tk.StringVar())
        include_chkbtnss[i].append(tk.Checkbutton(include_labelframe, bd=0, activeforeground='dodgerblue', 
                                                  onvalue=include_chkbtnss_onvalues[j], offvalue='', variable=include_chkbtnss_varss[i][j]))
        include_chkbtnss[i][j].grid(row=j, column=i+1, padx=9, sticky=tk.E)
    include_entrys.append(tk.Entry(include_labelframe, width=5, relief='flat'))
    include_entrys[i].grid(row=4, column=i+1, padx=5)

##輸出框
output_frame = tk.Frame(pady=5)
output_frame.grid(row=0, column=2, rowspan=4)
output_scrollbar = tk.Scrollbar(output_frame)
output_scrollbar.pack(side='right', fill='y')
output_text = tk.Text(output_frame, width=40, height=20, relief='flat', yscrollcommand=output_scrollbar.set)
output_text.pack()
output_scrollbar.config(command=output_text.yview)



clear_settings_cmd() #將'問幾段'從0歸1
sections_scale_cmd() #停用第一段以外的輸入，並計算總長度
window.mainloop()
