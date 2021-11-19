# x = 10
# y = 7
#
# perkalian = x * y
# pembagian = x / y
# penjumlahan = x + y
# pengurangan = x - y
# sisaBagi = x % y
#
# print (" x = 10 dan y = 5")
# print ("hasil perkalian = ", perkalian)
# print ("hasil pembagian = ", pembagian)
# print ("hasil penjumlahan = ", penjumlahan)
# print ("hasil pengurangan = ", pengurangan)
# print ("hasil modulo = ", sisaBagi)

# user_input = int ( input(" masukan nilai = "))
#
#
# if user_input >= 90 :
#     print("nilai anda  = ",user_input, " --A-- " )
# elif user_input >= 80 and nilai < 90 :
#     print(" nilai anda = ", user_input, " --B--")
#
# else :
#     print("nilai anda  = ",user_input," --C-- ")

# a = True
# b = False
#
# # Logika AND
# c = a and b
# print " %r and %r = %r" % (a,b,c)
# # Logika OR
# c = a or b
# print "%r or %r = %r" % (a,b,c)
#
# # Logika Not
# c = not a
# print "not %r  = %r" % (a,c)


# nama = input( "masukan nama = ")
#
# print("silahkan masuk ", nama)

# file: operator_pembanding.py
# a = input("Inputkan nilai a: ")
# b = input("Inputkan nilai b: ")
#
# # apakah a sama dengan b?
# c = a == b
# print "Apakah %d == %d: %r" % (a,b,c)
#
# # apakah a < b?
# c = a < b
# print "Apakah %d < %d: %r" % (a,b,c)
#
# # apakah a > b?
# c = a > b
# print "Apakah %d > %d: %r" % (a,b,c)
#
# # apakah a <= b?
# c = a <= b
# print "Apakah %d <= %d: %r" % (a,b,c)
#
# # apakah a >= b?
# c = a >= b
# print "Apakah %d >= %d: %r" % (a,b,c)
#
# # apakah a != b?
# c = a != b
# print "Apakah %d != %d: %r" % (a,b,c)

# program untuk mengecek bonus dan diskon
# file: bonus.py

# total_belanja = int (input("Total belanja: Rp "))
#
# # jumlah yang harus dibayar adalah berapa total belanjaannya
# # tapi kalau dapat diskon akan berkurang
# bayar = total_belanja
#
# # jika dia belanja di atas 100rb maka berikan bonus dan diskon
# if total_belanja > 100000:
#     print("Kamu mendapatkan bonus minuman dingin")
#     print("dan diskon 5%")
#
#     # hitung diskonnya
#     diskon = total_belanja * 5/100 #5%
#     bayar = total_belanja - diskon
#
#
# # cetak struk
# print("Total yang harus dibayar: Rp %s" % bayar)
# print("Terima kasih sudah berbelanja")
# print("Datang lagi yaa...")

# a = int ( input("masukan x = "))
# b =  float (input("masukan y = "))
# hasil = a + b
# print("hasil = ", hasil)

a= 0
while a < 10 :
    a += 1 
    print("antrian ke- ",a )
