Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import shelve

data = open("L200183143", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Fawwaz")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
