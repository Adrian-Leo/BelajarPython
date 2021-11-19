# hobi = []
# stop = False
# i = 0
#
# # Mengisi hobi
# while (not stop):
#     hobi_baru = input("Inputkan hobi yang ke-{}: ".format(i))
#     hobi.append(hobi_baru)
#
#     # Increment i
#     i += 1
#
#     tanya = input("Mau isi lagi? (y/t): ")
#     if (tanya == "t"):
#         stop = True
#
# # Cetak Semua Hobi
# print ("=" * 10)
# print ("Kamu memiliki {} hobi".format(len(hobi)))
# for hb in hobi:
#     print("- {}".format(hb))

# for while
# i = 0
# n1 = input("masukan nama : ")
# n2 = input("masukan nama : ")
# n3 = input("masukan nama : ")
# nama = [n1,n2,n2]
#
# for item in nama :
#     i += 1
#     print("ini nama ke - {}".format(i), item)
# print("ini input ke 2 : ", nama[1] )

# a = 0
# while a < 10 :
#     print("nilai ke -",a)
#     a += 1

# EXEPTION ZERO DIVISON ERROR

try :
    a =int (input("masukan x : "))
    b = int (input("masukan y : "))
    hasil = a / b
    print("hasil = ", hasil)
except ZeroDivisionError :
    print("pembagi tidak boleh nol ")

# EXEPTION INDEX ERROR
try :
    list = [1,2,3,4]
    print(list[4])
except IndexError :
    print("index tidak ditemukan ")

# EXEPTION KEY ERROR = DICTIONARY TIDAK SESUAI
# EXEPTION NAME ERROR = CEK EKSITENSI NAMA VARIABEL
# EXEPTION TYPE ERROR = TIPE DATA TIDAK SESUAI ATAU OPERASI SALAH
# EXEPTION VALUE ERROR = VALUE TIDAK SESUAI DENGAN TIPE DATA