data_mahasiswa = []

while True:
    nama = (input("Nama: "))
    nim =  (input("Nim: "))
    nilai_tugas = float(input("Nilai tugas: "))
    nilai_uts = float(input("Nilai UTS: "))
    nilai_uas = float(input("Nilai UAS: "))

    nilai_akhir = (nilai_tugas * 0.30) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

    data_mahasiswa.append([nama,nim,nilai_tugas,nilai_uts,nilai_uas,nilai_akhir])
    
    a = (input("Tambah data(y/t)?:"))
    if a.lower() == "t":
        break
    print()

print("=" * 72)
print("| No |    Nama    |  Nim  | Tugas | UTS | UAS | Akhir |")    
print("=" * 72)

no = 1
for mhs in data_mahasiswa:
    print(f"| {no:<2} | {mhs[0]:<9} | {mhs[1]:<7} | {mhs[2]:<5} | {mhs[3]:<3} | {mhs[4]:<3} | {mhs[5]:<6.2f} |")
    no += 1

print("="*72)



    


