# Python modules
import time
import os

# Extra modules
import pyautogui as pygui

## Main Variables ##
screensize = pygui.size()
screen_cx = screensize[0]/2
screen_cy = screensize[1]/2

dirname = os.path.abspath(os.path.dirname(__file__))
outputs_folder = dirname + "\\Outputs"
images_folder = dirname + "\\images"
types = ["Pipe", "Node", "Customer"]

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

def data_report(ver,replace,code,rev):
    ## prints pipe/node/customer data report
    pygui.moveTo(154,50,duration=0.2)   # to GW window
    pygui.click()
    pygui.hotkey("alt","r")             # Report tab
    pygui.press(types[ver][0])
    time.sleep(0.75)    # wait time for report window to come up
    if ver == 2:
        time.sleep(0.8) # extra wait time for Customer report (for large projects)
    locate_click(images_folder + "\\GW_print_button.png")
    check = True
    while check:
        im = pygui.screenshot()
        im_pixel = im.getpixel((screen_cx,screen_cy))
        time.sleep(0.2)
        if im_pixel == (240, 240, 240):
            check = False
    time.sleep(0.2)
    pygui.hotkey("alt","p") # prints report
    time.sleep(0.75)    # wait time for file explorer window to come up
    capture_change(screen_cx,screen_cy)
    pygui.write(outputs_folder + "\\" + code + " - " + rev + " - " + types[ver] + " Data Report.pdf") # inputs name for report
    pygui.hotkey("alt","s") # saves report
    if replace == True:
        pygui.press("y")
    time.sleep(1.5)     # wait time for file explorer window to close
    pygui.press("y")    # redundancy for "Replace file" selection
    capture_change(screen_cx,screen_cy) # checks centre pixel change
    pygui.hotkey("alt","c") # closes report window

def summary(replace,code,rev):
    ## prints system summary report
    pygui.moveTo(154,50,duration=0.2)   # to GW window
    pygui.click()
    pygui.hotkey("alt","r")             # Report tab
    pygui.press("m")
    pygui.hotkey("alt","c")
    time.sleep(0.2)
    locate_click(images_folder + "\\GW_print_button_2.png")
    capture_change(screen_cx,screen_cy)
    pygui.hotkey("alt","p")     # prints report
    capture_change(screen_cx,screen_cy)
    pygui.write(outputs_folder + "\\" + code + " - " + rev + " - System Summary Report.pdf")
    pygui.hotkey("alt","s")     # saves report
    if replace == True:
        pygui.press("tab")
        pygui.press("enter")
    time.sleep(1.5)
    pygui.hotkey("alt","c")     # redundant for closing report window
    pygui.hotkey("alt","c")     # closes report window

def drawing(replace,code,rev):
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
    pygui.hotkey("alt","c") # presses second "Continue"
    pygui.write(outputs_folder + "\\" + code + " - " + rev + " - Noded Drawing.pdf")
    pygui.hotkey("alt","s") # saves report
    if replace == True:
        pygui.press("tab")
        pygui.press("enter")
