from Tkinter import *

root = Tk()

menubar = Menu(root)

# create icons for comppound menu demo

newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')

# create menu items
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar, tearoff=0)
aboutmenu = Menu(menubar, tearoff=0)
themesmenu = Menu(menubar, tearoff=0)

# add icon, command and shortcut to menu item

# File menu,for open,save,save as and quit
filemenu.add_command(label="New file", accelerator='Ctrl+N', compound=LEFT, image=newicon, underline=0)
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, image=openicon, underline=0)
filemenu.add_command(label="Save", accelerator='Ctrl+S', compound=LEFT, image=saveicon, underline=0)
filemenu.add_command(label="Save as", accelerator='Shift+Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4')

# Edit menu - Undo, Redo, Cut, Copy and Paste
editmenu.add_command(label="Undo", compound=LEFT, image=undoicon, accelerator='Ctrl+Z')
editmenu.add_command(label="Redo", compound=LEFT, image=redoicon, accelerator='Ctrl+Y')
editmenu.add_separator()
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon, accelerator='Ctrl+X')
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon, accelerator='Ctrl+C')
editmenu.add_command(label="Paste", compound=LEFT, image=pasteicon, accelerator='Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label="Find", underline=0, accelerator='Ctrl+F')
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A')

# View menu -
showln = IntVar()
showln.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
showinbar = IntVar()
showinbar.set(1)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar)
hltln = IntVar()
viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=hltln)

themesmenu = Menu(menubar, tearoff=0)
viewmenu.add_cascade(label="Theme", menu=themesmenu)

# we define a color scheme dictionary containg name and color code as key value pair
clrschms = {
    '1. Default White': 'FFFFFF',
    '2. Greygarious Grey': 'D1D4D1',
    '3. Lovely Lavender': 'E1E1FF',
    '4. Aquamarine': 'D1E7E0',
    '5. Bold Beige': 'FFF0E1',
    '6. Cobalt Blue': '333AA',
    '7. Olive Green': '5B8340',
}

themechoice= StringVar()
themechoice.set('1. Default White')
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice)

# About menu - Aboutus, Help
aboutmenu.add_command(label="About")
aboutmenu.add_command(label="Help")

# add menu items
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="View", menu=viewmenu)
menubar.add_cascade(label="About", menu=aboutmenu)

# shortcut menu bar & line number bar
shortcutbar = Frame(root, height=25, bg="light gray")
shortcutbar.pack(expand=NO, fill=X)
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

# add menubar to app
root.config(menu=menubar)
root.mainloop()
