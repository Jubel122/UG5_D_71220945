
def hitung_mobil():
   
    jumlahSol = 0
    jumlahsura = 0
    jumlahJog = 0
    jumlahMag = 0
    
    while True:
        asal = int(input("Masukkan asal mobil (Solo, Surabaya, Jogja, Magelang) atau ketik 'done' untuk selesai: "))
        if asal.lower() == "done":
            break
        
       
        if asal.capitalize() == "Solo":
            jumlahSol += 1
        elif asal.capitalize() == "Surabaya":
            jumlahsura += 1
        elif asal.capitalize() == "Jogja":
            jumlahJog += 1
        elif asal.capitalize() == "Magelang":
            jumlahMag += 1
        else:
            print("Asal mobil tidak valid.")
    
    hitung_mobil()

    print("Jumlah mobil dari Solo: ", jumlahSol)
    print("Jumlah mobil dari Surabaya: ", jumlahsura)
    print("Jumlah mobil dari Jogja: ", jumlahJog)
    print("Jumlah mobil dari Magelang: ", jumlahMag)
        
