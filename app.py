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
from tkFileDialog import * # to browse files

def definations():
    global varFileLocation
    varFileLocation = StringVar()
    global varKey #this is the text variable which have the key value
    varKey = StringVar()
    global varLocation
    varLocation=''
    global lblDoneSignal #occure after a successfull encryption/decryption
    lblDoneSignal = ''

def DESEncrypt(key='12345678',fileLoc='file'):
    print('key='+key)
    print('file= '+fileLoc)
    #get key must be just 8 char
    if len(key) != 8 : #verifing the key is 8 char = 8*8bit = 64 bit
        key = key[0:8]
    algo = des(key ,CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    #encrypting file
    File = open(fileLoc,'rb+')
    enc= algo.encrypt(File.read());
    encFile = open(fileLoc+'-encrypted','wb+')
    encFile.write(enc); #write the ecripted data to file
    encFile.close()

def DESDecrypt(key='12345678',fileLoc='file'):
    #get key must be just 8 char
    if len(key) != 8 :
        key = key[0:8]
    algo = des(key ,CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    # decrypting file
    File = open(fileLoc,'rb+')
    dec= algo.decrypt(File.read());
    decFile = open(fileLoc+'-decrypted','wb+')
    decFile.write(dec); #write the ecripted data to file
    decFile.close()


def getFileLocation(frame1):
    # global varFileLocation
    loc = askopenfilename()
    varFileLocation.set(str(loc))

    # entry to write the location of the file
    lblFileLocation = Label(frame1, text=varFileLocation.get()).grid(row=1, column=2, sticky=W)
    return varFileLocation.get()

def encryptHandler():
    location = varFileLocation.get() # getting the location
    key = varKey.get()#getting the key
    DESEncrypt(key,location)#applying the Encryptions
    lblDoneSignal = "Done !!" ##ocure after the app finish it
    #object to handle the "DONE" label
    Label(frame1, text=lblDoneSignal).grid(row=3, column=3, sticky=W)

def decryptHandler():
    location = varFileLocation.get() # getting the location
    key = varKey.get()#getting the key
    DESDecrypt(key,location)#applying the Encryptions
    lblDoneSignal = "Done !!" ##ocure after the app finish it
    #object to handle the "DONE" label
    Label(frame1, text=lblDoneSignal).grid(row=3, column=3, sticky=W)

def main(win):
    global frame1
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
    Button(frame1, text='Browse', command=lambda: getFileLocation(frame1)).grid(row=1, column=3, sticky=W)

    #object to handle the key entry
    lblTitle = 'key (8 charcters)'
    Label(frame1, text=lblTitle).grid(row=2, column=1, sticky=W)
    Entry(frame1,textvariable = varKey).grid(row=2, column=2, sticky=W)

    #encrypt btn
    Button(frame1, text='Encrypt', command=encryptHandler ).grid(row=3, column=1, sticky=W)

    #decrypt btn
    Button(frame1, text='Decrypt', command=decryptHandler ).grid(row=3, column=2, sticky=W)


    win.mainloop() #GUI Mainloop


win =Tk() #main widget
definations()
main(win)
