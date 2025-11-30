from art_calculator import logo_calculator
import os


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponents(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

math_key = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "**":exponents,
    "%":modulo
}

def calculator():
    print(logo_calculator)
    began = True
    number_first = float(input("what's the first number: "))

    while began:

        for simbol in math_key:
            print(simbol)
        operasi = input("pick an operation: ")
        number_second = float(input("what's the next number: "))

        hasil = math_key[operasi](n1=number_first, n2=number_second)
        print(f"{number_first} {operasi} {number_second} = {hasil}")

        jalan_tidak = input(f"type 'y' to continue calculating {hasil}, or type 'n' to start a new calculation, or type 'x' to close the calculator: ")
        if jalan_tidak == "y":
            number_first = hasil

        elif jalan_tidak == "n":
            began =  False
            os.system("clear")
            calculator()
        elif jalan_tidak == "x":
            began = False
            os.system('clear')
calculator()




