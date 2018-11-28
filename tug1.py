Data = {"NIM":"L200183143", "Nama":"Fawwaz Haidar Abyansyah Kusuma", "Tempat/Tanggal_Lahir":"Sukoharjo / 12 juni 2000", "Jenis_Kelamin":"Laki - laki", "Golongan_Darah":"AB", "Alamat":"Jetis rt 03/01 wonorejo polokarto sukoharjo", "Agama":"Islam", "Status_Pernikahan":"Belum Menikah", "Pekerjaan":"Mahasiswa", "Kewarganegaraan":"Indonesia"}
NIM = Data["NIM"]
Nama = Data["Nama"]
TTL = Data["Tempat/Tanggal_Lahir"]
JK = Data["Jenis_Kelamin"]
GD = Data["Golongan_Darah"]
Alamat = Data["Alamat"]
Agama = Data["Agama"]
SP = Data["Status_Pernikahan"]
Pekerjaan = Data["Pekerjaan"]
Kewarganegaraan = Data["Kewarganegaraan"]

print("Pilihan Yang Tersedia:")
print("f menampilkan bantuan ini")
print("z menampilkan NIM")
print("x menampilkan Nama")
print("t menampilkan Tempat/Tanggal Lahir")
print("k menampilkan Jenis Kelamin")
print("b menampilkan Golongan Darah")
print("n menampilkan Alamat")
print("i menampilkan Agama")
print("a menampilkan Status Pernikahan")
print("s menampilkan Pekerjaan")
print("u menampilkan Kewarganegaraan")
print("g untuk keluar")
print(" ")

f ='''Pilihan Yang Tersedia:
f menampilkan bantuan ini
z menampilkan NIM
x menampilkan Nama
t menampilkan Tempat/Tanggal Lahir
k menampilkan Jenis Kelamin
b menampilkan Golongan Darah
n menampilkan Alamat
i menampilkan Agama
a menampilkan Status Pernikahan
s menampilkan Pekerjaan
u menampilkan Kewarganegaraan
g untuk keluar'''

g = "Terima Kasih"
w = input("Masukkan huruf: ")
while w != "g":
    if w == "f":
        print(f)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "z":
        print(NIM)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "x":
        print(Nama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "t":
        print(TTL)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "k":
        print(JK)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "b":
        print(GD)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "n":
        print(Alamat)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "i":
        print(Agama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "a":
        print(SP)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "s":
        print(Pekerjaan)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "u":
        print(Kewarganegaraan)
        print(" ")
        w = input("Masukkan huruf: ")
    else:
        print("perintah tidak dikenal")
        print(" ")
        w = input("Masukkan huruf: ")
print(g)
