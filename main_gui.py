version = "v0.1.13"
# Python modules
import time
import subprocess
import os
import tkinter as tk

# Extra modules
import pyautogui as pygui
import customtkinter as ctk

# Dependent files
import report_functions as rf

## Main Window ##
root = ctk.CTk()
root.geometry("575x160")
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

def existing_files_check():
    # Checks if the Outputs folder already has report files with the same name
    # Returns True if files exist, False if not
    global code
    global rev
    existing_files = os.listdir(rf.outputs_folder)
    for file in existing_files:
        if file == code + " - " + rev + " - Pipe Data Report.pdf" or \
           file == code + " - " + rev + " - Node Data Report.pdf" or \
           file == code + " - " + rev + " - Customer Data Report.pdf" or \
           file == code + " - " + rev + " - Summary Report.pdf" or \
           (drawing_var.get() == 1 and file == code + " - " + rev + " - Noded Drawing.pdf"):
            return True
    return False

def publish():
    # Main function for publishing reports
    # Assigned to the "Publish" button
    global code
    global rev
    global draw_report
    code = code_var.get()
    if len(code.split("-")) > 1:
        # If project code has a variation number, split it
        code = code.split("-")[0]
    elif code[0:3] == "PAR" and len(code.split("-")) > 1:
        # If project code starts with "PAR", split it to get the project code
        code = code.split("-")[1]
    rev = rev_var.get()
    draw_report = drawing_var.get()
    if existing_files_check() == True:
        # If files with the report files already exist, change replace variable to True
        tk.messagebox.showwarning(title="Existing Reports Found", message="Existing reports for " + code + " - " + rev + " found in Outputs folder.\nPress OK to overwrite existing reports...")
        replace_files = True
    else:
        # If no existing files found, change replace variable to False
        replace_files = False
    tk.messagebox.showinfo(title="Publishing Reports...", message="Ensure that GASWorkS is open on the Main Display!\nPress OK to continue publishing reports for " + code + "...")
    full(replace_files,draw_report)

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
    global edb_projects_dir
    global local_gw_dir
    live_projects_dir = os.listdir("S:\\Projects\\Live Projects")
    edb_projects_dir = os.listdir("S:\\Projects\\EDB Projects")
    local_gw_dir = os.listdir("C:\\Users\\Fawwaz.Azwar.UPSL\\OneDrive - Last Mile\\Documents - OneDrive\\- GASWorkS")
    if len(live_projects_dir) > 0:
        read_dir_button.configure(text="Refresh")
        project_tabs_button.configure(command=project_tabs, state="normal", fg_color="#1f6aa5", hover_color="#144870")

def project_folder_paths(project_code):
    # Function that returns the 3 project folder paths based on project code
    # Called in project_tabs()
    if project_code[0:3] == "UKP":
        # If project code starts with "UKP", set path to Live Projects
        # UKP project code should be in the format "UKPxxxx-Vxx"
        if len(project_code.split("-")) > 1:
            variation_no = project_code.split("-")[1]
            project_code = project_code.split("-")[0]
        for i in live_projects_dir:
            if i.split( )[0] == project_code and len(i.split(".")) < 2:
                path_project = "S:\\Projects\\Live Projects\\" + i
                project_dir = os.listdir(path_project)
                break
        if not ("path_project" in locals()):
            # If project code does not match any folder in Live Projects, show error message
            tk.messagebox.showerror(title="Error", message="Project does not exist. Please enter a valid UKP project code.")
            return None, None, None, None
    elif project_code[0:3] == "PAR" and project_code.split("-")[1][0] == "E":
        # If project code contains a "PAR" number and an "E" project code, set path accordingly
        # EDB project code should be in the format "PARxxxx-Exxxx-Vxx"
        if len(project_code.split("-")) > 2:
            variation_no = project_code.split("-")[2]
        parent_code = project_code.split("-")[0]
        project_code = project_code.split("-")[1]
        for i in edb_projects_dir:
            if i.split( )[0] == parent_code and len(i.split(".")) < 2:
                parent_dir = os.listdir("S:\\Projects\\EDB Projects\\" + i)
                for j in parent_dir:
                    if j.split( )[0] == project_code and len(j.split(".")) < 2:
                        path_project = "S:\\Projects\\EDB Projects\\" + i + "\\" + j
                        project_dir = os.listdir(path_project)
                        if "5, Design" in project_dir or "6, Drawings" in project_dir or "3. Design" in project_dir:
                            break
    else:
        # If project code does not start with "UKP" or "PAR" followed by "E" project code, show error message
        tk.messagebox.showerror(title="Error", message="Invalid Project Code. Please enter a valid UKP or EDB (PARxxxx-Exxxx) project code.")
        return None, None, None, None
    for i in local_gw_dir:
            if i.split( )[0] == project_code and len(i.split(".")) < 2:
                path_gw = "C:\\Users\\Fawwaz.Azwar.UPSL\\OneDrive - Last Mile\\Documents - OneDrive\\- GASWorkS\\" + i
                print(path_gw)
                break
            else:
                path_gw = None
    if "5, Design" in project_dir:
        # If project directory contains "5, Design", set paths accordingly
        path_drawings = path_project + "\\5, Design\\Drawings"
        path_packs = path_project + "\\5, Design\\Gas Design"
    if "6, Drawings" in project_dir:
        # If project directory contains "6, Drawings", set paths accordingly
        path_drawings = path_project + "\\6, Drawings"
    if "3. Design" in project_dir:
        # If project directory contains "3. Design", set paths accordingly
        path_drawings = path_project + "\\3. Design\\2. Gas\\1. Drawings"
        path_packs = path_project + "\\3. Design\\2. Gas\\2. Gas Design"
    if "variation_no" in locals():
        # If variation number exists, check for the specific Variation Pack in the Gas Design folder
        path_packs_og = path_packs
        gas_design_folder = os.listdir(path_packs)
        for j in gas_design_folder:
            if j.split(" ")[0] == variation_no:
                path_packs = path_packs + "\\" + j
        if path_packs == path_packs_og:
            # If variation pack does not exist, show warning message
            tk.messagebox.showwarning(title="Variation Not Found", message=variation_no + " Pack not found. Opening Gas Design folder instead...")
    return path_project, path_drawings, path_packs, path_gw

