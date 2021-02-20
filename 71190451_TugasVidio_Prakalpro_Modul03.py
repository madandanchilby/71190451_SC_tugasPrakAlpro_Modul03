#Nama:Chilby Madandan
#Nim:71190451
#SOAL
#Buatlah sebuah program yang dapat menampilkan jumlah hari dalam suatu bulan di
# tahun 2020. Program meminta pengguna memasukkan nomor bulan (1-12), kemudian program
# akan menampilkan jumlah hari pada bulan tersebut.
#Sebagai contoh, perhatikan input dan output berikut ini:
#Masukkan bulan (1-12): 7
#Jumlah hari: 31
#Lengkapi program tersebut dengan penanganan kesalahan jika pengguna memasukkan bulan
#yang salah. Penanganan kesalahan dalam bentuk memunculkan pesan bahwa bulan yang
#diinputkan oleh pengguna tersebut tidak valid.
bulan=input('masukan bulan=')
try:
    bulan =int(bulan)
    if bulan == 2:
        print('jumlah hari = 29')
    elif bulan >= 1 and bulan <= 7:
        if bulan % 2 != 0:
            print('jumlah hari =31')
        else:
            print('jumlah hari = 30')
    elif bulan >= 8 and bulan <= 12:
        if bulan % 2 != 0:
            print('jumlah hari = 31')
        else:
            print('jumlah hari = 30')
except:
    print('inputan oleh pengguna tidak valid')