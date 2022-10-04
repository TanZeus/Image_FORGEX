import Tkinter as tk
import ttk

root=Tk()

vertical=Scrollbar(root, orient='vertical')
vertical.pack(side=LEFT, fill='y')
vertical.config(command=im.yview)

horizontal=Scrollbar(root, orient='horizontal')
horizontal.pack(side=BOTTOM, fill-'x')
horizontal.config(command=im.xview)
