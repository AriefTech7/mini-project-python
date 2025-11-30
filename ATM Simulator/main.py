from nasabah import Nasabah
from data import data_nasabah

nasabah = Nasabah()

main_key = input("berikan main key kamu: ")

print(nasabah.cek_saldo(data_nasabah[main_key]["nasabah"]))