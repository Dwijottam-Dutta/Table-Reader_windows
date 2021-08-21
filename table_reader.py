# TABLE READER WINDOWS VERSION
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import pygame
import sys
import os
import webbrowser

# Global Declared Var
GAME_SOUNDS={}
w=''
res=''
progress={}


# ######################################Startup#################################
def startup_screen():
    startup()
    GAME_SOUNDS['start'].play()
    bar()
    bar_two()
    
    
def bar():
    global w
    a='#E99497'
    l4=Label(w,text='Software developed by Dwijottam and Dwijoraj Dutta',fg='white',bg=a)
    lst4=('Century Gothic',9)
    l4.config(font=lst4)
    l4.place(x=10,y=210)
    import time
    r=0
    for i in range(110):
        
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.05)
        r=r+1
    


def bar_two():
    global w
    r=0
    for i in range(100):
        
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.02)
        r=r+1
    w.destroy()
    
def backbar():
    global w
    r=0
    for i in range(100):
        
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.0001)
        r=r+1

def startup():
    global w
    global progress
    w=Tk()
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

    w.overrideredirect(1)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='#E99497', background='#D83A56')
    progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')
      
    progress.place(x=-10,y=235)
    backbar()

    a='#E99497'
    Frame(w,width=427,height=241,bg="#E99497").place(x=0,y=0)  #249794


    l1=Label(w,text='Table Reader',fg='white',bg=a)
    lst1=('System',30,'bold')
    l1.config(font=lst1)
    l1.place(x=20,y=70)


    l3=Label(w,text='A simple multiplication table reader',fg='white',bg=a)
    lst3=('System',15)
    l3.config(font=lst3)
    l3.place(x=20,y=120)

 
# ##############################################################################


# ######################################Restart#################################
def restartup_screen():
    restartup()
    GAME_SOUNDS['start'].play()
    bar_res()
    bar_two_res()
    
    
def bar_res():
    global res
    a='#E99497'
    l4=Label(res,text='Restarting . . .',fg='white',bg=a)
    lst4=('Century Gothic',9)
    l4.config(font=lst4)
    l4.place(x=10,y=210)
    import time
    r=0
    for i in range(110):
        
        progress['value']=r
        res.update_idletasks()
        time.sleep(0.05)
        r=r+1
    


def bar_two_res():
    global res
    r=0
    for i in range(100):
        
        progress['value']=r
        res.update_idletasks()
        time.sleep(0.02)
        r=r+1
    res.destroy()
    
def backbar_res():
    global res
    r=0
    for i in range(100):
        
        progress['value']=r
        res.update_idletasks()
        time.sleep(0.0001)
        r=r+1

def restartup():
    global res
    global progress
    res=Tk()
    width_of_window = 427
    height_of_window = 250
    screen_width = res.winfo_screenwidth()
    screen_height = res.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    res.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

    res.overrideredirect(1)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='#E99497', background='#D83A56')
    progress=Progressbar(res,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')
      
    progress.place(x=-10,y=235)
    backbar_res()

    a='#E99497'
    Frame(res,width=427,height=241,bg="#E99497").place(x=0,y=0)  #249794


    l1=Label(res,text='Table Reader',fg='white',bg=a)
    lst1=('System',30,'bold')
    l1.config(font=lst1)
    l1.place(x=20,y=70)


    l3=Label(res,text='A simple multiplication table reader',fg='white',bg=a)
    lst3=('System',15)
    l3.config(font=lst3)
    l3.place(x=20,y=120)

 
# ##############################################################################

# ####################################Shutdown##################################

def on_closing():
    GAME_SOUNDS['stop'].play()
    time.sleep(3)
    tab.destroy()
    
# ##############################################################################


# Function for opening link (used in third party licence)
def callback(url):
    webbrowser.open_new(url)


# Function which will open window of third party licence
def licenceagree():
    li = Tk()
    li.configure(background="#10caeb")
    li.title(" Third Party Licenses")
    li.geometry("700x390")
    li.iconbitmap("./assets/table_reader.ico")
    li.resizable(0, 0)
    Label(li, text="Third Party Licenses", bg='light green', padx=195, font=('System', 25, 'bold')).place(x=0)
    Label(li, text='''Table Reader is made possible by these''', bg='#10caeb', font=('System', 17, 'bold')).place(
        x=3, y=50)
    Label(li, text='''following open source softwares: ''', bg='#10caeb', font=('System', 17, 'bold')).place(x=3, y=75)
    
    Label(li, text='''Python (programming language) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=15, y=110)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=15, y=130)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/license.html"))
    
    Label(li, text='''Tkinter (GUI Framework for python) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=15, y=160)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=15, y=180)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/tkinter.html"))
    
    Label(li, text='''tkinter.messagebox (Tkinter message prompts) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=15, y=210)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=15, y=230)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/tkinter.messagebox.html"))
    
    Label(li, text='''Webbrowser (Python Browser controller) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=15, y=260)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=15, y=280)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/webbrowser.html"))
    
    Label(li, text='''Time (Python Library for Time access) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=15, y=310)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=15, y=330)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/time.html"))
    
    Label(li, text='''Pygame (Python Library used for sounds) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=345, y=110)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=345, y=130)
    hello.bind("<Button-1>", lambda e: callback("https://www.pygame.org/docs/"))
    
    Label(li, text='''os (Miscellaneous operating system interfaces)''', bg='#10caeb', font=('System', 9, 'bold')).place(x=345, y=160)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=345, y=180)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/os.html"))
    
    Label(li, text='''Sys (System-specific parameters and functions) ''', bg='#10caeb', font=('System', 9, 'bold')).place(x=345, y=210)
    hello=Label(li, text='''View License''', fg = 'blue', bg='#10caeb', cursor= "hand2", font=('System', 9, 'underline'))
    hello.place(x=345, y=230)
    hello.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/sys.html"))
    

