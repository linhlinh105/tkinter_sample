import tkinter as tk
def print_txtval():
    val_en =en.get()
    print(val_en)
root = tk.Tk()
root.title('get text box')
root.geometry('350x150')
lb= tk.Label(text='Label')
en=tk.Entry()
bt= tk.Button(text='button',command=print_txtval)
lb.pack()
en.pack()
bt.pack()
root.mainloop()