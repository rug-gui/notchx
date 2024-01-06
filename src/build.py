import base64

import subprocess
from click import style
import requests
import importlib.resources
import certifi # hiddenimport
import time
import tkinter
import os
import tempfile
from tkinter import mainloop, ttk
from tkinter.ttk import *
from tkinter.constants import HORIZONTAL, LEFT, RIGHT
import multiprocessing
import urllib.request
from PIL import Image, ImageTk
import io
from multiprocessing import Process
import os

def ImgFromUrl(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image
def ImgFromUrlR(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data)).resize((180,40))
    image = ImageTk.PhotoImage(im)
    return image
installer=tkinter.Tk()
tkinter.Label(text='Notch X',font=('Bold',32)).pack()
url = "https://i.ibb.co/vkTxXJ3/0bbeea2ad486f676890d5e7cac167c2d.png"
image = ImgFromUrl(url)
image_widget = tkinter.Label(installer, image=image)
image_widget.pack()
image_1 = ImgFromUrl("https://ik.imagekit.io/jointest/notchx/tr:h-50/rb5wtbC/btn.png")
image_widget_1 = tkinter.Button(installer,height=50,command=lambda:installing(),relief="flat",overrelief="solid", image=image_1, cursor='hand2')
image_widget_1.pack()
nurl="https://i.ibb.co/HnCQD3G/cc7b835a0e9a9ec03971f6c0613953a2.png"
image_2 = ImgFromUrl(nurl)
image_widget_2 = tkinter.Label(image=image_2)
purl="https://ik.imagekit.io/jointest/notchx/tr:h-80/s6BDR6s/index.png"
image_3 = ImgFromUrl(purl)

tkinter.Label(text='By downloading NotchX you agree to the Terms and Conditions').pack()
#ttk.Button(text='Yes',).pack(side=LEFT)
ttk.Button(text='Cancel',command=installer.destroy).pack(side=RIGHT)
#installer.geometry('180x70')
path=r"C:\\Program Files\\NotchX"
os.chdir('C:\\Program Files')
os.system('mkdir NotchX')

os.chdir(path)
#os.system()

print(requests.utils.DEFAULT_CA_BUNDLE_PATH)
with importlib.resources.path("certifi", "cacert.pem") as ca_path:
    print(ca_path)

def download_latest():
    url = "https://github.com/rug-gui/notchx/releases/download/v0.0.2/notchx_setup.zip"
    #link to export

    r = requests.get(url,verify=False)
    #retrieving data from the URL using get method

    with open("setup.zip", 'wb') as f:
    #giving a name and saving it in any required format
    #opening the file in write mode

        f.write(r.content) 
    #writes the URL contents from the server
        f.close()
    return 0

def installing():
    widgets=installer.pack_slaves()
    global p
    p=0
    for i in widgets:
        if str(i)=='.!label':
            print('Notch X starts installing')
        else:
            i.pack_forget()
    url="https://i.ibb.co/HnCQD3G/cc7b835a0e9a9ec03971f6c0613953a2.png"
    image_2 = ImgFromUrl(url)
    image_widget_2 = tkinter.Label(installer,height=50, image=image_2)
    image_widget_2.pack()
    tkinter.Label(text='Installing').pack()
    '''progress=Progressbar( installer,orient = HORIZONTAL,value=0,length = 100, mode = 'determinate')
    progress.pack()
    print(progress)'''
    download()

def download():
    global p
    download_latest()
    '''k=Process(target=download_latest)
    k.start()
    k.run()'''
    #installer.update_idletasks()
    unzip()

def unzip():
    global p
    print('Unzipping via tar')
    os.system('tar -xf setup.zip')

    '''p=100
    progress['value']=100
    installer.update_idletasks()'''
    done()

def done():
    widgets=installer.pack_slaves()
    for i in widgets:
        if str(i)=='.!label':
            print('Notch X has been installed')
        else:
            i.pack_forget()
    
    image_widget_2.pack()
    tkinter.Label(text='Installation Complete',foreground='green').pack()
    tkinter.Label(text='Do you want to open Notch X?').pack()
    #installer.geometry('180x120')
    def run_notchx():
        # print('Opening')
        #os.chdir(r'C:/Program Files/NotchX')
        #os.startfile(r"C:/Program Files/NotchX/notchx.exe")
        #os.system(r"notchx.exe")
        subprocess.Popen(r"C:/Program Files/NotchX/notchx.exe")
        # exit()
    tkinter.Button(text='Open Now',command=run_notchx,relief='flat',width=189, image=image_3,cursor="hand2").pack()
    ttk.Button(text="Later",command=installer.destroy).pack()

installer.title('Notch X')

installer.mainloop()
