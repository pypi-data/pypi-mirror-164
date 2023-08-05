import pyautogui
import sys
import time
import random
import os
import subprocess
import pandas as pd
from random import choice
from string import digits
import tempfile

if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
    from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
from PIL.PngImagePlugin import PngImageFile, PngInfo

from aai_engine_package.screenshot_taker import ScreenShotTaker

pyautogui.FAILSAFE = True

LARGE_FONT = ("Courier", 12)
NORM_FONT = ("Courier", 10)
SMALL_FONT = ("Courier", 8)

REGION_PICK_VIEW = 0
OFFSET_PICK_VIEW = 1
SIMILARITY_PICK_VIEW = 2
NAME_PICK_VIEW = 3 

CWD = os.getcwd()

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "my_screenshot.png"
abs_file_path = os.path.join(script_dir, rel_path)
SCREENSHOT = abs_file_path

dirname = os.path.dirname(__file__)
if os.name == "posix":
    icon_path = os.path.join(dirname, r'style/icon.ico')
    theme_path = os.path.join(dirname, r'style/sun-valley.tcl')
else:
    icon_path = os.path.join(dirname, r'style\icon.ico')
    theme_path = os.path.join(dirname, r'style\sun-valley.tcl')

class TaskWrapper():
    """
    Task wrapper class to control execution
    """
    def __init__(self, task_id, name, cwd, script, scheduled_time, frequency=-1, trigger=lambda _ : True):
        self.task_id = task_id
        self.name = name
        self.cwd = cwd
        self.steps = []
        self.script = script
        self.scheduled_time = scheduled_time
        self.frequency = frequency
        self.trigger = trigger

    def execute(self):
        print("Executing script")
        filepath=self.script # TODO: checks on file
        SW_MINIMIZE = 6
        # info = subprocess.STARTUPINFO()
        # info.dwFlags = subprocess.STARTUPINFO()
        # info.wShowWindow = SW_MINIMIZE
        p = subprocess.Popen(['python', filepath], cwd=self.cwd) #, startupinfo=info)
        # stdout, stderr = p.communicate()
        return p
    

class Task():
    """
    Task class to control and keep track of all information and steps within a task
    """
    def __init__(self, name, cwd, script=None):
        self.name = name
        self.cwd = cwd
        self.steps = []
        self.script = script

    def add_step(self, step):
        self.steps.append(step)

    def execute(self):
        if self.script is None:
            for step in self.steps:
                step.execute()
        else:
            # For legacy scripts or external scripts outside the engine
            print("Executing script")
            filepath=self.script # TODO: checks on file
            p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(p.returncode) # is 0 if success
            


class Step():
    """
    Keep track of a certain step within a task
    """
    def __init__(self, name, func, *args):
        self.name = name
        self.func = func
        self.args = args

    def execute(self):
        self.func(*self.args)


def click(img_location):
    """
    Locate the given image on the screen and click it.
    """
    click_n(img_location, 1)

def click_right(img_location):
    """
    Locate the given image on the screen and right click it.
    """
    click_n(img_location, 1, button="right")

def double_click(img_location):
    """
    Locate the given image on the screen and click it 2 times.
    """
    click_n(img_location, 2)

def click_n(img_location, n, button='left'):
    """
    Locate the given image on the screen and click it n times.
    """
    full_file_path = '/'.join([CWD, img_location])
    img = PngImageFile(full_file_path)
    print(img.text)
    print("Confidence: ", float(img.text["confidence"]))
    box_location = pyautogui.locateOnScreen(full_file_path, confidence=float(img.text["confidence"]))
    
    if box_location is None:
        raise RuntimeError("Image not found on current screen.")

    print(box_location)
    x_coord = int(float(img.text["offset_x"]))
    y_coord = int(float(img.text["offset_y"]))
    if os.name == 'posix': # resolution is half the size on macos for some reason
        x_coord /= 2
        y_coord /= 2
        x_coord += (box_location.left + box_location.width / 2) / 2
        y_coord += (box_location.top + box_location.height / 2) / 2
    else:
        x_coord += box_location.left + box_location.width / 2
        y_coord += box_location.top + box_location.height / 2
    print(x_coord, y_coord)
    for _ in range(0,n):
        pyautogui.click(x=x_coord, 
                        y=y_coord,
                        button=button)
    print("Clicked: {img}".format(img=img_location))

