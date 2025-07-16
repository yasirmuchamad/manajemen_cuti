# Manajemen Cuti – Sistem Informasi Manajemen Cuti Karyawan

Manajemen Cuti adalah aplikasi web berbasis Django untuk mencatat permohonan cuti oleh karyawan. Sistem ini dilengkapi fitur validasi sisa cuti, approval atau reject oleh admin, dan pembatalan pengajuan.

## Fitur
- Login & otorisasi user
- Daftar Permohonan cuti dan manajemen sisa cuti
- Pengajuan cuti (oleh user)
- Persetujuan pengajuan (oleh admin)
- Pembatalan cuti (oleh admin)
- Validasi sisa cuti (oleh admin)
- Daftar cuti per user (oleh user)


# Teknologi yang digunakan
- Python 3
- Django 5
- SQLite3
- HTML (template bawaan Django)


## Menjalankan Aplikasi (Development)
1. Clone repository ini:
   - https://github.com/yasirmuchamad/manajemen_cuti.git
3. Install virtual environment & dependencies:
   - python -m venv venv
   - unix: source venv/bin/activate / Windows: venv\Scripts\activate
   - pip install -r requirements.txt
4. Migrasi database:
    - python manage.py makemigrations
    - python menage.py migrate
6. Jalankan server:
   - python manage.py runserver

8. Akses di browser: `http://127.0.0.1:8000/`
## Akun Login
- Admin
  - Username: admin
  - Password: admin123
- User biasa
  - Username: user
  - Password: user123

## Lisensi
Proyek ini bebas digunakan untuk keperluan belajar dan portofolio pribadi.

## Penulis
Muchamad Yasir – [GitHub](https://github.com/yasirmuchamad)

