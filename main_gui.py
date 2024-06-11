# Python modules
import time
import subprocess
import tkinter as tk
import os

# Extra modules
import pyautogui as pygui
import customtkinter as ctk

## Main Window ##
root = ctk.CTk()
root.geometry("560x200")
root.title("GASWorkS Automator & Folder Macros")
root.resizable(width=False,height=False)

## Main Variables ##
screensize = pygui.size()
screen_cx = screensize[0]/2
screen_cy = screensize[1]/2
code = ""
rev = ""
draw_report = ""
code_var = ctk.StringVar()  # project code
rev_var = ctk.StringVar()   # GASWorkS file revision
replace_var = ctk.IntVar()  # overwrite existing documents if == 1
drawing_var = ctk.IntVar()  # prints noded drawing if == 1
big_project = ctk.IntVar()  
project_1 = ctk.StringVar()
project_1.set("Project 1: ")    
project_2 = ctk.StringVar()
project_2.set("Project 2: ")

dirname = os.path.abspath(os.path.dirname(__file__))
outputs_folder = dirname + "\\Outputs"
images_folder = dirname + "\\images"
types = ["Pipe", "Node", "Customer"]

def publish():
    # base function for publishing reports
    global code
    global rev
    global draw_report
    code = code_var.get()
    rev = "Rev" + rev_var.get()
    draw_report = drawing_var.get()
    if big_project.get() == 1:
        locate_click(images_folder + "\\GW_zoomtofit.png")
        for i in range(3):
            locate_click(images_folder + "\\GW_zoomout.png")
            time.sleep(0.5)
    full(False,draw_report)

def open_outputs():
    # opens the .Outputs folder
    # assigned to the "Open Outputs" button
    subprocess.Popen(r'explorer ' + outputs_folder)

