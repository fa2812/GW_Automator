# Python modules
import time
import subprocess

# Extra modules
import pyautogui as pygui
import customtkinter as ctk

# Dependent files
import report_functions as rf

## Main Window ##
root = ctk.CTk()
root.geometry("540x200")
root.title("GASWorkS Automator & Folder Macros")
root.resizable(width=False,height=False)

## Main Variables ##
code = ""
rev = ""
draw_report = ""
code_var = ctk.StringVar()  # project code
rev_var = ctk.StringVar()   # GASWorkS file revision
replace_var = ctk.IntVar()  # overwrite existing documents if == 1
drawing_var = ctk.IntVar()  # prints noded drawing if == 1
new_project = ctk.IntVar()  # new project folder 
project_1 = ctk.StringVar()
project_1.set("Project 1: ")    
project_2 = ctk.StringVar()
project_2.set("Project 2: ")

def publish():
    # main function for publishing reports
    # assigned to the "Publish" button
    global code
    global rev
    global draw_report
    code = code_var.get()
    rev = "Rev" + rev_var.get()
    draw_report = drawing_var.get()
    full(False,draw_report)

def full(replace,draw):
    # function that calls report functions to publish all reports
    # called in publish()
    for i in range(3):
        rf.data_report(i,replace,code,rev)
        time.sleep(0.2)
    rf.summary(replace,code,rev)
    time.sleep(0.2)
    if draw == 1:
        rf.drawing(replace,code,rev)

def open_outputs():
    # opens the Outputs folder
    # assigned to the "Open Outputs" button
    subprocess.Popen(r'explorer ' + rf.outputs_folder)

def project_folder_format(project_code):
    # Checks if opened project has already been registered
    # Returns True if project folder is new format, False if it is old format
    new_format_list = open("references\\Projects List (New Format).txt", "r") 
    old_format_list = open("references\\Projects List (Old Format).txt", "r") 
    for i in new_format_list:
        if i == project_code:   
            return True
    for i in old_format_list:
        if i == project_code:
            return False
    if new_project.get() == 1:
        # append to new format list
        return True
    else:
        # append to old format list
        return False

def project_tabs():
    project_path = root.clipboard_get()
    project_name = project_path.split("\\")
    if project_name[2] == "Live Projects":
        project_code = project_name[3].split()[0]
    elif project_name[2] == "EDB Projects":
        project_code = project_name[4].split()[0]
    subprocess.Popen(r'explorer ')
    time.sleep(2)
    for i in range(3):
        pygui.hotkey("ctrl","t")
        time.sleep(0.5)
    tab_number = 1
    while tab_number < 5:
        pygui.hotkey("ctrl",str(tab_number))
        time.sleep(1)
        pygui.press("tab")
        time.sleep(1)
        pygui.hotkey("ctrl","l")
        pygui.hotkey("ctrl","v")
        if tab_number == 2: # Window 2: Drawings folder
            if project_folder_format(project_code):
                pygui.write("\\3. Design\\2. Gas\\1. Drawings")
            else:
                pygui.write("\\5, Design\\Drawings")
            # for new projects: pygui.write("\\3. Design\\2. Gas\\1. Drawings")
        if tab_number == 3:
            # Window 3: Gas Design folder
            if project_folder_format(project_code):
                pygui.write("\\3. Design\\2. Gas\\2. Gas Design")
            else:
                pygui.write("\\5, Design\\Gas Design")
            # for new projects: pygui.write("\\3. Design\\2. Gas\\2. Gas Design")
        if tab_number == 4:
            pygui.hotkey("ctrl","a")
            pygui.write("C:\\Users\\Fawwaz.Azwar\\OneDrive - Last Mile\\Documents - OneDrive\\.GASWorkS")
        pygui.press("enter")
        pygui.press("esc")
        time.sleep(1.5)
        tab_number += 1

