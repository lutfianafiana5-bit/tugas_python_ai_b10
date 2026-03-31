nama = "Lutfiana"        
umur = 21               
tinggi = 160.5           
is_mahasiswa = True      
hobi = ["membaca", "coding", "menonton", "musik", "traveling"]  

print("=== DATA AWAL ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", is_mahasiswa)
print("Hobi:", hobi)

print("\n=== MANIPULASI STRING ===")

kalimat = "halo dunia python"

print("Gabungan:", "Nama saya " + nama)

print("Panjang kalimat:", len(kalimat))

print("Uppercase:", kalimat.upper())
print("Lowercase:", kalimat.lower())

print("\n=== OPERASI MATEMATIKA ===")

a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi (modulus):", a % b)

print("\n=== LIST ===")

print("List hobi:", hobi)

print("Hobi pertama:", hobi[0])
print("Hobi terakhir:", hobi[-1])

hobi.append("olahraga")
print("Setelah ditambah:", hobi)

hobi.remove("musik")
print("Setelah dihapus:", hobi)

print("\n=== INPUT USER ===")

nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print("\n=== PERKENALAN ===")
print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun.")