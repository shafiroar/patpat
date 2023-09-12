## Nama    : Shafira Nurrohmah
## NPM     : 2206030035
## Kelas   : PBP C
## Link Aplikasi : https://patpat.adaptable.app/main/

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : 
- Hal pertama yang saya lakukan adalah membuat direktori dan repositori baru di local file dan juga di akun GitHub
- Selanjutnya membuat dan menggabungkan branch menggunakan pull request
- Membuat virtual environment `source env/bin/activate` pada terminal di IDLE VSCODE
- Selanjutnya, buat file requirements.txt dan isinya berisi daftar dependensi yang diperlukan, kemudian lakukan instalasi dengan perintah `pip3 install -r requirements.txt`.
- Inisialisasikan proyek Django dengan menjalankan perintah `django-admin startproject patpat`.
- Dalam file settings.py, tambahkan `"*"` ke dalam daftar `ALLOWED_HOSTS` dan buat berkas `.gitignore`.
- Buat aplikasi baru dengan perintah `python3 manage.py startapp main`.
- Membuat folder `templates` di dalam `main` dan menambahkan `main.html` didalamnya
- Di dalam direktori main, buat folder `templates` dan tambahkan berkas `main.html` di dalamnya.
- Konfigurasikan rute URL dengan menambahkan `path('main/', include('main.urls'))` di berkas `urls.py` dalam proyek `patpat`.
- Definisikan model bernama `product` dalam aplikasi main yang memiliki atribut seperti `name`, `price`, `description`, `pet`.
- Buat fungsi `show_main` dalam berkas `views.py`yang menyertakan konteks seperti app, name, dan class. Kemudian, render konteks ini ke dalam berkas `main.html`.
- Membuat `urls.py` pada `main` dan menambahkan ` app_name = 'main' `. Add `path('', show_main, name='show_main')` pada list `urlpatterns`.
- Terakhir, lakukan deploy aplikasi web ke Adaptable dan lakukan operasi add, commit, dan push ke repositori GitHub.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab : 

<img src="/image/graphs.jpg">

Penjelasan :

Anggap saja ada seorang klien yang melakukan tindakan tertentu di sebuah situs yang menggunakan Django. Saat itu, peramban klien akan mengirimkan permintaan HTTP ke server situs tersebut, dan permintaan ini akan ditangani oleh berkas `urls.py` untuk mencari pola URL yang diminta oleh klien. Setelah itu, framework Django akan menggunakan berkas `views.py` untuk melakukan pemrosesan dan operasi logika terhadap data yang terdapat dalam berkas `models.py`. Setelah proses pemrosesan data selesai, berkas `views.py` akan mengirimkan berkas HTML yang terdapat dalam direktori `templates` kepada klien. Selanjutnya, peramban klien akan melakukan proses penyusunan ulang (rendering) berkas HTML ini sebagai tanggapan HTTP yang diterimanya.
 
### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab :

Kita menggunakan virtual environment dalam pengembangan aplikasi web berbasis Django karena:
1. Isolasi Dependensi: Virtual environment memungkinkan kita untuk mengisolasi dependensi dan paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah dependensi.
2. Manajemen Versi Python: Dengan virtual environment, kita dapat menggunakan versi Python yang berbeda untuk setiap proyek, memberikan fleksibilitas dalam penggunaan versi Python yang sesuai.
3. Keamanan Proyek: Penggunaan virtual environment menjaga keamanan proyek dengan menghindari perubahan paket sistem Python yang dapat memengaruhi stabilitas atau keamanan sistem.
4. Portabilitas: Virtual environment memungkinkan proyek Python untuk tetap portabel, mudah dibagi dengan orang lain, atau dipindahkan ke server lain tanpa masalah.
Meskipun mungkin memungkinkan untuk membuat aplikasi web Django tanpa virtual environment, sebaiknya selalu menggunakan virtual environment untuk menjaga kebersihan, keamanan, dan manajemen dependensi yang efisien dalam pengembangan aplikasi Python.


### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab : 
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga konsep arsitektur perangkat lunak yang berfokus pada pemisahan tanggung jawab dalam pengembangan aplikasi. Berikut penjelasan singkat tentang masing-masing konsep dan perbedaannya:

1. **MVC (Model-View-Controller)**:
   - **Model**: Bertanggung jawab untuk mengelola data dan logika bisnis aplikasi.
   - **View**: Bertanggung jawab untuk menampilkan data kepada pengguna dan mengatur tampilan.
   - **Controller**: Bertanggung jawab untuk mengatur interaksi antara Model dan View serta mengendalikan alur aplikasi.

   **Perbedaan Utama**:
   - MVC adalah konsep yang umum digunakan dalam pengembangan perangkat lunak berbasis desktop dan web.
   - Controller berperan sebagai perantara antara Model dan View.
   - Penggunaan pengontrol (Controller) untuk mengatur alur aplikasi.

2. **MVT (Model-View-Template)**:
   - **Model**: Bertanggung jawab untuk mengelola data dan logika aplikasi, mirip dengan Model dalam MVC.
   - **View**: Bertanggung jawab untuk menampilkan data kepada pengguna, mirip dengan View dalam MVC.
   - **Template**: Bertanggung jawab untuk mengatur tampilan dan menggabungkan data dari Model untuk disajikan kepada pengguna.

   **Perbedaan Utama**:
   - MVT adalah konsep yang khusus digunakan dalam framework web Django, yang terkait dengan Python.
   - Template digunakan untuk merancang tampilan dan memisahkan kode HTML dari logika aplikasi.

3. **MVVM (Model-View-ViewModel)**:
   - **Model**: Mirip dengan Model dalam MVC dan MVT, mengelola data dan logika bisnis.
   - **View**: Mirip dengan View dalam MVC dan MVT, menampilkan data kepada pengguna.
   - **ViewModel**: Bertanggung jawab untuk menghubungkan Model dan View, serta mengatur tampilan data untuk ditampilkan di View.

   **Perbedaan Utama**:
   - MVVM adalah konsep yang sering digunakan dalam pengembangan aplikasi berbasis aplikasi seluler dan desktop.
   - ViewModel berfungsi sebagai perantara antara Model dan View, tetapi ViewModel memiliki lebih banyak kontrol atas tampilan data yang disajikan.

Perbedaan antara ketiganya terutama terletak pada bagaimana tanggung jawab dan peran masing-masing komponen diatur dan dipisahkan. MVC adalah konsep yang lebih umum digunakan dalam pengembangan web tradisional, sedangkan MVT khusus untuk Django, dan MVVM sering digunakan dalam aplikasi seluler dan desktop modern. Pilihan tergantung pada teknologi yang digunakan dan kebutuhan proyek pengembangan perangkat lunak.