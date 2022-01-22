
from tkinter import *
import customtkinter
from customtkinter.customtkinter_label import CTkLabel
import os
import subprocess
'''
def load_images():
    # Can Be Colored & Resized based on preferences
    urllib.request.urlretrieve(
    'https://img.icons8.com/fluency/48/000000/mail.png',
    "mail.png")
    urllib.request.urlretrieve(
    'https://img.icons8.com/color-glass/48/000000/partly-cloudy-night.png',
    "weather.png")

    urllib.request.urlretrieve(
    'https://img.icons8.com/color-glass/46/000000/whatsapp.png',
    "whatsapp.png")

    urllib.request.urlretrieve(
    'https://img.icons8.com/color/46/000000/telegram-app.png',
    "telegram.png")

    urllib.request.urlretrieve(
    'https://img.icons8.com/fluency/24/000000/mail.png',
    "mail_24.png")
    urllib.request.urlretrieve(
    'https://img.icons8.com/color-glass/24/000000/partly-cloudy-night.png',
    "weather_24.png")

    urllib.request.urlretrieve(
    'https://img.icons8.com/color-glass/24/000000/whatsapp.png',
    "whatsapp_24.png")

    urllib.request.urlretrieve(
    'https://img.icons8.com/color/24/000000/telegram-app.png',
    "telegram_24.png")

    urllib.request.urlretrieve(
    "https://img.icons8.com/ios-glyphs/24/000000/hide.png",
    "hide_24.png")

    urllib.request.urlretrieve(
    "https://img.icons8.com/ios-glyphs/24/000000/visible.png",
    "unhide_24.png")
    print('loaded')'''
