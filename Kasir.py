menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang di Resto Starbox")
    print(" List Menu Restoran")
 
    print(" ========================================")
    print(" 1. Ayam Geprek Sambal : Rp 13.000")
    print(" 2. Nasi Goreng Kambing : Rp 17.000")
    print(" 3. Sate Ayam : Rp 20.000")
    print(" 4. Daging Rendang + Nasi : Rp 16.000")
    print(" 5. Pecel Lele Goreng + Nasi : Rp. 17.000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Ayam Geprek Sambal"
        harga=(13000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= " Nasi Goreng Kambing"
        harga = (17000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= " Sate Ayam"
        harga=int(20000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= " Daging Rendang + Nasi"
        harga=int(16000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= " Pecel Lele Goreng + Nasi"
        harga=int(17000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")