# menu
def menu_item():
    print('1. Karpet')
    print('2. Jaket')
    print('3. Kemeja/Kaos/Celana')


def menu_metode():
    print('1. Regular')
    print('2. Deep Clean')


def menu_durasi():
    print('1. Langsung Ready')
    print('2. 1 Hari')
    print('3. 1-2 Hari')


def menu_minum():
    print('1. Coca Cola')
    print('2. Cappuccino')
    print('3. Lemon Tea')


def l():
    print('=========== Laundry Radiant ==========')


def data():
    nama = input('Nama \t: ')
    alamat = input('Alamat \t: ')
    nohp = input('No HP \t: ')


class laundry:
    totalharga = 0

    def __init__(self, item, metode, berat, durasi, lokasi, minum):
        self.item = item
        self.metode = metode
        self.berat = berat
        self.durasi = durasi
        self.lokasi = lokasi
        self.minum = minum

    def item(self):
        if item == 1:
            item = 5000

        elif item == 2:
            item = 3000

        elif item == 3:
            item = 2000

        else:

            print('Input Salah !')

        print('harga : ', self.item)

    def metode(self):
        i = 0
        while i != 1:
            if metode == 1:
                metode = 5000

            elif metode == 2:
                metode = 10000

            else:
                i += 1
                print('Input Salah !')

    def durasi(self):
        if durasi == 1:
            durasi = 10000
        elif durasi == 2:
            durasi = 7000
        elif durasi == 3:
            durasi = 5000

    def lokasi(self):
        if lokasi >= 1 and lokasi <= 5:
            lokasi = 5000
        else:
            lokasi = 10000

    def minum(self):
        if minum == 1:
            minum = 3000
        elif minum == 2:
            minum = 20000
        elif minum == 3:
            minum = 5000

    def totalharga(self):

        totalharga = ((self.item + self.lokasi) * self.berat) + (self.metode + self.durasi + self.minus)

    def tampilkan(self):

        l()
        data()
        print('HARGA TOTAL = ', totalharga)


l()
data()
menu_item()
item = int(input('Pilih item \t: '))
menu_metode()
metode = int(input('Pilih metode \t: '))
berat = int(input('Berat (kg) \t:'))
menu_durasi()
durasi = int(input('Pilih durasi \t: '))
lokasi = 0
minum =1
if durasi == 1:
    n = input('Pesan Minum ? (Y/N) : ')
    if n == 'Y' or 'y':
        menu_minum()
        minum = int(input('Pilih minum \t: '))
    else:
        minum = 0

if durasi == 2:
    antar = input('Antar ? (Y/N) : ')
    if antar == 'Y' or 'y':
        lokasi = int(input('Masukan Jarak (km) : '))

    else:
        lokasi = 0

tes=laundry(item,metode,berat,durasi,lokasi,minum)


# obj.item()
# obj.metode()
# obj.berat()
# obj.durasi()
# obj.lokasi()
# obj.minum()
# obj.totalharga()
# obj.tampilkan()


