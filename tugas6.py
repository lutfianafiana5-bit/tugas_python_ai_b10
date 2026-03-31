import numpy as np
import pandas as pd
import os

np.random.seed(42)
nilai_array = np.random.randint(50, 100, 12)

rata_rata = np.mean(nilai_array)
median = np.median(nilai_array)
std_dev = np.std(nilai_array)
nilai_min = np.min(nilai_array)
nilai_max = np.max(nilai_array)

data = {
    "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "nim": ["101", "102", "103", "104", "105"],
    "nilai": nilai_array[:5]  
}

df = pd.DataFrame(data)

df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

def write_summary_txt(path="ringkasan_tugas6.txt"):
    with open(path, "w") as f:
        f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata   : {rata_rata:.2f}\n")
        f.write(f"Median      : {median:.2f}\n")
        f.write(f"Std Dev     : {std_dev:.2f}\n")
        f.write(f"Nilai Min   : {nilai_min}\n")
        f.write(f"Nilai Max   : {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Data : {len(df)}\n")
        f.write(f"Jumlah Lulus: {(df['status'] == 'LULUS').sum()}\n")
        f.write(f"Tidak Lulus : {(df['status'] == 'TIDAK LULUS').sum()}\n")

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Rata-rata Nilai : {self.average():.2f}\n")
            f.write(f"Pass Rate       : {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook: jumlah data = {len(self.df)}, rata-rata = {self.average():.2f}"

if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Data Nilai :", nilai_array)
    print("Rata-rata  :", rata_rata)
    print("Median     :", median)
    print("Std Dev    :", std_dev)
    print("Min        :", nilai_min)
    print("Max        :", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average   :", gb.average())
    print("Pass Rate :", gb.pass_rate(), "%")

    write_summary_txt()
    gb.save_summary("ringkasan_tugas6.txt")

    print("\nFile 'ringkasan_tugas6.txt' berhasil dibuat!")