def open_project_1():
    # opens the project folders on first set of 3 windows
    code = code_var.get()
    project_path = root.clipboard_get()
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        pygui.write("2")
        if window_number > 1:
            pygui.write("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        pygui.hotkey("ctrl","l")
        pygui.hotkey("ctrl","v")
        if window_number == 2:
            # Window 2: Drawings folder
            pygui.write("\\5, Design\\Drawings")
        if window_number == 3:
            # Window 3: Gas Design folder
            pygui.write("\\5, Design\\Gas Design")
        pygui.press("enter")
        window_number += 1
    if project_path[26:29] == "UKP":
        project_name = project_path[26:]
        project_code = ""
        for i in project_name:
            project_code += i
            if i == " ":
                break
        project_1.set("Project 1: " + project_code)
    elif project_path[12:15] == "EDB":
        project_name = project_path[25:]
        project_code = ""
        count = 0
        for i in project_name:
            count += 1
            if i == "\\":
                project_name = project_name[count:]
                for x in project_name:
                    project_code += x
                    if x == " ":
                        break
        project_1.set("Project 1: " + project_code)

def show_project_1():
    # shows the project folders on first set of 3 windows
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        pygui.write("2")
        if window_number > 1:
            pygui.write("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        window_number += 1

def open_project_2():
    # opens the project folders on second set of 3 windows
    code = code_var.get()
    project_path = root.clipboard_get()
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        pygui.write("22222")
        if window_number > 1:
            pygui.write("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        pygui.hotkey("ctrl","l")
        pygui.hotkey("ctrl","v")
        if window_number == 2:
            # Window 2: Drawings folder
            pygui.write("\\5, Design\\Drawings")
        if window_number == 3:
            # Window 3: Gas Design folder
            pygui.write("\\5, Design\\Gas Design")
        pygui.press("enter")
        window_number += 1
    if project_path[26:29] == "UKP":
        project_name = project_path[26:]
        project_code = ""
        for i in project_name:
            project_code += i
            if i == " ":
                break
        project_2.set("Project 2: " + project_code)
    elif project_path[12:15] == "EDB":
        project_name = project_path[25:]
        project_code = ""
        count = 0
        for i in project_name:
            count += 1
            if i == "\\":
                project_name = project_name[count:]
                for x in project_name:
                    project_code += x
                    if x == " ":
                        break
        project_2.set("Project 2: " + project_code)

def show_project_2():
    # shows the project folders on second set of 3 windows
    window_number = 1 # Window 1: main project folder
    while window_number < 4:
        pygui.keyDown("win")
        pygui.write("22222")
        if window_number > 1:
            pygui.write("2") # previously written as pygui.press("2")
        if window_number > 2:
            pygui.write("2")
        pygui.keyUp("win")
        window_number += 1

def open_merge_auto():
    # opens Merge Automator window
    ma_window = ctk.CTkToplevel()
    ma_window.geometry("560x170")
    ma_window.title("Merge Automator")
    ma_window.resizable(width=False,height=False)

def green():
    # loops cursor movement and click on top left corner of screen
    while True:
        pygui.moveTo(5,5,duration=0)
        pygui.moveTo(10,10,duration=1)
        pygui.click()

## Widgets ##

# row 0
code_label = ctk.CTkLabel(root, text="Project Code")
code_entry = ctk.CTkEntry(root, textvariable=code_var)
code_entry.insert(0,"UKP")
drawing_checkbox = ctk.CTkCheckBox(root, text = "Noded Drawing (Saved View)",
                                   variable=drawing_var, onvalue=1, offvalue=0)
# row 1
rev_label = ctk.CTkLabel(root, text="Revision Number")
rev_entry = ctk.CTkEntry(root, textvariable=rev_var)
rev_entry.insert(0,"0")
big_checkbox = ctk.CTkCheckBox(root, text = "Big Project (>500 nodes)",
                                   variable=big_project, onvalue=1, offvalue=0)
# row 2
outputs_button = ctk.CTkButton(root, text="Open Outputs", command=open_outputs)
run_button = ctk.CTkButton(root, text="Publish", command=publish)
green_button = ctk.CTkButton(root, text="Green", command=green)
# row 3
merge_button = ctk.CTkButton(root, text="Merge Automator", command=open_merge_auto)
# row 4
project_label_1 = ctk.CTkLabel(root, textvariable=project_1)
project_button_1 = ctk.CTkButton(root, text="Open", command=open_project_1,width=60)
project_button_show_1 = ctk.CTkButton(root, text="Show", command=show_project_1,width=60)
# row 5
project_label_2 = ctk.CTkLabel(root, textvariable=project_2)
project_button_2 = ctk.CTkButton(root, text="Open", command=open_project_2,width=60)
project_button_show_2 = ctk.CTkButton(root, text="Show", command=show_project_2,width=60)

# Grid Placements
# row 0
code_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky='sw')
code_entry.grid(row=0,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
drawing_checkbox.grid(row=0,column=3,padx=(0,0),pady=(10,0),sticky='sw')
# row 1
rev_label.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky='sw')
rev_entry.grid(row=1,column=1,columnspan=2,padx=(20,0),pady=(10,0),sticky='sw')
big_checkbox.grid(row=1,column=3,padx=(0,0),pady=(10,0),sticky='sw')
# row 2
outputs_button.grid(row=2,column=0,padx=(10,0),pady=(10,0),sticky='sw')
run_button.grid(row=2,column=1,columnspan=2,padx=(20,20),pady=(10,0),sticky='sw')
green_button.grid(row=2,column=3,padx=(0,0),pady=(10,0),sticky='sw')
# row 3 (wip)
#merge_button.grid(row=3,column=0,padx=(10,0),pady=(10,0),sticky='sw')
# row 4
project_label_1.grid(row=4,column=0,padx=(10,0),pady=(10,0),sticky='sw')
project_button_1.grid(row=4,column=1,padx=(20,0),pady=(10,0),sticky='sw')
project_button_show_1.grid(row=4,column=2,padx=(0,0),pady=(10,0),sticky='sw')
# row 5
project_label_2.grid(row=5,column=0,padx=(10,0),pady=(10,0),sticky='sw')
project_button_2.grid(row=5,column=1,padx=(20,0),pady=(10,0),sticky='sw')
project_button_show_2.grid(row=5,column=2,padx=(0,0),pady=(10,0),sticky='sw')

## Functions ##

# Background Tracing Based on CAD (legacy)
    # was placed here, RIP

def progress(dur):
    # moves cursor from left to right end of screen to show wait time (legacy)
    pygui.moveTo(0,45,duration=0)
    pygui.moveTo(1915,45,duration=dur)

def capture_change(x,y):
    # checks if the cololur of a pixel at x,y has changed, then returns
    check = True
    while check:
        im1 = pygui.screenshot()
        im1_pixel = im1.getpixel((x,y))
        time.sleep(1)
        im2 = pygui.screenshot()
        im2_pixel = im2.getpixel((x,y))
        if not(im1_pixel == im2_pixel):
            check = False
    return

def locate_click(image):
    ## locate and click based on given image, in while loop
    check = True
    while check:
        print_location = pygui.locateCenterOnScreen(image) # delay 1-2 sec
        if not(print_location == None):
            check = False
    pygui.click(print_location[0],print_location[1])

def data_report(ver,replace):
    ## prints pipe/node/customer data report
    pygui.moveTo(154,50,duration=0.2)   # to GW window
    pygui.click()
    pygui.hotkey("alt","r")             # Report tab
    pygui.press(types[ver][0])
    time.sleep(0.2)
    locate_click(images_folder + "\\GW_print_button.png")
    check = True
    while check:
        im = pygui.screenshot()
        im_pixel = im.getpixel((screen_cx,screen_cy))
        if im_pixel == (240, 240, 240):
            check = False
    time.sleep(0.2)
    pygui.hotkey("alt","p") # prints report
    capture_change(screen_cx,screen_cy)
    pygui.typewrite(outputs_folder + "\\" + code + " - " + rev + " - " + types[ver] + " Data Report.pdf") # inputs name for report
    pygui.hotkey("alt","s") # saves report
    if replace == True:
        pygui.press("y")
    time.sleep(0.5)
    pygui.press("y")
    capture_change(screen_cx,screen_cy) # checks centre pixel change
    pygui.hotkey("alt","c") # closes report window

def summary(replace):
    ## prints system summary report
    pygui.moveTo(154,50,duration=0.2)   # to GW window
    pygui.click()
    pygui.hotkey("alt","r")             # Report tab
    pygui.press("m")
    pygui.hotkey("alt","c")
    time.sleep(0.2)
    locate_click(images_folder + "\\GW_print_button_2.png")
    capture_change(screen_cx,screen_cy)
    pygui.hotkey("alt","p") # prints report
    capture_change(screen_cx,screen_cy)
    pygui.typewrite(outputs_folder + "\\" + code + " - " + rev + " - System Summary Report.pdf")
    pygui.hotkey("alt","s") # saves report
    if replace == True:
        pygui.press("tab")
        pygui.press("enter")
    time.sleep(1)             # waiting time for PDF to be fully published
    pygui.hotkey("alt","c") # closes report window

def drawing(replace):
    ## prints noded drawing
    locate_click(images_folder + "\\GW_button_side.png")
    locate_click(images_folder + "\\GW_print_button.png")
    pygui.press("enter")
    time.sleep(0.5)
    # note: saved view/window should be preselected at this stage
    pygui.hotkey("alt","t") # navigates to Style pane
    pygui.hotkey("alt","p") # plots drawing
    capture_change(screen_cx,screen_cy)
    # note: title block values should be filled in at this stage
    pygui.hotkey("alt","c") # presses first "Continue"
    time.sleep(0.3)
    capture_change(screen_cx,screen_cy)
    #progress(2)
    pygui.hotkey("alt","c") # presses second "Continue"
    pygui.typewrite(outputs_folder + "\\" + code + " - " + rev + " - Noded Drawing.pdf")
    pygui.hotkey("alt","s") # saves report
    if replace == True:
        pygui.press("tab")
        pygui.press("enter")

def full(replace,draw):
    for i in range(3):
        data_report(i,replace)
        time.sleep(0.2)
    summary(replace)
    time.sleep(0.2)
    if draw == 1:
        drawing(replace)

root.mainloop()
