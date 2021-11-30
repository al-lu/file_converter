import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image  
import pandas as pd
import ntpath
import os

###############################
###   Initialize tkinter    ###
###############################
root= tk.Tk()

###########################
###    App Background   ###
###########################

canvas1 = tk.Canvas(root, width = 300, height = 450, bg = 'gray10', relief = 'raised')
canvas1.pack()

#########################
###   Main Heading    ###
#########################

label1 = tk.Label(root, text='Linkkuveitsi', bg = 'gray10', fg = 'snow')
label1.config(font=('Courier', 20))
canvas1.create_window(150, 60, window=label1)

#######################
###   Cool image    ###
#######################
#try:
    # Relative path
    ##img = Image.open("")
    ##width, height = img.size
    #print(width)
    #print(height)
    ##img = img.resize((round(150/height*width) , round(300)))

    # Saved in the same relative location
    # img.save("resized_picture.jpg")

    #img = ImageTk.PhotoImage(Image.open("swiss_army_knife.png")) 
    ##img = ImageTk.PhotoImage(img) 
    #print(img.height()) 
    #print(img.width())
# except IOError:
#     pass
# canvas1.create_image(150, 200, anchor="center", image=img) 

#######################
###    File name    ###
#######################

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail + '.json' or ntpath.basename(head + '.json')



#################################
###   CSV Conversion to JSON  ###
#################################

def getCSV ():
    global read_file
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv(import_file_path)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='DodgerBlue3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def convertToJSON ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.json', initialfile=path_leaf(import_file_path))
    read_file.to_json (export_file_path, orient='records')

saveAsButton_JSON = tk.Button(text='Convert CSV to JSON', command=convertToJSON, bg='DodgerBlue3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JSON)



#####################################
###   EXCEL Conversion to JSON    ###
#####################################

def getExcel ():
    global read_file
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (import_file_path)
    
browseButton_Excel = tk.Button(text="      Import EXCEL File     ", command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=browseButton_Excel)

def convertToJSON ():
    global read_file
    export_file_path = filedialog.asksaveasfilename(defaultextension='.json', initialfile=path_leaf(import_file_path))
    read_file.to_json (export_file_path, orient='records', encoding='utf-8')

saveAsButton_JSON = tk.Button(text='Convert EXCEL to JSON', command=convertToJSON, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 280, window=saveAsButton_JSON)

#####################################
###   EXCEL Conversion to CSV    ###
#####################################

def getExcel ():
    global read_file
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (import_file_path)
    
browseButton_Excel = tk.Button(text="      Import Excel File     ", command=getExcel, bg='yellow', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 330, window=browseButton_Excel)

def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv', initialfile=path_leaf(import_file_path))
    read_file.to_csv (export_file_path, index = None, header=True)

saveAsButton_CSV = tk.Button(text='Convert Excel to CSV', command=convertToCSV, bg='yellow', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 380, window=saveAsButton_CSV)

##############################
###    Exit Application    ###
##############################

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 430, window=exitButton)

root.mainloop()