def open_project(project_number):
    # opens the project folders on first set (Project 1) or second set (Project 2) of 3 windows
    project_path = root.clipboard_get()
    project_name = project_path.split("\\")
    if project_name[2] == "Live Projects":
        project_code = project_name[3].split()[0]
    elif project_name[2] == "EDB Projects":
        project_code = project_name[4].split()[0]
    if project_number == 1:
        project_1.set("Project 1: " + project_code)
    elif project_number == 2:
        project_2.set("Project 2: " + project_code)
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        if project_number == 1:
            pygui.write("2")
        elif project_number == 2:
            pygui.write("22222")
        if window_number > 1:
            pygui.write("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        pygui.hotkey("ctrl","l")
        pygui.hotkey("ctrl","v")
        if window_number == 2: # Window 2: Drawings folder
            if project_folder_format(project_code):
                pygui.write("\\3. Design\\2. Gas\\1. Drawings")
            else:
                pygui.write("\\5, Design\\Drawings")
            # for new projects: pygui.write("\\3. Design\\2. Gas\\1. Drawings")
        if window_number == 3:
            # Window 3: Gas Design folder
            if project_folder_format(project_code):
                pygui.write("\\3. Design\\2. Gas\\2. Gas Design")
            else:
                pygui.write("\\5, Design\\Gas Design")
            # for new projects: pygui.write("\\3. Design\\2. Gas\\2. Gas Design")
        pygui.press("enter")
        window_number += 1

def show_project(project_number):
    # shows the project folders on first set (Project 1) or second set (Project 2) of 3 windows 
    # assigned to the "Show" button
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        if project_number == 1:
            pygui.write("2")
        elif project_number == 2:
            pygui.write("22222")
        if window_number > 1:
            pygui.write("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        window_number += 1

def open_merge_auto():
    # opens Merge Automator window (n/a)
    ma_window = ctk.CTkToplevel()
    ma_window.geometry("560x170")
    ma_window.title("Merge Automator")
    ma_window.resizable(width=False,height=False)

def open_help():
    # opens Help window
    help_window = ctk.CTkToplevel()
    help_window.geometry("500x250")
    help_window.title("Help Guide")
    help_window.resizable(width=False,height=False)

def note_fe_windows():
    # opens warning dialog for before open_fe_windows()
    main_x = root.winfo_x()
    main_y = root.winfo_y()
    fe_note_window = ctk.CTkToplevel()
    fe_note_window.geometry(f"+{main_x+80}+{main_y+40}")
    fe_note_window.title("Create File Explorer Windows...")
    fe_note_window.resizable(width=False,height=False)
    note_fe_text = "Are you sure you want to create (8) new File Explorer windows?"
    note_fe_label = ctk.CTkLabel(fe_note_window, text=note_fe_text)
    note_fe_label.grid(row=0,column=0,padx=(20,20),pady=(10,0))

    def open_fe_windows():
        # opens 8x File Explorer windows
        for i in range(8):
            subprocess.Popen(r'explorer ')
        fe_note_window.destroy()

    note_fe_button = ctk.CTkButton(fe_note_window, text="Confirm", command=open_fe_windows)
    note_fe_button.grid(row=1,column=0,padx=(0,0),pady=(10,20))
    fe_note_window.grab_set()
    fe_note_window.focus()

def green():
    # loops cursor movement and click on top left corner of screen
    # assigned to the "Green" button
    while True:
        pygui.moveTo(5,5,duration=0)
        pygui.moveTo(10,10,duration=1)
        pygui.click()

## Widgets ##

## Main Window
# row 0
code_label = ctk.CTkLabel(root, text="Project Code")
code_entry = ctk.CTkEntry(root, textvariable=code_var)
code_entry.insert(0,"UKP")
drawing_checkbox = ctk.CTkCheckBox(root, text = "Noded Drawing (Saved View)",
                                   variable=drawing_var, onvalue=1, offvalue=0)
# row 1
rev_label = ctk.CTkLabel(root, text="Revision Number             ")
rev_entry = ctk.CTkEntry(root, textvariable=rev_var)
rev_entry.insert(0,"0")
new_checkbox = ctk.CTkCheckBox(root, text = "New Folder Format",
                                   variable=new_project, onvalue=1, offvalue=0)
# row 2
run_button = ctk.CTkButton(root, text="Publish", command=publish, fg_color="#d31f2a", hover_color="#84100b")
outputs_button = ctk.CTkButton(root, text="Outputs", command=open_outputs,width=80)
#help_button = ctk.CTkButton(root, text="Help", command=open_help,width=80)
project_folder_button = ctk.CTkButton(root, text="Project Folder", command=project_tabs,width=80)
# row 3 (wip)
merge_button = ctk.CTkButton(root, text="Merge Automator", command=open_merge_auto) 
# row 4
project_label_1 = ctk.CTkLabel(root, textvariable=project_1)
project_button_1 = ctk.CTkButton(root, text="Open", command= lambda: open_project(1),width=60)
project_button_show_1 = ctk.CTkButton(root, text="Show", command= lambda: show_project(1),width=60)
tools_label = ctk.CTkLabel(root, text="  Useful Tools:")
green_button = ctk.CTkButton(root, text="Green", command=green,width=80, fg_color="#1c9b18", hover_color="#186f17")
# row 5
project_label_2 = ctk.CTkLabel(root, textvariable=project_2)
project_button_2 = ctk.CTkButton(root, text="Open", command= lambda: open_project(2),width=60)
project_button_show_2 = ctk.CTkButton(root, text="Show", command= lambda: show_project(2),width=60)
fe_windows_button = ctk.CTkButton(root, text="FE (8x)", command=note_fe_windows,width=80)

## Grid Placements ##

## Main Window
# row 0
code_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky='sw')
code_entry.grid(row=0,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
drawing_checkbox.grid(row=0,column=3,columnspan=2,padx=(0,0),pady=(10,0),sticky='sw')
# row 1
rev_label.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky='sw')
rev_entry.grid(row=1,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
new_checkbox.grid(row=1,column=3,columnspan=2,padx=(0,0),pady=(10,0),sticky='sw')
# row 2
run_button.grid(row=2,column=1,columnspan=2,padx=(20,20),pady=(10,0),sticky='sw')
outputs_button.grid(row=2,column=3,padx=(0,0),pady=(10,0),sticky='sw')
project_folder_button.grid(row=2,column=4,padx=(0,0),pady=(10,0),sticky='sw')
# row 3 (wip)
#merge_button.grid(row=3,column=0,padx=(10,0),pady=(10,0),sticky='sw')
# row 4
project_label_1.grid(row=4,column=0,padx=(10,0),pady=(10,0),sticky='sw')
project_button_1.grid(row=4,column=1,padx=(20,0),pady=(10,0),sticky='sw')
project_button_show_1.grid(row=4,column=2,padx=(0,0),pady=(10,0),sticky='sw')
tools_label.grid(row=4,column=3,rowspan=2,padx=(0,0),pady=(10,0),sticky='w')
green_button.grid(row=4,column=4,padx=(0,0),pady=(10,0),sticky='sw')
# row 5
project_label_2.grid(row=5,column=0,padx=(10,0),pady=(10,0),sticky='sw')
project_button_2.grid(row=5,column=1,padx=(20,0),pady=(10,0),sticky='sw')
project_button_show_2.grid(row=5,column=2,padx=(0,0),pady=(10,0),sticky='sw')
fe_windows_button.grid(row=5,column=4,padx=(0,0),pady=(10,0),sticky='sw')

root.eval('tk::PlaceWindow . center')

root.mainloop()