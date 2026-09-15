produk = {
    "nama": "ayam geprek",
    "harga": 7000,
    "stok": 10
}

print("Data Produk:")
print(produk)


while True:
    print("\n=== MENU DATA PRODUK ===")
    print("1. Tampilkan Data")
    print("2. Tambah Kategori")
    print("3. Ubah Harga")
    print("4. Hapus Kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Nama:", produk["nama"])
        print("Harga:", produk["harga"])
        print("Stok:", produk["stok"])

        if "kategori" in produk:
            print("Kategori:", produk["kategori"])


    elif pilihan == "2":
        produk["kategori"] = "Makanan"

        print("Setelah Add:")
        print(produk)

    elif pilihan == "3":
        produk.update({"harga": 8000})

        print("Setelah Update:")
        print(produk)

    elif pilihan == "4":
        if  "kategori" in produk:
            produk.pop("kategori")

        print("Setelah Delete:")
        print(produk)

    elif pilihan == "5":
        print("\nData Produk Setelah Perubahan:")
        print(produk)
        print("Program selesai.")
        break


    else:
        print("Pilihan tidak tersedia.")