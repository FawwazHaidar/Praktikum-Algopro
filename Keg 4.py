Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import shelve

data = shelve.open("Fawwaz")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