def exists(img_location):
    """
    Check if a given image exists on the current screen.
    Return: boolean
    """
    full_file_path = '/'.join([CWD, img_location])
    img = PngImageFile(full_file_path)
    print(img.text)
    box_location = pyautogui.locateOnScreen(full_file_path, confidence=float(img.text["confidence"]))
    
    return box_location is not None

def wait(img_location, seconds):
    """
    Wait a given amount of seconds for a given image, checking its existence. 
    TODO: check if total waiting time matches given seconds.
    """
    print("Waiting for: ", img_location)
    starttime = time.time()
    for x in range(0, seconds):
        print(x)
        if exists(img_location):
            return
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    raise RuntimeError("Timeout: Image not found.")

def sleep(seconds):
    """
    Sleep for a given number of seconds
    """
    time.sleep(seconds)

def type_text(text):
    """
    Type a given text
    """
    pyautogui.write(text)

def key_combo(*keys):
    """
    Type a given key comination
    (ctrl, shift, esc, f1, ...)
    """
    print(*keys)  
    pyautogui.hotkey(*keys)

def remove_char(n=1):
    """
    Remove n characters (backspace)
    """
    for x in range(0, n):
        pyautogui.hotkey("backspace")

### FILE READ UTILS ###
def read_excel(path):
    return pd.read_excel(path).to_dict(orient='records')

def cli():
    if len(sys.argv) == 2:
        save_location = sys.argv[1]
        print(os.getcwd(), save_location)
    print("Called aai-engine-capture")
    main("H:\AdAstraIndustries\aai_engine\img")

def test_edit(save_location, h):
    pass

def edit(save_location, haystack):
    main(save_location, haystack, editing=True)

def main(save_location, haystack=r"C:\Users\Toto\Documents\AdAstraIndustries\aai_engine\img\cv.png", editing=False):
    temp_screenshot = tempfile.NamedTemporaryFile(suffix='.png')
    temp_screenshot_path = temp_screenshot.name
    # take_screenshot(temp_screenshot_path)
    take_screenshot()
    # TODO: make title bar black
    # aai_window = AAIWindow()
    # root = aai_window.root
    
    root = tkinter.Tk()
    style = ttk.Style(root)
    root.wm_iconbitmap(icon_path)
    root.wm_colormapwindows()
    
    root.tk.call('source', theme_path)
    root.tk.call("set_theme", "dark")

    if editing:
        print(" - EDIT MODE - ")
        app = ScreenShotTaker(root, save_location, haystack=haystack, editing=True) # When editing from extension
    else:
        print(" - CREATE MODE - ")
        app = ScreenShotTaker(root, save_location, editing=False)

    root.mainloop()

class AAIWindow():

    def __init__(self):
        self.root = tkinter.Tk()
        style = ttk.Style(self.root)
        self.root.wm_iconbitmap(icon_path)
        self.root.wm_colormapwindows()
        self.root.overrideredirect(True) # turns off title bar, geometry
        self.root.geometry('400x100+200+200') # set new geometry

        # make a frame for the title bar
        title_bar = tkinter.Frame(self.root, bg='black', relief='flat', bd=2)

        # put a close button on the title bar
        close_button = ttk.Button(title_bar, text='X', command=self.root.destroy)

        # pack the widgets
        title_bar.pack(expand=1, fill=tkinter.X)
        close_button.pack(side=tkinter.RIGHT)

        # bind title bar motion to the move window function
        title_bar.bind('<B1-Motion>', self.move_window)
        title_bar.bind('<Button-1>', self.get_pos)

        # root.configure(background='#3E4149')
        self.root.tk.call('source', theme_path)
        # root.tk.call('package', 'require', 'awdark')
        # style.theme_use('dark')
        self.root.tk.call("set_theme", "dark")

    def move_window(self, event):
        self.root.geometry("400x400" + '+{0}+{1}'.format(event.x_root + self.xwin, event.y_root + self.ywin))

    def get_pos(self, event):
        xwin = self.root.winfo_x()
        ywin = self.root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        self.ywin = ywin - starty
        self.xwin = xwin - startx

def take_screenshot(file_path='my_screenshot.png'):
    """
    Take a screenshot.
    Args:
        
    """
    print("Taking screenshot")
    # time.sleep(3)
    im = pyautogui.screenshot(file_path)
    print("Done")

def take_screenshot_save(save_location):
    """
    Take a screenshot.
    Args:
        
    """
    print("Taking screenshot")
    # time.sleep(3)
    save_path = ''.join([save_location, "/img/aai_", ''.join(choice(digits) for i in range(12)), ".png"])
    im = pyautogui.screenshot(save_path)
    print("Done")

