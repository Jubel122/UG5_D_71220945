while True:
    jarak_awal = input("Masukkan jarak awal dalam meter: ")
    if jarak_awal.lower() == "berhenti" or jarak_awal.lower() == "stop":
        break
    sudut_elevasi_pertama = input("Masukkan sudut elevasi pada menit ke-5(dalam derajat): ")
    sudut_elevasi_kedua = input("Masukkan sudut elevasi pada menit ke-6(dalam derajat): ")
    
    tinggi_awal = float(jarak_awal) * math.tan(math.radians(float(sudut_elevasi_pertama)))
    jarak_akhir = float(jarak_awal) * math.tan(math.radians(float(sudut_elevasi_kedua))) - math.tan(math.radians(float(sudut_elevasi_pertama)))
    selisih_ketinggian = jarak_akhir * math.tan(math.radians(float(sudut_elevasi_kedua)))
    
    print("Tinggi helikopter awal: {:.2f}".format(tinggi_awal))