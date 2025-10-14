import re
x = "-"
x*=10
print(f"{x} login sederhana {x}")
def registrasi():
    email = input("masukkan email anda\n")
    username = input("masukkan username anda\n")
    pw = input("masukkan password anda\n")
    kon_pw = input("masukkan konfirmasi password anda\n")
    if pw == kon_pw:
        print("password benar\n")
    else:
        print("password tidak benar\n")
        return False

    with open("database.txt", "a") as dtb:
        dtb.write(f"{email}:{username}:{pw}\n")
    



def login():
    username = input("masukkan username anda\n")
    pw = input("masukkan password anda\n")

    with open("database.txt", "r") as file:
        users = file.readlines()

    for user in users:
        data = user.strip().split(":")
        if data[1] == username and data[2] == pw:
            print("Login berhasil! Selamat datang,", username)
            return True
    
    print("Username atau password salah!\n")
    return False



on = True 
while on:
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilih = int(input("pilih menu (1/2/3) :"))

    if pilih == 1:
        registrasi()
    elif pilih == 2:
        login()
    elif pilih == 3:
        print("program selesai")
        break
    else:
        print("inputan anda salah")