# Funtion which opens the about in which about us is described
def aboutmore():
    aboutusmore = Tk()
    aboutusmore.configure(background="light green")
    aboutusmore.title(" About Table Reader")
    aboutusmore.geometry("340x120")
    aboutusmore.iconbitmap("./assets/table_reader.ico")
    aboutusmore.resizable(0, 0)                                   # |
    Label(aboutusmore, text='''Table Reader is simple multiplication''', bg='light green', font=('System', 17, 'bold')).place(
        x=5, y=10)
    Label(aboutusmore, text='''table reader, developed by Dwijottam ''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=40)
    Label(aboutusmore, text='''and Dwijoraj Dutta...''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=70)


# Function which will open the about window where version, whats new, more about software is there
def about():
    aboutus = Tk()
    aboutus.configure(background="#FF616D")
    aboutus.title(" About Table Reader")
    aboutus.geometry("340x290")
    aboutus.iconbitmap("./assets/table_reader.ico")
    aboutus.resizable(0, 0)
    
    Label(aboutus, text="Table Reader", bg='#FF616D', font=('System', 20, 'bold')).place(x=10, y=10)
    
    Label(aboutus, text="Windows Edition", bg='#FF616D', font=('System', 13, 'bold')).place(x=10, y=45)
    
    Label(aboutus, text="Version", bg='#FF616D', font=('System', 10, 'bold')).place(x=239, y=15)
    
    Label(aboutus, text="V.1.3.4", bg='#FF616D', font=('System', 17, 'bold')).place(x=239, y=35)
    
    Label(aboutus, text="What's New:", bg='#FF616D', font=('System', 10, 'bold')).place(x=10, y=90)
    
    Label(aboutus, text="$ Performance Enhanced", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=112)
    
    Label(aboutus, text="$ UI design enhanced for  ", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=132)
    
    Label(aboutus, text="   professional look and feel", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=150)
    
    Label(aboutus, text="$ Start Up Sound", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=172)

    Label(aboutus, text="$ Tables availability increased ", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=192)

    Label(aboutus, text="$ Window manupulating buttons added", bg='#FF616D', font=('System', 11, 'bold')).place(x=15, y=212)
    
    licen = Button(aboutus, text="Third Party Licenses",fg="#fff", bg='#0A1D37', cursor = "hand2", font=('System', 10), command = licenceagree)
    licen.place(x=100, y=250)

    aboutbut = Button(aboutus, text='More', fg='#000', bg='#FFBD9B', height=1, width=6, font=('System', 13), command=aboutmore)
    aboutbut.place(x=230, y=75)
    
    # Label(aboutus, text='''CalCharm is Simple Hackable Calculator''', bg='#10caeb', font=('System', 17, 'bold')).place(
    #     x=5, y=10)
    # Label(aboutus, text='''developed by Dwijottam Dutta ''', bg='#10caeb', font=('System', 17, 'bold')).place(x=5, y=40)
    # Label(aboutus, text='''and Dwijoraj Dutta...''', bg='#10caeb', font=('System', 17, 'bold')).place(x=5, y=70)
    aboutus.mainloop()
    
def restart():
    tab.title("Restart")
    time.sleep(1)
    tab.title("Restart .")
    time.sleep(1)
    tab.title("Restart . .")
    time.sleep(1)
    tab.title("Restart . . .")
    time.sleep(1)
    tab.title("Restarting . . .")
    GAME_SOUNDS['stop'].play()
    time.sleep(3)
    tab.withdraw()
    time.sleep(1)
    restartup_screen()
    tab.deiconify()
    tab.title("Table Reader - Restarted Successfully")
    time.sleep(2)
    tab.title("Table Reader")
    
    
