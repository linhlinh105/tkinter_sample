#
# modify to study git/github 2021/2/3
import tkinter as tk
root = tk.Tk()
root.geometry('300x270')
ms_dict = {}
for bw_int in range(1,6):
    bw_str = str(bw_int)
    ms_dict[bw_str] = tk.Message(text='borderwidge='+bw_str,relief='ridge', bd=bw_int, width=100)
    ms_dict[bw_str].pack()
root.mainloop()