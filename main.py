from ButtonsFunctions import *
from tkinter import *
import random

btf = Buttons_Fun()

m = Tk()
m.title('Main window')
m.geometry("170x200+30+30")
m.eval('tk::PlaceWindow %s center' % m.winfo_pathname(m.winfo_id()))

buttons = ['Students', 'Professors', 'Courses', 'Marks', 'Reports']
ct = [random.randrange(256) for x in range(3)]
brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
ct_hex = "%02x%02x%02x" % tuple(ct)
bg_colour = '#' + "".join(ct_hex)
b1 = Button(m,text=buttons[0],fg='White' if brightness < 120 else 'Black',bg=bg_colour,command = btf.S_OpenningWindows)
b1.place(x=25, y=30 + 0 * 30, width=120, height=25)
b2 = Button(m,text=buttons[1],fg='White' if brightness < 120 else 'Black',bg=bg_colour ,command = btf.P_OpenningWindows)
b2.place(x=25, y=30 + 1 * 30, width=120, height=25)
b3 = Button(m,text=buttons[2],fg='White' if brightness < 120 else 'Black',bg=bg_colour,command = btf.C_OpenningWindows)
b3.place(x=25, y=30 + 2 * 30, width=120, height=25)
b4 = Button(m,text=buttons[3],fg='White' if brightness < 120 else 'Black',bg=bg_colour,command = btf.M_OpenningWindows)
b4.place(x=25, y=30 + 3 * 30, width=120, height=25)
b5 = Button(m,text=buttons[4],fg='White' if brightness < 120 else 'Black',bg=bg_colour,command = btf.Save_report)
b5.place(x=25, y=30 + 4 * 30, width=120, height=25)
mainloop()