def limitSizeDay(*args):
    value = limitValue.get()
    if len(value) > 5: limitValue.set(value[:5])
    
def edit_label():
    input_value=entry.get()
    fetch = int(input_value)
    header=Label(tab, text="Table of "+str(fetch), bg='#66DE93', padx=13,width=22, font=('System', 18), anchor=W,justify=CENTER)
    header.place(x=0, y=200)

    first=Label(tab, text=str(fetch)+" x 1 = "+str(fetch), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    first.place(x=0, y=239)

    second=Label(tab, text=str(fetch)+" x 2 = "+str(fetch*2), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    second.place(x=0, y=271)

    third=Label(tab, text=str(fetch)+" x 3 = "+str(fetch*3), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    third.place(x=0, y=303)

    fourth=Label(tab, text=str(fetch)+" x 4 = "+str(fetch*4), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    fourth.place(x=0, y=335)

    fifth=Label(tab, text=str(fetch)+" x 5 = "+str(fetch*5), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    fifth.place(x=0, y=367)

    sixth=Label(tab, text=str(fetch)+" x 6 = "+str(fetch*6), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    sixth.place(x=0, y=399)

    seventh=Label(tab, text=str(fetch)+" x 7 = "+str(fetch*7), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    seventh.place(x=0, y=431)

    eighth=Label(tab, text=str(fetch)+" x 8 = "+str(fetch*8), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    eighth.place(x=0, y=463)

    ninth=Label(tab, text=str(fetch)+" x 9 = "+str(fetch*9), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    ninth.place(x=0, y=495)

    tenth=Label(tab, text=str(fetch)+" x 10 = "+str(fetch*10), bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    tenth.place(x=0, y=527)
    
if __name__ == "__main__":
    pygame.init()  
    pygame.mixer.init()
    GAME_SOUNDS['start'] = pygame.mixer.Sound('./assets/startup.mp3')
    GAME_SOUNDS['stop'] = pygame.mixer.Sound('./assets/shutdown.wav')
    startup_screen()
    tab = Tk()
    tab.configure(background="#66DE93")
    tab.title(" Table Reader")
    width_of_window = 400
    height_of_window = 610
    tab.geometry(str(width_of_window)+"x"+str(height_of_window))
    tab.iconbitmap("./assets/table_reader.ico")
    tab.resizable(0, 0)
    style = ttk.Style()
    Label(tab, text="Table Reader", bg='#FF616D', padx=72, font=('System', 30, 'bold')).place(x=0)
    Label(tab, text="A simple multiplication table reader", bg='#FF616D', padx=63, font=('System', 17, 'bold')).place(x=0, y=50)
    Label(tab, text="Enter Table Number", bg='#66DE93',padx=113, font=('Century Gothic', 14)).place(x=0, y=90)
    
    limitValue = StringVar()
    limitValue.trace('w', limitSizeDay)
    entry = Entry(tab, width=23,bg='#66DE99', highlightthickness=0,font=('Century Gothic', 13), textvariable=limitValue)
    entry.place(x=100, y=130)
    entry.insert(0, "1")
    
    Button(tab,text="Read Table", bg='#FF616D',padx=3, font=('System', 11), command=edit_label).place(x=160, y=160)

    header=Label(tab, text="Table of 1", bg='#66DE93', padx=13,width=22, font=('System', 18), anchor=W,justify=CENTER)
    header.place(x=0, y=200)

    first=Label(tab, text="1 x 1 = 1", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    first.place(x=0, y=239)

    second=Label(tab, text="1 x 2 = 2", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    second.place(x=0, y=271)

    third=Label(tab, text="1 x 3 = 3", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    third.place(x=0, y=303)

    fourth=Label(tab, text="1 x 4 = 4", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    fourth.place(x=0, y=335)

    fifth=Label(tab, text="1 x 5 = 5", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    fifth.place(x=0, y=367)

    sixth=Label(tab, text="1 x 6 = 6", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    sixth.place(x=0, y=399)

    seventh=Label(tab, text="1 x 7 = 7", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    seventh.place(x=0, y=431)

    eighth=Label(tab, text="1 x 8 = 8", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    eighth.place(x=0, y=463)

    ninth=Label(tab, text="1 x 9 = 9", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    ninth.place(x=0, y=495)

    tenth=Label(tab, text="1 x 10 = 10", bg='#66DE93', width=29, font=('Century Gothic', 18, 'bold'), anchor=CENTER,justify=CENTER)
    tenth.place(x=0, y=527)

    MenuBar = Menu(tab)
    MenuBar.add_cascade(label="Close")
    MenuBar.add_cascade(label="Restart", command=restart)
    MenuBar.add_cascade(label="About", command=about)
    tab.protocol("WM_DELETE_WINDOW", on_closing)
    

    tab.config(menu=MenuBar)
    tab.mainloop()