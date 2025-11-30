from connect_mysql import  db,cursor
from  fitur_tambahdata import  tambah_mahasiswa
from  fitur_hapusdata import hapus_mahasiswa
from  fitur_lihatdata import lihat_mahasiswa
from  fitur_updatedata import update_mahasiswa

def app():
    while True:
        print("--- SELAMAT DATANG DIMANAJEMEN DATA MAHASISWA 1 TI A")

        menu = int(input("1. Tambah data\n2. hapus data\n3. lihat data\n4. update data\n5. keluar\npilihan: "))
        match menu:
            case 1:
                tambah_mahasiswa()
            case 2:
                hapus_mahasiswa()
            case 3:
                lihat_mahasiswa()
            case 4:
                update_mahasiswa()
            case 5:
                cursor.close()
                return False
            case _:
                print("Mohon input kembali")



if __name__ == "__main__":
    if db.is_connected():
        print("Koneksi ke Database Berhasil")
        app()