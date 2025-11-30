from machine import ATM

# Membuat instance dari kelas ATM
machine = ATM()

# Variabel kontrol untuk loop utama
on = True

# Dictionary untuk menyimpan opsi menu
opsions = {
    1:"Lihat Saldo",
    2:"Deposit",
    3:"Tarik Uang",
    4:"Keluar"
}

def opsi():
    # Fungsi untuk menampilkan menu opsi
    for i in range(1, 5):
        print(f"{i}.{opsions[i]}")
        

# Loop utama program
while on:
    print("=== ATM Sederhana ===")
    opsi()  # Menampilkan menu
    try:
        # Menerima input pilihan menu dari pengguna
        chosen = int(input("Pilih Menu: "))
    except NameError and ValueError:
        # Menangani error jika input bukan angka
        print("input kamu tidak valid mohon, input kembali")
        continue
    
    # Logika untuk memproses pilihan menu
    if chosen == 4:
        # Keluar dari program
        on = False
    elif chosen == 1:
        # Menampilkan saldo
        print(machine.liat_saldo())
    elif chosen == 2:
        # Memproses deposit
        deposit = float(input("Masukkan jumlah uang: "))
        print(machine.deposit(deposit))
    elif chosen == 3:
        # Memproses penarikan uang
        withdraw_money = float(input("Masukkan jumlah uang: "))
        print(machine.tarik(withdraw_money))