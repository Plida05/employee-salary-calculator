# Input dari pengguna
golongan = input("Masukkan Golongan Karyawan (A/B/C): ").upper()
jam_lembur = int(input("Masukkan Jumlah Jam Lembur: "))

# Tentukan gaji pokok
if golongan == 'A':
    gaji_pokok = 5000000
elif golongan == 'B':
    gaji_pokok = 6500000
elif golongan == 'C':
    gaji_pokok = 9500000
else:
    print("Golongan tidak valid.")
    exit()

# Hitung gaji lembur
if jam_lembur == 1:
    gaji_lembur = 0.30 * gaji_pokok
elif jam_lembur == 2:
    gaji_lembur = 0.32 * gaji_pokok
elif jam_lembur == 3:
    gaji_lembur = 0.34 * gaji_pokok
elif jam_lembur == 4:
    gaji_lembur = 0.36 * gaji_pokok
elif jam_lembur >= 5:
    gaji_lembur = 0.38 * gaji_pokok
else:
    gaji_lembur = 0

# Hitung total penghasilan
total_gaji = gaji_pokok + gaji_lembur

# Tampilkan hasil
print("\n===== HASIL PERHITUNGAN =====")
print("Golongan Karyawan   :", golongan)
print("Gaji Pokok          : Rp {:,.0f}".format(gaji_pokok))
print("Gaji Lembur         : Rp {:,.0f}".format(gaji_lembur))
print("Total Penghasilan   : Rp {:,.0f}".format(total_gaji))
