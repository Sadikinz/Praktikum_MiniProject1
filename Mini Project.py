#input untuk LOGIN 
Nama = str(input('Masukkan Nama Kamu: '))
NIM = int(input('Masukkan NIM Kamu: '))

print(f'\nHaloo, {Nama} Selamat Datang!')
print(f'NIM Kamu adalah {NIM}')


while True:
#Input untuk mengetahui Jam kerja dan Tarif kerja karyawan
    jam_kerja = int(input('\nMasukkan total jam kerja karyawan :'))
    gaji_kerja = float(input('Masukkan gaji kerja karyawan Per hari Rp.'))


#Percabangan untuk menentukan Bonus tarif kerja kepada karyawan yang bekerja lebih dari 160 jam
    if jam_kerja > 160:
        bonus = jam_kerja * gaji_kerja * 0.1
        gaji = jam_kerja * gaji_kerja + bonus
    else:
        gaji = jam_kerja*gaji_kerja
        bonus = 0 

#Hasil
    print(f'Total Gaji Karyawan: Rp {gaji:,.2f}')
    if bonus > 0:
        print(f'Bonus karyawan 10% karena jam kerja lebih dari 160, jadi bonusnya adalah Rp {bonus:,.2f} ')
    else:
        print('Tidak ada bonus karena jam kerja tidak lebih dari 160 jam')

#Perulangan untuk memberikan pilihan ingin menghitung gaji lagi atau keluar dari program
    pilihan = input('\nApakah ingin menghitung gaji lagi? (ya/tidak)').strip().lower()
    if pilihan == 'ya':
        continue
    elif pilihan == 'tidak':
        print('Terima kasih dan sampai jumpa!')
        break
    else:
        print('Tidak valid, anda keluar dari program')
        break
