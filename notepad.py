from tkinter import *
top=Tk()
#size of the window "500x500" with geometry()function
top.geometry("700x500")
#title of the window
top.title("Untitled")
#create the menubar
menubar=Menu(top)
#Create the menu name as file
file=Menu(menubar,tearoff=0)
#Add the item to file menu
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
#Add the separator
file.add_separator()
file.add_command(label="Exit",command=top.quit)
#Add this filemenu to the menubar
menubar.add_cascade(label="File",menu=file)

#Create the menu name as Edit
edit=Menu(menubar,tearoff=0)
#Add the item to the edit menu
edit.add_command(label="Undo")
#Add the separator
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
#Add the separator
edit.add_separator()
edit.add_command(label="Find...")
edit.add_command(label="Replace")
edit.add_command(label="Go To...")
edit.add_separator()
edit.add_command(label="Select All")
edit.add_command(label="Time Date")
# Add this edit menu to the menubar
menubar.add_cascade(label="Edit",menu=edit)
#Create the menu name as format
format=Menu(menubar,tearoff=0) 
#Add checkbutton with word wrap label
format.add_checkbutton(label="Word Wrap")
#Create a sub menu for font
submenu_font=Menu(format,tearoff=0)
submenu_font.add_command(label="Font Style")

#Create a sub menu for font weight
submenu_font_weight=Menu(submenu_font,tearoff=0)
for i in range(4,38):
	submenu_font_weight.add_command(label=i*2)

"""submenu_font_weight.add_command(label="14")
submenu_font_weight.add_command(label="16")
submenu_font_weight.add_command(label="18")
submenu_font_weight.add_command(label="20")
submenu_font_weight.add_command(label="22")
submenu_font_weight.add_command()"""
#Add the sumbmenu_font_weight to submenu
submenu_font.add_cascade(label="Font Weight",menu=submenu_font_weight)
#Add the submenu to the format menu
format.add_cascade(label="Font ",menu=submenu_font,underline=1)

#Add this format menu to the menubar
menubar.add_cascade(label="Format",menu=format)

#Create the menu name as Help
help=Menu(menubar,tearoff=0)
#Add the item to the help menu
help.add_command(label="View Help")
#Add the separator
help.add_separator()
help.add_command(label="About Editor")
#Add this help menu to the menubar
menubar.add_cascade(label="Help",menu=help)
top.config(menu=menubar)
font_weight=23
text=Text(top,font=font_weight)
text.pack(fill=BOTH,expand=YES)
top.mainloop()