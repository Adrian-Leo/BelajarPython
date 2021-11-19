# LIST TUPLE DAN DICTIONARY

sebuah_list = ["NAP","SE","ISA"]
sebuah_tuple = (1,2,3,4,5)
sebuah_dictionary = {"Nama " : "Leo", "Alamat" : "vilbin" , "NO-TELPON" : "0912292"}

print(sebuah_list)
print(sebuah_list[1])
print(sebuah_dictionary["Alamat"])
print(sebuah_dictionary.get('Nama'))

# mengakses beberapa elemen


print("=========")
print(sebuah_list[0:2])
print(sebuah_tuple[0:3])

# menggunakan loop

for x in sebuah_list :
    print(x)

for y in sebuah_tuple :
    print(y)

for z in sebuah_dictionary :
    print(z ,':' ,sebuah_dictionary[z])

# UPDATE ELEMEN

sebuah_list [1] = "data diganti"
print(sebuah_list)
sebuah_dictionary["NO-TELPON"] = "data berubah"
print(sebuah_dictionary)
# tuple tidak dapat diubah elemennya

# ADDING ELEMEN
print("=============")
print(sebuah_list)
list_baru = sebuah_list + ["teknik komputer"]
print(list_baru)
print(sebuah_tuple)
tuple_baru = sebuah_tuple + (6,7,8)
print(tuple_baru)
print(sebuah_dictionary)
dictionary_baru = {"website " : "google.com"}
sebuah_dictionary.update(dictionary_baru)
print(sebuah_dictionary)
# DELETE ELEMEN

print("= " * 10)
print(list_baru)
del list_baru [1]
print(list_baru)
del sebuah_dictionary["Alamat"]
print(sebuah_dictionary)

# mengetahui panjang elemen
print("="*10)
print("panjang list : ", len(sebuah_list))
print("panjang tuple : ",len(sebuah_tuple))
print("panjang dict : ",len(sebuah_dictionary),"\n")

# strukdat menjadi string

print ("mengubah list, tuple, dictionary menjadi string : \n")
print (str(sebuah_list), ' memiliki panjang karakter :', len(str(sebuah_list)))
print (str(sebuah_tuple), ' memiliki panjang karakter:' ,   len(str(sebuah_tuple)))
print (str(sebuah_dictionary), ' memiliki panjang karakter : ', len(str(sebuah_dictionary)))

# mencari nilai max dan min
print("mencari nilai max dan min : \n")
print("coba periksa sebuah_list :")
print("max : ", max(sebuah_list))
print("min : ", min(sebuah_list))
print("\n")

print("coba periksa sebuah_tuple :")
print("max : ", max(sebuah_tuple))

print("min : ", min(sebuah_tuple))
print("\n")

print("coba periksa sebuah_dictionary :")
print("max : ", max(sebuah_dictionary))
print("min : ", min(sebuah_dictionary))
print("\n")

# mengubah list ke tuple dan sebaliknya
print ("mengubah list ke tuple : ")
print("semula : ", sebuah_list)
print("menjadi : ", tuple(sebuah_list))
print("\n")

print("mengubah tuple ke list : ")
print("semula : ", sebuah_tuple)
print("menjadi : ", list(sebuah_tuple))

