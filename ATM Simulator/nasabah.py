class Nasabah:
    def __init__(self, nomor_rekening, nama, pin, saldo):
        self.nmr_rekening = nomor_rekening
        self.name = nama
        self.pin = pin
        self.deposit = saldo

    def cek_saldo(self):
        print(f"this your deposit {self.deposit}")
