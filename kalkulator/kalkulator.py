# Membuat garis pemisah dekoratif sepanjang 50 karakter
a = "-"
a *= 50
# Menampilkan header program "KALKULATOR" dengan garis dekoratif
print(a + "KALKULATOR" + a)

# Inisialisasi list untuk menyimpan riwayat perhitungan
riwayat = []

# Variabel kontrol untuk loop utama program
mulai = True

# Loop utama program
while mulai:
    try:
        # Meminta input dari pengguna
        nmr_1 = int(input("nomor pertama: "))  # Input angka pertama
        operator = input("operator ('+', '-', '*', '/', '%'): ")  # Input operator matematika
        nmr_2 = int(input("nomor kedua: "))  # Input angka kedua

        # Template string untuk output hasil
        txt = "hasil = {} "
        hasil_riwayat = "Riwayat Kalkulator:\n{}"

        # Logika operasi matematika berdasarkan operator yang dipilih
        if operator == "+":
            # Penjumlahan
            hasil = nmr_1 + nmr_2
            print(txt.format(hasil))
        elif operator == "-":
            # Pengurangan
            hasil = nmr_1 - nmr_2
            print(txt.format(hasil))
        elif operator == "*":
            # Perkalian
            hasil = nmr_1 * nmr_2
            print(txt.format(hasil))
        elif operator == "/":
            # Pembagian
            hasil = nmr_1 / nmr_2
            print(txt.format(hasil))
        elif operator == "%":
            # Pembagian
            hasil = nmr_1 % nmr_2
            print(txt.format(hasil))
        else:
            # Handler untuk operator yang tidak valid
            print("your input not valid")
        
        # Format string untuk riwayat perhitungan
        operato_math = f"{nmr_1} {operator} {nmr_2} = {hasil}"
        # Menyimpan perhitungan ke dalam list riwayat
        riwayat.append(operato_math)
    
    # Exception handling untuk pembagian dengan nol
    except ZeroDivisionError:
        print("Error: tidak bisa dibagi dengan nol")

    # Meminta input apakah pengguna ingin melanjutkan perhitungan
    lanjut = input("hitung lagi y/n: ").lower()
    # Jika pengguna memilih 'n', keluar dari loop
    if lanjut == "n":
        break

# Menampilkan semua riwayat perhitungan setelah pengguna selesai
print("\nRiwayat Perhitungan:")
# Loop melalui setiap entri dalam riwayat dan menampilkannya
for each in riwayat:
    print(each)