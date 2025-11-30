#Program untuk mengelola daftar belanja.

shopping_list = {"shampoo": 2 , "sabun": 3, "snack": 5, "yogurt": 5, "sosis": 5}


def show_list():
    if shopping_list:
        print("\ndafar belanja:")
        for item, quantity in shopping_list.items():
            print(f"- {item}: {quantity}")
    else:
        print("\ndaftar belanja kosong!")

def add_item():
    item = input("masukan nama barang:").strip()
    quantity = int(input(f"masukan jumlah {item}:"))
    shopping_list[item] = shopping_list.get(item, 0) + quantity
    print(f"{item }berhasil ditambahkan")

def remove_item():
    item = input("masukan nama barang yang ingin dihapus:").strip()
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} berhasil dihapus!")
    else:
        print(f"{item} tidak ditemukan didaftar belanja")

while True:
    print("\nmenu:")
    print("1.lihat daftar belanja")
    print("2. tambah barang")
    print("3.hapus barang")
    print("4.keluar")

    choice = input("pilih menu 1/2/3/4: ")
    if choice == "1":
        show_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        print("program selesai. selamat berbelanja!")
        break
    else:
        print("pilihan tidak valid. silahkan coba lagi.")