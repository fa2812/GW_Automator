version = "v0.1.5"
# Python modules
import time
import subprocess
import os

# Extra modules
import pyautogui as pygui
import customtkinter as ctk

# Dependent files
import report_functions as rf

## Main Window ##
root = ctk.CTk()
root.geometry("540x170")
root.title("GASWorkS Automator & Folder Macros (" + version + ")")
root.resizable(width=False,height=False)

## Main Variables ##
code = ""
rev = ""
draw_report = ""
code_var = ctk.StringVar()  # project code
rev_var = ctk.StringVar()   # GASWorkS file revision
replace_var = ctk.IntVar()  # overwrite existing documents if == 1
drawing_var = ctk.IntVar()  # prints noded drawing if == 1 
project_1 = ctk.StringVar()
project_1.set("Project 1: ")
project_2 = ctk.StringVar()
project_2.set("Project 2: ")
live_projects_dir = []
edb_projects_dir = []

def publish():
    # Main function for publishing reports
    # Assigned to the "Publish" button
    global code
    global rev
    global draw_report
    code = code_var.get()
    rev = rev_var.get()
    draw_report = drawing_var.get()
    full(False,draw_report)

def full(replace,draw):
    # Function that calls report functions to publish all reports
    # Called in publish()
    for i in range(3):
        rf.data_report(i,replace,code,rev)
        time.sleep(0.2)
    rf.summary(replace,code,rev)
    time.sleep(0.2)
    if draw == 1:
        rf.drawing(replace,code,rev)

def open_outputs():
    # Opens the Outputs folder
    # Assigned to the "Open Outputs" button
    subprocess.Popen(r'explorer ' + rf.outputs_folder)

def read_project_dir():
    # Reads the Live Project directory in the S: drive
    # Assigned to the "Read Project Directories" button
    global live_projects_dir
    live_projects_dir = os.listdir("S:\\Projects\\Live Projects")
    #edb_projects_dir = os.listdir("S:\\Projects\\EDB Project")
    if len(live_projects_dir) > 0:
        read_dir_button.configure(text="Refresh Project Directory")
        project_tabs_button.configure(command=project_tabs, state="normal", fg_color="#1f6aa5", hover_color="#144870")

def project_folder_paths(project_code):
    # Function that returns the 3 project folder paths based on project code
    # Called in project_tabs()
    if project_code[0:3] == "UKP":
        for i in live_projects_dir:
            if i.split( )[0] == project_code and len(i.split(".")) < 2:
                path_project = "S:\\Projects\\Live Projects\\" + i
    project_dir = os.listdir(path_project)
    for i in project_dir:
        if i == "5, Design":
            path_drawings = path_project + "\\5, Design\\Drawings"
            path_packs = path_project + "\\5, Design\\Gas Design"
        if i == "6, Drawings":
            path_drawings = path_project + "\\6, Drawings"
        if i == "3. Design":
            path_drawings = path_project + "\\3. Design\\2. Gas\\1. Drawings"
            path_packs = path_project + "\\3. Design\\2. Gas\\2. Gas Design"
    return path_project, path_drawings, path_packs

def project_tabs():
    # Function to open a project folder, the drawings folder, and the gas design folder in tabs within one File Explorer window
    # Assigned to the "Open Project in Tabs" button
    code = code_var.get()
    path_project, path_drawings, path_packs = project_folder_paths(code)
    subprocess.Popen(r'explorer ')
    time.sleep(2)
    for i in range(2):
        pygui.hotkey("ctrl","t")
        time.sleep(0.5)
    time.sleep(0.5)
    tab_number = 1
    for i in [path_project, path_drawings, path_packs]:
        pygui.hotkey("ctrl",str(tab_number))
        pygui.hotkey("ctrl","l")
        pygui.write(i)
        pygui.press("enter")
        pygui.press("esc")
        time.sleep(1.5)
        tab_number += 1

def open_merge_auto():
    # Opens Merge Automator window (n/a)
    ma_window = ctk.CTkToplevel()
    ma_window.geometry("560x170")
    ma_window.title("Merge Automator")
    ma_window.resizable(width=False,height=False)

def open_help():
    # Opens Help window (n/a)
    help_window = ctk.CTkToplevel()
    help_window.geometry("500x250")
    help_window.title("Help Guide")
    help_window.resizable(width=False,height=False)

def green():
    # Loops cursor movement and click on top left corner of screen
    # Assigned to the "Green" button
    while True:
        pygui.moveTo(5,5,duration=0)
        pygui.moveTo(10,10,duration=1)
        pygui.click()

## Widgets & Grid Placements ##

## Main Window
# row 0
code_label = ctk.CTkLabel(root, text="Project Code")
code_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky='sw')
code_entry = ctk.CTkEntry(root, textvariable=code_var)
code_entry.insert(0,"UKP")
code_entry.grid(row=0,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
project_tabs_button = ctk.CTkButton(root, text="Open Project in Tabs", width=170, fg_color="#949a9f", state="disable")
project_tabs_button.grid(row=0,column=3,columnspan=2,padx=(0,0),pady=(10,0),sticky='w')
# row 1
rev_label = ctk.CTkLabel(root, text="Revision Number     ")
rev_label.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky='sw')
rev_entry = ctk.CTkEntry(root, textvariable=rev_var)
rev_entry.insert(0,"Rev0")
rev_entry.grid(row=1,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
read_dir_button = ctk.CTkButton(root, text="Read Project Directory", width=170, command=read_project_dir)
read_dir_button.grid(row=1,column=3,columnspan=2,padx=(0,0),pady=(10,0),sticky='w')
# row 2
options_label = ctk.CTkLabel(root, text="Publish Options:")
options_label.grid(row=2,column=0,padx=(10,0),pady=(10,0),sticky='sw')
run_button = ctk.CTkButton(root, text="Publish", command=publish, fg_color="#d31f2a", hover_color="#84100b")
run_button.grid(row=2,column=1,columnspan=2,padx=(20,20),pady=(10,0),sticky='sw')
outputs_button = ctk.CTkButton(root, text="Outputs", command=open_outputs, width=80)
outputs_button.grid(row=2,column=3,padx=(0,5),pady=(10,0),sticky='sw')
green_button = ctk.CTkButton(root, text="Green", command=green, width=80, fg_color="#1c9b18", hover_color="#186f17")
green_button.grid(row=2,column=4,padx=(5,0),pady=(10,0),sticky='sw')
#help_button = ctk.CTkButton(root, text="Help", command=open_help,width=80)
#merge_button.grid(row=3,column=0,padx=(10,0),pady=(10,0),sticky='sw')
# row 3 (wip)
merge_button = ctk.CTkButton(root, text="Merge Automator", command=open_merge_auto) 
# row 4
drawing_checkbox = ctk.CTkCheckBox(root, text = "Noded Drawing",
                                   variable=drawing_var, onvalue=1, offvalue=0)
drawing_checkbox.grid(row=4,column=0,padx=(10,0),pady=(10,0),sticky='w')

root.eval('tk::PlaceWindow . center')

root.mainloop()