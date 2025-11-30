class ATM:
    def __init__(self):
        # Inisialisasi saldo awal menjadi 0
        self.saldo = 0

    def liat_saldo(self):
        # Fungsi untuk melihat saldo
        # Mengembalikan string yang berisi informasi saldo
        return f"\njumlah saldo: ${self.saldo}\n"

    def deposit(self, jumlah):
        # Fungsi untuk melakukan deposit
        # Menambahkan jumlah deposit ke saldo
        self.saldo += jumlah
        return f"\nBerhasil deposit: ${jumlah}\n"

    def tarik(self, jumlah):
        # Fungsi untuk menarik uang
        # Memeriksa apakah saldo mencukupi sebelum menarik
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            return f"\nBerhasil tarik: ${jumlah}\n"
        else:
            return "\nSaldo tidak cukup\n"