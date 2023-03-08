 
# nama_hari = ("senin, selasa, rabu, kamis, jumat, sabtu, minggu")

# i = 0
# while i < len(nama_hari):
#   print(nama_hari[i])
#   i += 1

# pilih = input("silahkan masukkan hari yang ingin anda telusuri: ").lower()
# if pilih == 'senin':
#     sesi1 = ""
#     sesi2 = "sesi-2 : NgasdosPrakAlPro"
#     sesi3 = "sesi-3 :muaythai"
#     sesi4 = ""
#     sesi5 = ""
#     sesi6 = ""
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)
# elif pilih== 'selasa':
#     sesi1 =  'sesi-1 :kelas artificial intelligence'
#     sesi2 = 'sesi-2 :Kelas RPLBO'
#     sesi3 = 'sesi-3 :kelas progweb'
#     sesi4 = 'sesi-4 :ngerjain tugas progweb'
#     sesi5 = ' sesi-5:bikin soal UG PRAKALPRO'
#     sesi6 = ' sesi-6 :seminar cyber security'
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)

# elif pilih == 'rabu':   
#     sesi1 =   'sesi-1 :KelasPrakRPLBO'
#     sesi2= 'sesi-2 :KelasPrakProgWeb'
#     sesi3 = 'sesi-3 :KelasPendidikanPancasila'
#     sesi4 = 'sesi 4:Kelas EtProf'
#     sesi5 = 'sesi 5:ngasdos PrakAlPro'
#     sesi6 = 'sesi 6:Ngerjain Tugas Keamanan komputer'
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)
# elif pilih == 'kamis':   
#     sesi1 =   'sesi-1 :Kelas Keamanan Komputer'
#     sesi2= ''
#     sesi3 = 'sesi-3 :Ngasdos PrakJarkom'
#     sesi4 = ''
#     sesi5 = ''
#     sesi6 = ''  
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)
# elif pilih == 'Jumat':   
#     sesi1 =   'sesi-1 : KelasPrakRPLBO'
#     sesi2= ''
#     sesi3 = 'sesi-2 :MengoreksiUnguidedPrakAlPro'
#     sesi4 = 'sesi-3 :Mengoreksi Tugas PrakJarkom'
#     sesi5 = 'sesi-4 :MuayThai'
#     sesi6 = ''
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)
# elif pilih == 'Jumat':   
#     sesi1 =   ''
#     sesi2= 'PhotoShoot'
#     sesi3 = ''
#     sesi4 = 'Muaythai'
#     sesi5 = ''
#     sesi6 = ''    
#     print(sesi1)
#     print(sesi2)
#     print(sesi3)
#     print(sesi4)
#     print(sesi5)
#     print(sesi6)              

# if pilih == 'minggu': 
#     print ("input yang anda masukkan tidak valid")

    

def ganti_kata(kalimat, cari, ganti):
    kata = kalimat.split()
    for i in range(len(kata)):
        if kata[i] == cari:
            kata[i] = ganti
    kalimat_baru = ' '.join(kata)
    return kalimat_baru

    