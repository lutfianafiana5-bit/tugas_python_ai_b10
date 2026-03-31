print("=== LIST ===")

my_list = ["apel", 10, "jeruk", 25, "mangga", 50]
print("List awal:", my_list)
print("Elemen pertama:", my_list[0])
print("Elemen terakhir:", my_list[-1])
print("Slicing [1:5:2]:", my_list[1:5:2])
print("\nSebelum manipulasi:", my_list)

my_list.append("pisang")
my_list.insert(1, "anggur")
my_list.extend([100, "melon"])

print("Setelah append, insert, extend:", my_list)

my_list.pop()
my_list.remove("apel")

print("Setelah pop & remove:", my_list)

print("\n=== TUPLE ===")

my_tuple = ("andi", 20, "jakarta", "informatika", 2022)
print("Tuple:", my_tuple)

print("Panjang tuple:", len(my_tuple))
print("Elemen index ke-2:", my_tuple[2])

nama, umur, kota, *rest = my_tuple
print("Nama:", nama)
print("Umur:", umur)
print("Kota:", kota)
print("Sisa data:", rest)

print("\n=== SET ===")

set1 = {1, 2, 3, 4, 5, 5}
set2 = {4, 5, 6, 7}

print("Set1:", set1)  
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

print("\n=== DICTIONARY ===")

mahasiswa = {
    "nama": "Budi",
    "nim": "12345",
    "angkatan": 2022,
    "kota": "Bandung"
}

print("Data awal:", mahasiswa)
mahasiswa["jurusan"] = "Informatika"
mahasiswa["kota"] = "Jakarta"
del mahasiswa["angkatan"]

print("Data setelah perubahan:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi:")
for k, v in mahasiswa.items():
    print(f"{k} : {v}")

print("\n=== NESTED STRUCTURES ===")

books = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2018},
    {"judul": "AI Modern", "penulis": "Budi", "tahun": 2021},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2019},
    {"judul": "Machine Learning", "penulis": "Dewi", "tahun": 2023},
]

print("Daftar Judul Buku:")
for book in books:
    print("-", book["judul"])

filtered_books = [b for b in books if b["tahun"] >= 2020]
print("\nBuku tahun >= 2020:", filtered_books)

print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

dict_ganjil_genap = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict ganjil/genap:", dict_ganjil_genap)

kalimat = "Belajar Python Itu Menyenangkan"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}
print("Huruf unik:", huruf_unik)

print("\n=== KEANGGOTAAN ===")

if "jeruk" in my_list:
    print("'jeruk' ada di list pada index:", my_list.index("jeruk"))
else:
    print("'jeruk' tidak ditemukan")

if 3 in set1:
    print("3 ada di set1")
else:
    print("3 tidak ada di set1")