## CALCULATOR SIMPLE

def Calculator():
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (x)")
    print("4. Bagi (:)")
    input_calculator = int(input("Masukan pilihan : "))


    if input_calculator == 1:
        Tambah()
    elif input_calculator == 2:
        Kurang()
    elif input_calculator == 3:
        Kali()
    elif input_calculator == 4:
        Bagi()
    else :
        print("Input salah!")
        Ulang()

## PENJUMLAHAN
def Tambah():
    print("1.Tambah")
    a1 = int(input("Masukan angka pertama :"))
    a2 = int(input("Masukan angka kedua : "))
    hasil = a1 + a2
    print("", a1, "+", "", a2, "= ", hasil)
    Ulang()

def Kurang():
    print("2.Kurang")
    a1 = int(input("Masukan angka pertama :"))
    a2 = int(input("Masukan angka kedua : "))
    hasil = a1 + a2
    print("", a1, "-", "", a2, "= ", hasil)
    Ulang()

def Kali():
    print("3.Kali")
    a1 = int(input("Masukan angka pertama :"))
    a2 = int(input("Masukan angka kedua : "))
    hasil = a1 * a2
    print("", a1, "*", "", a2, "= ", hasil)
    Ulang()

def Bagi():
    print("4.Bagi")
    a1 = int(input("Masukan angka pertama :"))
    a2 = int(input("Masukan angka kedua : "))
    hasil = a1 / a2
    print("", a1, "/", "", a2, "= ", hasil)
    Ulang()

def Ulang():
    u1 = input("Apakah anda ingin mengulang? (Y/N) :")
    if u1 == "Y" or u1 == "y":
        Calculator()
    elif u1 == "N" or u1 == "n":
        print("Terimakasih")
    else :
        print("Input salah!")
        Ulang()


## OPSI CALCULATOR
Calculator()
