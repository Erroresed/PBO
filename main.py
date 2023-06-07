pengambilan_produk = 1020000
jumlah_kendaraan = 6

if pengambilan_produk >= 1000000:
    if jumlah_kendaraan > 8:
        print("Anda memenuhi syarat menjadi distributor di daerah ini.")
    else:
        print("Jumlah kendaraan Anda tidak mencukupi.")
else:
    print("Pengambilan produk Anda kurang dari minimum yang dibutuhkan.")