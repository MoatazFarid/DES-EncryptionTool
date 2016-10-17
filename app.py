#############################################
# Author:   Moataz Mahmoud Farid
# Date:     16th March, 2009
# Verion:   2.0.0
# License:  Public Domain - free to do as you wish
# Homepage: http://moatazfarid.com/tools/des-enc-dec
#############################################

#importing libraries ued in that tool
from pyDes import * #thats a pure implementation of DES and TRIPLE DES encryption algorithms written by Todd Whiteman
import Tkinter #GUI

top = Tkinter.Tk() #main widget



top.mainloop() #GUI Mainloop



#get key must be just 8 char
key = "12345678"

algo = des(key ,ECB, pad=None, padmode=PAD_PKCS5)

#encrypting file
File = open('file','rb+')
enc= algo.encrypt(File.read());
encFile = open('file-encrepted','wb+')
encFile.write(enc); #write the ecripted data to file
encFile.close()


# decrepting file
File = open('file-encrepted','rb+')
dec= algo.decrypt(File.read());
decFile = open('file-decrepted','wb+')
decFile.write(dec); #write the ecripted data to file
decFile.close()


