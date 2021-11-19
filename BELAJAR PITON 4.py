while True:
    fname = input('Nama file input: ')

    try:
        fread = open(fname)
        break
    except:
        print('Tidak dapat menemukan file yang dimaksud, tolong cek lagi.\nNama file input: ')

nama = []
for line in fread:
    nama.append(line.strip())
#Program di atas bisa dimodifikasi sehingga yang dihitung hanyalah baris yang tidak kosong (.strip() menghapus semua karakter spasi dan \n di kiri-kanan string):
nama = sorted(nama)

fwrite = open('output_' + fname, 'w')

for item in nama:
    fwrite.write(item + '\n')

fwrite = open('output_'+ fname,'r')
print(fwrite.read())
fwrite.close()

#OPEN FILE MENGHITUN JUMLAH BARIS
# fread = open('output-segitiga.txt')
# count = 0
# for line in fread:
#     count += 1
#
# print(count)

#MENGHAPUS KARAKTER SPASI DARI ATAS BAWAH STRING
# fread = open('output-segitiga.txt')
#
# count = 0
# for line in fread:
#     if  len(line.strip()) > 0 :
#         count += 1
# print(count)

# MENBUAT FILE BARU

# fwrite = open('output-segitiga.txt', 'w')
#
# n = 1
# for i in range(2, 50):
#     n += i
#     fwrite.write(str(n) + '\n')
#
# fwrite.close()

# membaca file

# file = open("data.txt","w")
# file.write("ini contoh \n")
# file.write("baris pertama\n")
# file.write("baris kedua\n")
# file.write("baris ketiga\n")
# file.close()
#
# file2 = open("data.txt","r")
# print(file2.read())
# print("\n")
# print(file2.read(2),"\n")
# print(file2.readline())
#
# print(file2.readline())
# file2.close()

# appending mode

# file3 = open("data.txt", "a")
# file3.write("\n ini data dengan appending ")
# file3.close()

#  ‘r’  Membuka file untuk dibaca. (default) // read mode
# • ‘w’ Membuka file untuk ditulis. Membuat file baru jika file belum tersedia atau  menimpa isi file jika file sudah ada // write mode
# • ‘x’ Membuka file untuk pembuatan eksklusif. Jika file sudah ada, maka operasi akan gagal // exclusive mode
# • ‘a’ Membuka file dan menambahkan karakter di ujung file lama (tanpa menghapus isinya). Membuat file baru bila file belum tersedia // appending mode
# • ‘t’ Membuka dalam mode teks. (default) // text mode
# • ‘b’ Membuka file dalam mode biner // binary mode
# • ‘r+’ Membuka file untuk diupdate (membaca dan menulis) // write and read mode