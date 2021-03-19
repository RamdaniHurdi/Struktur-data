#Nama : Ramdani Hurdi
#NIM    : TI17200040
#Matkul : Struktur Data

hari = ["Senin","Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
for i in range(len(hari)):
    print(i + 1,hari[i])
    if i== 4: 
        print("     hari masuk kuliah")
    elif i == 6:
        print("     Hari libur kuliah")