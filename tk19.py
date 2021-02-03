import tkinter as tk
def print_txt():
    val_id = en1.get()
    val_name = en2.get()
    print('User ID: {} Name: {}'.format(val_id, val_name))
    en1.delete(0, tk.END)
    en2.delete(0, tk.END)
    en1.focus_set()

root=tk.Tk()
root.geometry('300x300')
lb1 = tk.Label(text='User ID')
en1 = tk.Entry()
lb2 = tk.Label(text='Name')
en2 = tk.Entry()
bt1 = tk.Button(text='Enter Data', command=print_txt)
[w.pack() for w in (lb1,en1,lb2,en2,bt1)]

root.mainloop()