# Menerima input nilai tugas dan ujian dari pengguna
nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

# Memeriksa apakah nilai tugas dan nilai ujian memenuhi kriteria kelulusan
if nilai_tugas > 70 and nilai_ujian > 60:
    hasil = "Lulus"
else:
    hasil = "Gagal"

# Mencetak hasil kelulusan
print("Hasil: Siswa", hasil)
