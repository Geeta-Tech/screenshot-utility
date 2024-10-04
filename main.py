import os
from tkinter import *
from tkinter import filedialog, messagebox
import pyautogui
def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory()  # opens a dialog box for selecting directory

    if folder_path:
        entry_var.set(folder_path)  # entry variable to take folder path in the text box
    else:
        entry_var.set("No folder selected")
def take_screenShot():
    file_name = file_var.get()
    if folder_path and file_name:
        if not os.access(folder_path, os.W_OK):
            messagebox.showerror("Error", "You don't have permissions to save files in the directory.")
            return
        # construct the full file path
        file_path = os.path.join(folder_path, f"{file_name}.png")
        # hide the window
        win.withdraw()
        # Give some time for the window to hide
        win.after(200, lambda: capture_screenShot(file_path))  # 200 miliseconds
    else:
        messagebox.showerror("Error", "Please select a folder and enter a file name.")
def capture_screenShot(file_path):
    # get the file name form the variable
    ss = pyautogui.screenshot()
    try:
        # save the screenshot to the specified path
        ss.save(file_path)
        messagebox.showinfo("Success", f"Screenshot saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Failed", f"Failed to save screenshot: {e}")
    # show the window again
    win.deiconify()
# create the main window
win = Tk()
win.title("Easier to take screenshot")
win.geometry("800x280")
win.config(bg="#161b22")
win.resizable(False,False)
# variable to store
entry_var = StringVar(value="Choose folder")
file_var = StringVar()
msg_file = StringVar(value="Enter file name in the box : ")
# create a entry box to show an entry box
entry = Entry(win, textvariable=entry_var, font=('Time New Roman', 20), state="readonly", bd=1)
entry.place(relx=0.025, rely=0.05, relheight=0.2, relwidth=0.71)
# create a button to open the folder dialog
file_option = Button(win, text="select", font=('Time New Roman', 25),cursor='hand2',command=choose_folder)  # hand2 is a cursor pointer
file_option.place(relx=0.765, rely=0.05, relheight=0.2, relwidth=0.21)
msg_file = Entry(win, textvariable=msg_file, font=('Time New Roman', 15), state="readonly")
msg_file.place(relx=0.05, rely=0.3, relheight=0.2, relwidth=0.44)
entry_file_name = Entry(win, textvariable=file_var, font=('Time New Roman', 20))
entry_file_name.place(relx=0.51, rely=0.3, relheight=0.2, relwidth=0.44)
# create a button to take screenshot
button = Button(win, text="Take Screenshot", font=('Time New Roman', 25), cursor="hand2", command=take_screenShot)
button.place(relx=0.2, rely=0.59, relheight=0.2, relwidth=0.6)
# footer frame
footer_frame = Frame(win, bg="grey", height=10)
footer_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)
footer_label = Label(footer_frame,text="Simple utility for taking screenshot created by Harsh Yadav check it on github @HarshYadav152 for Source Code",bg="grey")
footer_label.pack(side=LEFT, padx=10)
# bind return key with button
win.bind('<Return>', lambda event:button.invoke())
# Bind esc key for closing window
win.bind("<Escape>", lambda event:win.destroy())
# Bind m key for minimize the window
win.bind("<Control+m>", lambda event:win.iconify())
win.bind("<Control+M>", lambda event:win.iconify())
# Bind s key for open file dialog
win.bind("<Control+o>", lambda event:file_option.invoke())
win.bind("<Control+O>", lambda event:file_option.invoke())

win.mainloop()