def project_tabs():
    # Function to open a project folder, the drawings folder, and the gas design folder in tabs within one File Explorer window
    # Assigned to the "Open Project in Tabs" button
    code = code_var.get()
    path_project, path_drawings, path_packs, path_gw = project_folder_paths(code)
    print(path_gw)
    if None in (path_project, path_drawings, path_packs):
        # If project folder paths are not valid, return
        return
    subprocess.Popen(r'explorer ')
    time.sleep(2)
    if path_gw == None:
        number_of_tabs = 2
        path_list = [path_project, path_drawings, path_packs]
    else:
        number_of_tabs = 3
        path_list = [path_project, path_drawings, path_packs, path_gw]
    for i in range(number_of_tabs):
        pygui.hotkey("ctrl","t") # opens new tab
        time.sleep(0.5)
    time.sleep(1.5)
    tab_number = 1
    for i in path_list:
        pygui.hotkey("ctrl",str(tab_number))
        pygui.hotkey("ctrl","l")
        pygui.write(i)
        pygui.press("enter")
        pygui.press("esc")
        time.sleep(1.5)
        tab_number += 1

def project_gw_folder():
    # Opens the local GASWorkS folder for the project
    # Assigned to the "Open Project GW Folder" button
    code = code_var.get()
    gw_folder_path = "C:\\Users\\Fawwaz.Azwar.UPSL\\OneDrive - Last Mile\\Documents - OneDrive\\- GASWorkS"
    if len(code.split("-")) > 1:
        # If project code has a variation number, split it
        code = code.split("-")[0]
    elif code[0:3] == "PAR" and len(code.split("-")) > 1:
        # If project code starts with "PAR", split it to get the project code
        code = code.split("-")[1]
    for i in os.listdir(gw_folder_path):
        if i.split( )[0] == code and len(i.split(".")) < 2:
            # If project code matches a folder in the local GASWorkS folder, open it
            gw_folder = gw_folder_path + "\\" + i + "\\"
            print(gw_folder)
            subprocess.Popen(r'explorer ' + gw_folder)
            time.sleep(2)
            return
    # If project code does not match any folder in the local GASWorkS folder, show error message
    tk.messagebox.showerror(title="Error", message="Project does not exist in local GASWorkS folder. Please enter a valid project code.")

def settings_window():
    # Opens Settings window
    settings_window = ctk.CTkToplevel()
    settings_window.geometry("500x250")
    settings_window.title("Settings")
    settings_window.resizable(width=False,height=False)

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
project_tabs_button.grid(row=0,column=3,columnspan=2,padx=(0,10),pady=(10,0),sticky='w')
read_dir_button = ctk.CTkButton(root, text="Refresh", width=80, command=read_project_dir)
read_dir_button.grid(row=0,column=5,padx=(0,0),pady=(10,0),sticky='w')
# row 1
rev_label = ctk.CTkLabel(root, text="Revision Number   ")
rev_label.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky='sw')
rev_entry = ctk.CTkEntry(root, textvariable=rev_var)
rev_entry.insert(0,"Rev0")
rev_entry.grid(row=1,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
gw_folder_button = ctk.CTkButton(root, text="Open Project GW Folder", width=170, command=project_gw_folder)
gw_folder_button.grid(row=1,column=3,columnspan=2,padx=(0,10),pady=(10,0),sticky='w')
outputs_button = ctk.CTkButton(root, text="Outputs", command=open_outputs, width=80)
outputs_button.grid(row=1,column=5,padx=(0,0),pady=(10,0),sticky='sw')
# row 2
run_button = ctk.CTkButton(root, text="Publish", command=publish, fg_color="#d31f2a", hover_color="#84100b")
run_button.grid(row=2,column=1,columnspan=2,padx=(20,20),pady=(10,0),sticky='sw')
settings_button = ctk.CTkButton(root, text="Settings", width=80, command=settings_window)
settings_button.grid(row=2,column=3,padx=(0,5),pady=(10,0),sticky='sw')
help_button = ctk.CTkButton(root, text="Help", command=open_help, width=80)
help_button.grid(row=2,column=4,padx=(5,10),pady=(10,0),sticky='sw')
green_button = ctk.CTkButton(root, text="Green", command=green, width=80, fg_color="#1c9b18", hover_color="#186f17")
green_button.grid(row=2,column=5,padx=(0,0),pady=(10,0),sticky='sw')
# # row 3
options_label = ctk.CTkLabel(root, text="Publish Options:")
options_label.grid(row=3,column=0,padx=(10,0),pady=(10,0),sticky='sw')
drawing_checkbox = ctk.CTkCheckBox(root, text = "Noded Drawing",
                                   variable=drawing_var, onvalue=1, offvalue=0)
drawing_checkbox.grid(row=3,column=1,padx=(20,0),pady=(10,0),sticky='w')

root.eval('tk::PlaceWindow . center')

root.mainloop()