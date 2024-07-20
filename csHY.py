import time
import os
from tkinter import *
from tkinter import ttk,filedialog,messagebox
import pyautogui

def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory() # opens a dialog box for selecting directory
    
    if folder_path:
        entry_var.set(folder_path) # entry variable to take folder path in the text box
    else:
        entry_var.set("No folder selected")

def take_screenShot():
    file_name = file_var.get()
    if folder_path and file_name:

        if not os.access(folder_path,os.W_OK):
            messagebox.showerror("Error","You don't have permissions to save files in the directory.")

            return

        #construct the full file path
        file_path = os.path.join(folder_path,f"{file_name}.png")
        # hide the window
        win.withdraw()

        #Give some time for the window to hide
        win.after(200,lambda:capture_screenShot(file_path)) # 200 miliseconds
    else:
        messagebox.showerror("Error","Please select a folder and enter a file name.")

def capture_screenShot(file_path):
    # get the file name form the variable

    ss = pyautogui.screenshot()

    try:
        # save the screenshot to the specified path
        ss.save(file_path)
        messagebox.showinfo("Success",f"ScreenShot saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Failed",f"Failed to save ScreenShot : {e}")

    # show the window again
    win.deiconify()


# create the main window
win = Tk()


win.title("Easier to take screenshot")
win.geometry("800x280")
win.config(bg = "#4b5262")
win.resizable(False,False)


# variable to store
entry_var = StringVar(value="Choose folder")
file_var = StringVar()
folder_var = StringVar()
msgfile = StringVar(value="Enter file name in the box : ")

# create a entry box to show an entry box

entry = Entry(win,textvariable=entry_var,font=('Time New Roman',15),state="readonly",bd=1,bg="brown")
entry.place(x=10,y=15,height=50,width=680)

# create a button to open a the folder dialog
fileOption = Button(win,text="select",font=('Time New Roman',15),cursor='hand2',command=choose_folder) #hand2 is a cursor pointer
fileOption.place(x=700,y=15,height=50,width=90)

msgFile = Entry(win,textvariable=msgfile,font=('Time New Roman',15),state="readonly")
msgFile.place(x=50,y=85,height=50,width=350)

entryFile_name = Entry(win,textvariable=file_var,font=('Time New Roman',15))
entryFile_name.place(x=410,y=85,height=50,width=340)


# create a button to take screen shot
button = Button(win,text="Take Screenshot",font=('Time New Roman',25),cursor="hand2",command=take_screenShot)
button.place(x=150,y=160,height=50,width=500)

# footer frame
footer_frame = Frame(win,bg="grey",height=10)
footer_frame.pack(side=BOTTOM,fill=X,padx=10,pady=10)

footer_label=Label(footer_frame,text="Simple utility for taking screenshot created by Harsh Yadav check it on github @HarshYadav152 for Source Code",bg="grey")
footer_label.pack(side=LEFT,padx=10)

win.mainloop()