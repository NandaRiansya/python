while True:
    nama_siswa = input ("masukan nama anda : ")
    nilai_harian = float (input("masukan nilai anda :"))
    nilai_uts = float (input("masukan nilai uts :"))
    nilai_uas = float (input("masukan nilai uas :"))
    nilai_akhir = float (((nilai_harian*40)/100)+((nilai_uts*30)/100)+((nilai_uas*30)/100))

    if nilai_akhir >=80:
        predikat_nilai= 'A'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=70:
        predikat_nilai= 'B'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=60:
        predikat_nilai= 'C'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=50:
        predikat_nilai= 'D'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    else:
        predikat_nilai= 'E'
        print("nama lengkap anda =  ", nama_siswa)
        print("nilai akhir anda =", nilai_akhir)
        print("predikat anda = ", predikat_nilai)
    