root=Tk()
root.config(bg='SystemButtonFace',cursor='none')
root.overrideredirect(True)
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
root.geometry('175x25+{}+0'.format((ws//2)-125))
root.wm_attributes('-transparentcolor','SystemButtonFace')


import urllib.request
from PIL import Image,ImageTk

'''
img = Image.open("mail_24.png")
icon_24=ImageTk.PhotoImage(img)
weather_icon_24=PhotoImage(file='weather_24.png')
hide_icon_24=PhotoImage(file='hide_24.png')
unhide_icon_24=PhotoImage(file='unhide_24.png')
whatsapp_icon_24=PhotoImage(file='whatsapp_24.png')
telegram_icon_24=PhotoImage(file='telegram_24.png')'''
'''
img.load()
background = Image.new("RGB", img.size, (255, 255, 255))
background.paste(img, mask=img.split()[3]) # 3 is the alpha channel

background.save('mail.png', 'PNG', quality=80)'''
'''
img = Image.open("AppData/IconData/Fluent/icons8_search_more_48px.png").resize((22,22))
icon=ImageTk.PhotoImage(img)
weather_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_game_controller_48px.png').resize((22,22)))
whatsapp_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_settings_48px.png').resize((22,22)))
telegram_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_contact_us_48px_1.png').resize((22,22)))
notes_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_note_48px.png').resize((22,22)))
mail_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_open_envelope_48px.png').resize((22,22)))
dashboard_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_dashboard_layout_48px.png').resize((22,22)))
#notes_icon=ImageTk.PhotoImage(Image.open('AppData/IconData/Fluent/icons8_contact_us_48px_1.png'))
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW'''
main_frame=customtkinter.CTkFrame(bg_color='SystemButtonFace',fg_color='SystemButtonFace',height=25,width=175)
main_frame.pack(expand=True,fill='both')
main_frame.configure(cursor='none')
content_frame=customtkinter.CTkFrame(main_frame,bg_color='SystemButtonFace',fg_color='#000000',height=25,width=175)
content_frame.configure(cursor='none')
content_frame.pack(side=TOP,expand=True,fill='both')
'''
left_frame=Frame(content_frame,height=10)
left_frame.pack(side=LEFT,padx=8)
b1=Label(left_frame,image=icon,background='#000000',cursor='hand2',height=20)
def open_quicksearch(event=None):
    subprocess.call('explorer shell:appsfolder\com.squirrel.Wox.Wox',startupinfo=si)
b1.bind('<Button-1>',open_quicksearch)
b1.pack(side=LEFT)
b2=Label(left_frame,image=weather_icon,background='#000000',cursor='hand2',height=20)
def open_gamebar(event=None):
    subprocess.call('explorer shell:appsfolder\Microsoft.XboxGamingOverlay_8wekyb3d8bbwe!App',startupinfo=si)
b2.bind('<Button-1>',open_gamebar)
b2.pack(side=LEFT)
bt1=Label(left_frame,image=mail_icon,background='#000000',cursor='hand2',height=20)
def open_work(event=None):
    subprocess.call('explorer shell:appsfolder\com.squirrel.Teams.Teams',startupinfo=si)
bt1.bind('<Button-1>',open_work)
bt1.pack(side=RIGHT)
center_frame=Frame(content_frame,bg='white')
#center_frame.pack(side=LEFT,fill=X,expand=TRUE)
d1=Label(center_frame,image=dashboard_icon,background='#000000',cursor='hand2',height=20)
d1.pack(side=TOP)
right_frame=Frame(content_frame)
right_frame.pack()
bt2=Label(right_frame,image=notes_icon,background='#000000',cursor='hand2',height=20)
def open_notes(event=None):
    subprocess.call('explorer shell:appsfolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App',startupinfo=si)
bt2.bind('<Button-1>',open_notes)
bt2.pack(side=LEFT)
b3=Label(right_frame,image=whatsapp_icon,background='#000000',cursor='hand2',height=20)
b3.pack(side=LEFT)
def open_settings(event=None):
    subprocess.call('explorer shell:appsfolder\windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel',startupinfo=si)
b3.bind('<Button-1>',open_settings)
b4=Label(right_frame,image=telegram_icon,background='#000000',cursor='hand2',height=20)
def open_contacts(event=None):
    subprocess.call('explorer shell:appsfolder\Microsoft.YourPhone_8wekyb3d8bbwe!App',startupinfo=si)
b4.bind('<Button-1>',open_contacts)
b4.pack()'''
root.hide=False
'''def hide_wnd(event):
    root.wm_attributes('-alpha',0.5)
    root.wm_attributes('-topmost',False)
    hide.config(image=unhide_icon_24)
    root.hide=True'''
def inactive(event):   
    if root.hide:
        print('Hidden')
    else:
        '''content_frame.corner_radius=0
        content_frame.draw()'''
        #root.wm_attributes('-alpha',0.7)
        #content_frame.canvas.configure(cursor='fleur')
        '''b1.config(image=icon_24)
        b2.config(image=weather_icon_24)
        global hide
        hide=Label(content_frame,image=hide_icon_24,background='#000000',cursor='hand2',height=20)
        hide.bind('<Button-1>',hide_wnd)
        hide.pack(side=TOP)
        b3.config(image=whatsapp_icon_24)
        b4.config(image=telegram_icon_24)
        main_frame.configure(width=150,height=25)
        content_frame.configure(width=150,height=25)
        root.geometry('150x25+660+0')
        root.update()'''
        root.wm_attributes('-topmost',True)
        #root.wm_attributes('-alpha',0.75)
        

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , 0))


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
def right_click(event):
    content_frame.canvas.bind('<Button-1>', SaveLastClickPos)
    content_frame.canvas.bind('<B1-Motion>', Dragging)

root.bind("<Button-3>",right_click)
root.bind("<FocusOut>", inactive)
def close_win(e):
   root.destroy()
root.bind('<Escape>', lambda e: close_win(e))
# importing modules
'''
tp=Toplevel()
tp.config(bg='white')

tp.overrideredirect(True)
tp.geometry('350x50+660+0')
tp.wm_attributes('-transparentcolor','white')
tp.wm_attributes('-topmost',True)
tp.wm_attributes('-alpha',0.5)

tp=customtkinter.CTkFrame(tp,bg_color='white',fg_color='#000000',height=50,width=350)
tp.pack()'''
'''
tp=Toplevel()
tp.config(bg='white')

tp.overrideredirect(True)
tp.geometry('{}x25+0+0'.format(ws,hs))
tp.wm_attributes('-transparentcolor','white')
tp.wm_attributes('-topmost',True)
tp.wm_attributes('-alpha',0.5)
root.wm_attributes('-topmost',True)
tp.bind("<FocusIn>", inactive)
tp.bind("<FocusOut>", inactive)
trp=customtkinter.CTkFrame(tp,bg_color='white',fg_color='black',height=hs,width=ws)
trp.pack()
'''
root.mainloop()