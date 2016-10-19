#############################################
# Author:   Moataz Mahmoud Farid
# Date:     13rd October, 2016
# Verion:   1.0.0
# License:  Public Domain - free to do as you wish
# Homepage: http://moatazfarid.com/tools/des-enc-dec
#############################################

#importing libraries ued in that tool
from pyDes import * #thats a pure implementation of DES and TRIPLE DES encryption algorithms written by Todd Whiteman
from Tkinter import * #GUI
import Tkconstants, tkFileDialog
from tkFileDialog import *
from functools import partial #to send arguments with functions in command

def definations():
    global varFileLocation
    varFileLocation = StringVar()
    global varKey
    varKey = StringVar()
    varKey.set('yourKey')
    global varLocation
    varLocation=''


def DESEncrypt(key='12345678',fileLoc='file'):
    print('key='+key)
    print('file= '+fileLoc)
    #get key must be just 8 char
    if len(key) != 8 : #verifing the key is 8 char = 8*8bit = 64 bit
        key = key[0:8]
    algo = des(key ,ECB, pad=None, padmode=PAD_PKCS5)

    #encrypting file
    File = open(fileLoc,'rb+')
    enc= algo.encrypt(File.read());
    encFile = open(fileLoc+'-encrepted','wb+')
    encFile.write(enc); #write the ecripted data to file
    encFile.close()

def DESDecrypt(key='12345678',fileLoc='file'):
    #get key must be just 8 char
    if len(key) != 8 : #verifing the key is 8 char = 8*8bit = 64 bit
        key = key[0:8]
    algo = des(key ,ECB, pad=None, padmode=PAD_PKCS5)

    # decrepting file
    File = open('file-encrepted','rb+')
    dec= algo.decrypt(File.read());
    decFile = open('file-decrepted','wb+')
    decFile.write(dec); #write the ecripted data to file
    decFile.close()


def getFileLocation(frame1):
    # global varFileLocation
    loc = askopenfilename()
    # print(str(loc))
    print('inside da functions asshole')
    varFileLocation.set(str(loc))
    varLocation=varFileLocation.get()

    #entry to write the location of the file
    lblFileLocation = Label(frame1, text=varFileLocation.get()).grid(row=1, column=2, sticky=W)


def main(win):
    frame1 = Frame(win)
    frame1.pack()

    #object to handle the title of the tool
    lblTitle = 'DES Encrypter'
    Label(frame1, text=lblTitle).grid(row=0, column=1, sticky=W)

    #object to handle the "file" label
    lblSourceFile = "File :"
    Label(frame1, text=lblSourceFile).grid(row=1, column=1, sticky=W)


    #btn to browse
    varFileLocation = StringVar()
    # varFileLocation.set("bla")
    location = Button(frame1, text='Browse', command=lambda: getFileLocation(frame1)).grid(row=1, column=3, sticky=W)

    #key entry
    #object to handle the key entry
    lblTitle = 'key (8 charcters)'
    Label(frame1, text=lblTitle).grid(row=2, column=1, sticky=W)
    Entry(frame1,textvariable = varKey).grid(row=2, column=2, sticky=W)
    # key = varKey
    # key = varKey.get()
    # print(key)
    #encrypt btn
    Button(frame1, text='Encrypt', command=lambda: DESEncrypt(varKey.get(),varLocation)).grid(row=3, column=1, sticky=W)

    #decrypt btn
    Button(frame1, text='Decrypt', command=lambda: DESDecrypt("fghjkhgfhj",str(varFileLocation.get()))).grid(row=3, column=2, sticky=W)

    win.mainloop() #GUI Mainloop


win =Tk() #main widget
definations()
main(win)
