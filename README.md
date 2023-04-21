## Nama-nama anggota kelompok:
- Ardian - 2106638173
- I Dewa Putu Aditya Rahman - 2106650456
- Khairinka Rania Lizadhi - 2006597254
- Prudita Victory - 2006486071 
- Anandafa Syukur Rizky - 2106655040
- Muhammad Nabil Mahardika - 2106751871

## Tautan aplikasi Railway
Belum Tersedia

## Cerita aplikasi yang diajukan serta manfaatnya
StudyBee adalah sebuah website aplikasi yang berguna bagi para pelajar dan mahasiswa dalam memudahkan mereka dalam memantau dan mengatur jadwal belajar mereka. Aplikasi ini menawarkan berbagai fitur yang berguna seperti daftar studi, forum diskusi tugas, jadwal semester, kalkulator nilai dan bobot, form diary, dan catatan kelas. Semua fitur tersebut dapat diakses secara online dan gratis.
Dengan menggunakan aplikasi ini, pengguna dapat mengoptimalkan waktu belajar mereka dan meningkatkan prestasi akademik mereka.

## Daftar modul yang akan diimplementasikan
Daftar modul atau fitur-fitur yang akan diimplementasikan pada website StudyBee adalah sebagai berikut:

- Study List: Modul ini akan memungkinkan pengguna untuk mencatat dan mengatur daftar mata pelajaran dan tugas-tugas yang harus mereka selesaikan. Dengan modul ini, pengguna dapat memantau dan mengingatkan diri mereka sendiri tentang tugas-tugas yang harus diselesaikan.

- Forum Diskusi Tugas: Modul ini akan memungkinkan pengguna untuk berdiskusi dengan teman-teman mereka tentang tugas dan proyek tertentu. Hal ini akan membantu pengguna dalam memahami materi pelajaran dan mendapatkan ide-ide baru dari teman-teman mereka.

- Jadwal Semester: Modul ini akan memungkinkan pengguna untuk mengatur jadwal kuliah dan ujian mereka sehingga mereka dapat mengalokasikan waktu belajar mereka secara efisien.

- Kalkulator Nilai (Nilai & bobot): Modul ini akan membantu pengguna dalam menghitung nilai mereka dan bobot tugas mereka. Fitur ini akan membantu pengguna untuk memperkirakan nilai mereka dan memahami bagaimana bobot tugas tertentu dapat mempengaruhi nilai akhir mereka.

- Form Diary : Modul ini memungkinkan pengguna untuk menceritakan keluh kesah suka mau-pun duka dalam kegiatan sehari-harinya

- Class Notes: Modul ini akan memungkinkan pengguna untuk membuat catatan kelas mereka dan memperbaiki pemahaman mereka tentang materi pelajaran.

## Role
- Guest (user yang belum log in): hanya dapat mengakses kalkulator nilai 
- User (Pengguna yang sudah terautentikasi): dapat mengakses semua fitur, kecuali menghapus forum dan komentar dari user lain
- Admin: dapat mengakses semua fitur, termasuk menghapus forum dan komentar user lain

## Tutorial

1. Buka file yang ingin kamu simpan file PBP-KELOMPOK ini, di dalam directory tersebut bukalah terminal dan masukkan dengan perintah:
```
git clone https://github.com/StudyBee-PBP/StudyBee.git
```

2. Di dalam direktori StudyBee, bukalah command prompt atau shell dan buatlah sebuah virtual environment. Virtual environment ini berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputermu. Kamu dapat membuat virtual environment dengan perintah:
```
python -m venv env
```

3. Nyalakan virtual environment yang telah dibuat dengan perintah berikut. Pastikan saat ini kamu sedang berada pada direktori StudyBee yang telah dibuat sebelumnya. Perhatikan pula bahwa Windows dengan Unix memiliki perintah yang berbeda. Apabila virtual environment berhasil dinyalakan, kamu dapat melihat sebuah teks (env) di posisi paling kiri dari baris input shell milikmu.
- Windows 
```
env\Scripts\activate.bat
```
- Unix (Linux & Mac OS)
```
source env/bin/activate
```

4. Instal dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah:
```
pip install -r requirements.txt
```

5. Run pada terminal didalam direktory StudyBee dengan perintah:
```
py manage.py runserver
```

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)