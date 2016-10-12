#############################################
# Author:   Moataz Mahmoud Farid
# Date:     16th March, 2009
# Verion:   2.0.0
# License:  Public Domain - free to do as you wish
# Homepage: http://moatazfarid.com/tools/des-enc-dec
#############################################

#importing libraries ued in that tool
from pyDes import * #thats a pure implementation of DES and TRIPLE DES encryption algorithms written by Todd Whiteman

#get key
key = "mhgtfihd8"
#get the first 8 bytes only from the key
key = key[0:8]
print(key)

# algo = des(key ,CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
algo = des(key ,CBC, key, pad=None, padmode=PAD_PKCS5)

#testing with textfile

file = open('file1.txt','rb')
enc= algo.encrypt(file.read());
print(enc)
dec = algo.decrypt(enc)
print(dec)
#testing with audio file

#testing with image



