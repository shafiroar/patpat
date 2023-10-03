## Nama    : Shafira Nurrohmah
## NPM     : 2206030035
## Kelas   : PBP C
## Link Aplikasi : https://patpat.adaptable.app/main/

# Tugas 2
<details>
<summary>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

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
</details>

<details>
<summary>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</summary>
Jawab: 

<img src="/image/graphs.jpg">

Penjelasan:

Anggap saja ada seorang klien yang melakukan tindakan tertentu di sebuah situs yang menggunakan Django. Saat itu, peramban klien akan mengirimkan permintaan HTTP ke server situs tersebut, dan permintaan ini akan ditangani oleh berkas `urls.py` untuk mencari pola URL yang diminta oleh klien. Setelah itu, framework Django akan menggunakan berkas `views.py` untuk melakukan pemrosesan dan operasi logika terhadap data yang terdapat dalam berkas `models.py`. Setelah proses pemrosesan data selesai, berkas `views.py` akan mengirimkan berkas HTML yang terdapat dalam direktori `templates` kepada klien. Selanjutnya, peramban klien akan melakukan proses penyusunan ulang (rendering) berkas HTML ini sebagai tanggapan HTTP yang diterimanya.
 </details>

<details>
<summary>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</summary>

Kita menggunakan virtual environment dalam pengembangan aplikasi web berbasis Django karena:
1. Isolasi Dependensi: Virtual environment memungkinkan kita untuk mengisolasi dependensi dan paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah dependensi.
2. Manajemen Versi Python: Dengan virtual environment, kita dapat menggunakan versi Python yang berbeda untuk setiap proyek, memberikan fleksibilitas dalam penggunaan versi Python yang sesuai.
3. Keamanan Proyek: Penggunaan virtual environment menjaga keamanan proyek dengan menghindari perubahan paket sistem Python yang dapat memengaruhi stabilitas atau keamanan sistem.
4. Portabilitas: Virtual environment memungkinkan proyek Python untuk tetap portabel, mudah dibagi dengan orang lain, atau dipindahkan ke server lain tanpa masalah.
Meskipun mungkin memungkinkan untuk membuat aplikasi web Django tanpa virtual environment, sebaiknya selalu menggunakan virtual environment untuk menjaga kebersihan, keamanan, dan manajemen dependensi yang efisien dalam pengembangan aplikasi Python.
</details>

<details>
<summary>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</summary>

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
</details>

# Tugas 3
<details>
<summary>1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?</summary>

| Perbedaan         |  `POST`                                           | `GET`                                                 |
|-------------------|---------------------------------------------------|-------------------------------------------------------|
| Metode HTTP       | Mengirim data dengan metode POST.                 | Mengirim data dengan metode GET.                      |
| Tampilan URL      | Data tidak tampil dalam URL.                      | Data ditampilkan dalam URL.                           |
| Keamanan          | Lebih aman untuk mengirim data sensitif.          | Kurang aman karena data terlihat dalam URL.           |
| Panjang Data      | Tidak terbatas pada panjang data yang dikirim.    | Terbatas pada panjang URL maksimum                    |
| Cacheable         | Data biasanya tidak di-cache.                     | Data dapat di-cache (oleh proxy server atau browser). |
| Penggunaan        | Mengirim data yang akan diproses oleh server.     | Digunakan untuk mengambil data dari server.           |
| Contoh Penggunaan | Formulir login, pengeposan data sensitif.         | Pengambilan data dari URL (misalnya, pencarian).      |

</details>

<details>
<summary>2. Apa perbedaan utama antara `XML`, `JSON`, dan `HTML` dalam konteks pengiriman data?</summary>

| Perbedaan Utama      | XML                          | JSON                            | HTML                                |
|----------------------|------------------------------|---------------------------------|-------------------------------------|
| Struktur Data        | Menggunakan markup hierarkis  | Berbasis key-value pairs       | Berbasis tag dan elemen             |
| Kemampuan Pemrosesan | Tidak selalu mudah diproses oleh mesin dan manusia | Mudah diproses oleh mesin dan manusia | Dirancang untuk ditampilkan di browser |

</details>

<details>
<summary>3. Mengapa `JSON` sering digunakan dalam pertukaran data antara aplikasi web modern?</summary>

**JSON (JavaScript Object Notation)** sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki sejumlah keunggulan dan karakteristik yang sangat cocok untuk kebutuhan ini:

**Ringkas dan Mudah Dibaca:** JSON menggunakan format teks yang ringkas dan mudah dibaca oleh manusia. Ini membuatnya mudah untuk dipahami dan dianalisis, baik oleh pengembang maupun oleh mesin.

**Bahasa-Agnostik:** JSON adalah format data yang bahasa-agnostik, artinya dapat digunakan dalam berbagai bahasa pemrograman. Ini memungkinkan berbagai aplikasi yang ditulis dalam bahasa yang berbeda untuk berkomunikasi dengan mudah.

**Kemampuan Pemrosesan Mudah:** JSON dapat dengan mudah diproses oleh mesin, termasuk JavaScript di sisi klien dan bahasa pemrograman lain di sisi server. Ini membuatnya ideal untuk pertukaran data antara klien dan server dalam aplikasi web.

**Struktur Data yang Fleksibel:** JSON mendukung struktur data yang fleksibel. Anda dapat menggunakan objek dan array bersarang untuk merepresentasikan data yang kompleks dan terstruktur dengan baik.

**Dukungan untuk Tipe Data Standar:** JSON mendukung tipe data standar seperti string, angka, boolean, array, dan objek. Ini mencakup hampir semua jenis data yang umum digunakan dalam aplikasi web.
</details>

<details>
<summary>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

## Input Form
<details>
<summary>Langkah 1: Buat Struktur Form </summary>
- Buat berkas `forms.py` dalam direktori main untuk membuat struktur form. 
Gunakan kode berikut:

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
</details>

<details>
<summary>Langkah 2: Tambahkan fungsi Views</summary>
- Buka berkas `views.py` dalam direktori main dan tambahkan import yang diperlukan.
Gunakan kode berikut:

```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```

- Tambahkan fungsi create_product untuk menampilkan dan memproses form.
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

</details>

<details>
<summary>Langkah 3: Perbaikin fungsi `show_main`</summary>
- Perbarui fungsi `show_main` dalam `views.py` untuk menampilkan data produk yang ada dengan melanjutkan dari tugas sebelumnya.
</details>

<details>
<summary>Langkah 4: Tambahkan URL</summary>
- Buka berkas `urls.py` dalam direktori `main` dan tambahkan URL untuk akses fungsi `create_product`.

```python
path('create-product', create_product, name='create_product'),
```
</details>

<details>
<summary>Langkah 5: Buat Form HTML</summary>
Buat berkas `create_product.html` dalam direktori `main/templates` dan tambahkan kode form HTML.

```python
{% extends 'base.html' %} 

{% block content %}
<h2>Add New Product</h2>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
</details>

<details>
<summary>Langkah 6: Tampilkan Data pada Halaman Utama</summary>
Perbarui berkas `main.html` dalam direktori `main/templates` untuk menampilkan data produk dalam bentuk tabel dan tombol "Add New Product" yang akan mengarahkan ke halaman form.
</details>

## 5 Fungsi Views
Berikut adalah langkah-langkah singkat untuk menjawab pertanyaan tentang cara menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID dalam Django:

<details>
<summary>Mengembalikan Data dalam Format HTML</summary>

1. Buat fungsi view yang mengambil data produk dalam format HTML.
2. Tambahkan URL untuk mengakses fungsi tersebut.
</details>
<details>
<summary>Mengembalikan Data dalam Format XML</summary>

1. Buat fungsi view yang mengambil data produk dalam format XML.
2. Gunakan serializer untuk mengonversi data ke dalam format XML.
3. Tambahkan URL untuk mengakses fungsi tersebut.

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
</details>
<details>
<summary>Mengembalikan Data dalam Format JSON</summary>

1. Buat fungsi view yang mengambil data produk dalam format JSON.
2. Gunakan serializer untuk mengonversi data ke dalam format JSON.
3. Tambahkan URL untuk mengakses fungsi tersebut.

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
</details>
<details>
<summary>Mengembalikan Data dalam Format XML by ID</summary>

1. Buat fungsi view yang mengambil data produk berdasarkan ID dalam format XML.
2. Gunakan serializer untuk mengonversi data ke dalam format XML.
3. Tambahkan URL dengan parameter ID untuk mengakses fungsi tersebut.

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
</details>
<details>
<summary>Mengembalikan Data dalam Format JSON by ID</summary>

1. Buat fungsi view yang mengambil data produk berdasarkan ID dalam format JSON.
2. Gunakan serializer untuk mengonversi data ke dalam format JSON.
3. Tambahkan URL dengan parameter ID untuk mengakses fungsi tersebut.

```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
</details>

Setelah mengikuti langkah-langkah ini, Anda akan memiliki lima fungsi views yang dapat digunakan untuk melihat objek yang sudah ditambahkan dalam berbagai format (HTML, XML, JSON) serta berdasarkan ID dalam format XML dan JSON. Pastikan untuk menambahkan URL yang sesuai agar Anda dapat mengakses fungsi-fungsi tersebut.

## Membuat Routing URL
Tambahkan semua path URL fungsi yang telah disebutkan di atas ke dalam variabel `urlpatterns` dalam berkas `urls.py` di direktori main. Jangan lupa untuk mengimpor fungsi-fungsi tersebut dari `views.py`. Lalu menambahkan kode:

```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
]
```
Dengan ini kita telah menambahkan path URL, mengintegrasikan fungsi-fungsi tersebut ke dalam aplikasi Django Anda, sehingga kita dapat mengaksesnya melalui URL yang sesuai. Setelah menambahkan kode ini, jalankan perintah `python manage.py runserver` dan kunjungi http://localhost:8000 untuk mengakses aplikasi.

## Screenshot POSTMAN
<details>
<summary>1. HTML</summary>
<img src="/image/1.jpg">
</details>

<details>
<summary>2. XML</summary>
<img src="/image/2.jpg">
</details>

<details>
<summary>3. JSON</summary>
<img src="/image/3.jpg">
</details>

<details>
<summary>4. XML BY ID</summary>
<img src="/image/4.jpg">
</details>

<details>
<summary>5. JSON BY ID</summary>
<img src="/image/5.jpg">
</details>
</details>

# Tugas 4
<details>
<summary>1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?</summary>

|                                               **UserCreationForm**                                                          |
|-----------------------------------------------------------------------------------------------------------------------------|
|`UserCreationForm` adalah impor bawaan yang memudahkan proses pembuatan form pendaftaran pengguna dalam aplikasi web. Dengan form ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal. Fitur-fitur utama dari UserCreationForm meliputi validasi otomatis untuk nama pengguna, kata sandi, serta konfirmasi kata sandi. Formulir ini juga mencakup tombol "Daftar" yang menginisiasi proses pendaftaran pengguna dengan data yang diisi.|


| **Kelebihan**                                       | **Kekurangan**                                                                    |
|-----------------------------------------------------|-----------------------------------------------------------------------------------|
| Kemudahan penggunaan                                | Keterbatasan fitur jika memerlukan pendaftaran pengguna secara kustom             |
| Penghematan waktu dalam pengembangan                | Tampilan standar yang mungkin memerlukan penyesuaian lebih lanjut                 |
| Integrasi dengan model pengguna Django              | Perlu kustomisasi jika memerlukan tampilan yang sangat spesifik                   |
| Kemungkinan kustomisasi                             | Bergantung pada Django dan tidak cocok untuk pengembangan di luar kerangka Django |

</details>

 <details>
<summary>2.Apa perbedaan antara `autentikasi` dan `otorisasi` dalam konteks Django, dan mengapa keduanya penting?</summary>

| Fitur                       | Autentikasi                                      | Otorisasi                                   |
|-----------------------------|-------------------------------------------------|---------------------------------------------|
| Definisi                   | Proses verifikasi identitas pengguna            | Proses memberikan izin akses kepada pengguna |
| Apa yang Diperiksa         | Apakah pengguna adalah pengguna yang sebenarnya | Apakah pengguna memiliki izin yang sesuai   |
| Tujuan Utama               | Memastikan identitas pengguna                   | Memastikan pengguna memiliki akses yang sesuai |
| Contoh Implementasi        | Proses login dengan username dan password      | Menentukan apakah pengguna dapat mengakses halaman tertentu |
| Contoh Kode Django        | `authenticate(username=username, password=password)` | `@permission_required('some_permission')`   |
| Pentingnya dalam Aplikasi  | Memastikan pengguna hanya bisa mengakses akun mereka sendiri | Mencegah pengguna yang tidak sah mengakses data rahasia atau tindakan tertentu |
| Contoh Kebijakan Keamanan | Kebijakan pengguna harus memasukkan kata sandi yang benar untuk masuk | Kebijakan pengguna hanya bisa mengakses halaman admin jika mereka adalah superuser |
</details>

<details>
<summary>3.Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?</summary>

**Cookies** adalah file teks kecil yang disimpan pada perangkat pengguna saat mereka mengunjungi sebuah situs web. Dalam konteks aplikasi web, cookies digunakan untuk menyimpan informasi khusus pengguna, seperti preferensi, data masukan, atau data sesi. Mereka biasanya digunakan oleh aplikasi web untuk mengenali pengguna saat mereka kembali ke situs yang sama atau untuk menyimpan informasi yang perlu dipertahankan selama sesi pengguna.

| Langkah | Deskripsi |
| ------- | --------- |
| 1       | **Impor Modul**<br>Impor modul yang diperlukan seperti `django.http` di dalam berkas `views.py` atau berkas yang sesuai. Ini diperlukan untuk mengelola cookies. |
| 2       | **Mengatur Nilai Cookies**<br>Setelah pengguna berhasil masuk atau sesi dimulai, Anda dapat mengatur nilai cookies menggunakan objek `HttpResponse`|
| 3       | **Mengambil Nilai Cookies**<br>Untuk mengambil nilai cookies yang telah disimpan, Anda dapat menggunakan `request.COOKIES`|
| 4       | **Menghapus Cookies**<br>Jika Anda ingin menghapus cookie yang sudah ada, Anda dapat menggunakan metode `.delete_cookie()`|
| 5       | **Keamanan Cookies**<br>Penting untuk tidak menyimpan data sensitif atau kata sandi dalam cookies karena cookies bersifat terbuka dan dapat dibaca oleh pengguna. Untuk data sensitif, gunakan sesi Django yang lebih aman. Pastikan untuk menggantikan contoh kode dengan kode yang sesuai dengan kebutuhan aplikasi.|

Dengan mengikuti langkah-langkah ini, Anda dapat menggunakan cookies dalam Django untuk mengelola data sesi pengguna dengan aman. Pastikan untuk menggantikan contoh kode dengan kode yang sesuai dengan kebutuhan aplikasi Anda.

</details>

<details>
<summary>4.Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</summary>

| Langkah                          | Deskripsi                                                                                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------|
| Penggunaan Cookies dalam Web     | Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang perlu diwaspadai. Ini adalah sejenis file kecil yang digunakan untuk menyimpan informasi sederhana, seperti preferensi atau sesi login pengguna.                                                                                                                       |
| Keamanan Data                    | Cookies bisa berisi informasi sensitif jika tidak dienkripsi dengan benar, seperti informasi akun pengguna. Pencurian data ini bisa berakibat fatal.                         |
| Potensi Pencurian Cookie         | Penyerang dapat mencuri cookies dari perangkat pengguna, membahayakan keamanan informasi dan akun pengguna.                                                       |
| Privasi                          | Cookies juga bisa digunakan untuk melacak aktivitas online tanpa izin, yang dapat mengganggu privasi pengguna.   |
| Modifikasi Cookie                | Pengguna dengan pengetahuan teknis dapat memanipulasi cookies, memungkinkan akses yang tidak sah atau perubahan data.      |
| Tindakan Keamanan                | Untuk meningkatkan keamanan penggunaan cookies, pastikan untuk menggunakan HTTPS, enkripsi data sensitif dalam cookies, dan menjaga sesi login tetap aman.|
| Kesimpulan                       | Penggunaan cookies adalah alat yang berguna dalam pengembangan web, tetapi perlu diwaspadai risiko yang terkait dan tindakan keamanan yang sesuai harus diambil.|

</details>

<details>
<summary>5. Jelaskan bagaimana cara kamu mengimplementasikan `checklist` di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

1. **Membuat Fungsi Registrasi dan Form Registrasi:**
   - Buat fungsi `register` di `views.py` untuk menangani proses registrasi pengguna.
   - Gunakan modul `UserCreationForm` untuk membuat formulir registrasi pengguna dengan mudah.
   - Validasi dan simpan data registrasi pengguna menggunakan formulir.
   - Berikan pesan konfirmasi setelah registrasi berhasil.
   - Buat halaman HTML `register.html` untuk tampilan formulir registrasi.
   - Tambahkan URL path untuk registrasi.

2. **Membuat Fungsi Login:**
   - Buat fungsi `login_user` di `views.py` untuk menangani proses login pengguna.
   - Gunakan modul `authenticate` dan `login` untuk melakukan autentikasi pengguna.
   - Validasi data masuk pengguna.
   - Buat halaman HTML `login.html` untuk tampilan formulir login.
   - Tambahkan URL path untuk login.

3. **Membuat Fungsi Logout:**
   - Buat fungsi `logout_user` di `views.py` untuk menangani proses logout pengguna.
   - Gunakan modul `logout` untuk menghapus sesi pengguna yang saat ini masuk.
   - Tambahkan tombol logout pada halaman utama.

4. **Merestriksi Akses Halaman Main:**
   - Tambahkan `@login_required` decorator untuk membatasi akses ke halaman utama hanya untuk pengguna yang sudah login.
   - Pengguna yang tidak terautentikasi akan diarahkan ke halaman login.

5. **Menggunakan Data Dari Cookies:**
   - Gunakan cookies untuk menyimpan informasi, seperti data terakhir login pengguna.
   - Saat pengguna login, set cookie dengan data terakhir login.
   - Tampilkan data cookies di halaman utama.
   - Hapus cookie saat pengguna logout.

6. **Menghubungkan Model Product dengan User:**
   - Hubungkan setiap objek Product dengan pengguna yang membuatnya menggunakan ForeignKey.
   - Modifikasi fungsi `create_product` untuk mengaitkan produk yang dibuat dengan pengguna yang sedang login.
   - Tampilkan produk yang dimiliki oleh pengguna yang sedang login di halaman utama.

7. **Menambahkan Bonus:**
   - Pembuatan Fungsi dalam views.py:
        1. Membuat tiga fungsi di views.py yang akan diakses melalui URL:
            - add_product: Menambahkan satu unit produk ke keranjang belanja.
            - decrement_product: Mengurangi satu unit produk dari keranjang belanja.
            - remove_product: Menghapus produk dari keranjang belanja.
        Fungsi ini menerima permintaan POST dan memprosesnya sesuai dengan tombol yang ditekan pada halaman HTML.
        2. Konfigurasi URL dalam urls.py:
            - Menambahkan tiga pola URL yang akan mengarahkan permintaan ke fungsi yang sesuai di views.py. 
            - Setiap pola URL memiliki parameter product_id untuk mengidentifikasi produk yang akan diubah.
        3. Penggunaan Tombol dalam main.html:
            - Di dalam file template main.html, Anda telah menambahkan tombol yang akan digunakan untuk menambah, mengurangi, dan menghapus produk.
            - Setiap tombol terletak dalam sebuah <form> yang mengirimkan permintaan POST ke URL yang sesuai dengan aksi yang diinginkan (add_product, decrement_product, atau remove_product).
            - Tombol memiliki nama yang berbeda (Tambah, Kurang, atau Hapus) sehingga Anda dapat membedakan aksi yang diambil dalam fungsi views.py.

</details>


# Tugas 5

<details>
<summary> 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.</summary>

**Element Selector** merupakan salah satu jenis selektor dalam CSS yang berfungsi untuk memilih elemen HTML berdasarkan jenis atau nama elemen yang digunakan. Dalam CSS, terdapat beberapa variasi selektor elemen yang sering digunakan, dan masing-masingnya memiliki kegunaan dan waktu yang sesuai untuk digunakan. Berikut ini adalah beragam jenis selektor elemen beserta manfaat dan situasi penggunaannya yang tepat:

| Jenis Selector                  | Manfaat                                                                           | Waktu Penggunaan                                                                                                 |
|---------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Universal Selector (*)           | Memilih semua elemen pada halaman web.                                            | Jarang digunakan secara eksplisit karena dapat berdampak besar pada performa. Dapat digunakan untuk menerapkan gaya umum pada semua elemen.                |
| Type Selector (e.g., p, h1, div) | Memilih semua elemen dengan jenis atau tipe yang spesifik misalnya, `<p>`, `<h1>`, `<div>`. | Digunakan ketika ingin mengaplikasikan gaya khusus pada jenis elemen tertentu pada halaman.                      |
| Class Selector (e.g., .class-name) | Memilih semua elemen yang memiliki atribut class tertentu.                       | Berguna saat ingin mengaplikasikan gaya pada sekelompok elemen yang memiliki kelas yang sama. Dapat digunakan berulang-ulang pada halaman yang berbeda. |
| ID Selector (e.g., #element-id)  | Memilih elemen dengan atribut ID tertentu.                                        | Digunakan ketika ingin mengaplikasikan gaya atau logika tertentu pada elemen yang memiliki ID unik. Sebaiknya digunakan satu kali untuk setiap ID pada halaman. |
| Attribute Selector (e.g., [attribute=value]) | Memilih elemen berdasarkan atribut dan nilai atribut yang spesifik.         | Berguna ketika ingin mengaplikasikan gaya atau logika pada elemen dengan atribut tertentu, seperti mengubah gaya tautan dengan atribut "href" tertentu. |
| Pseudo-class Selector (e.g., :hover, :first-child) | Memilih elemen berdasarkan keadaan atau status tertentu.                  | Digunakan untuk memberikan efek interaktif atau gaya tambahan pada elemen berdasarkan interaksi pengguna atau posisi dalam struktur dokumen. |
| Pseudo-element Selector (e.g., ::before, ::after) | Memilih dan menggabungkan elemen palsu yang dibuat dengan CSS.         | Digunakan ketika ingin menambahkan konten tambahan ke dalam elemen, seperti ikon atau garis bawah pada tautan.       |

</details>

<details>
<summary> 2. Jelaskan HTML5 Tag yang kamu ketahui. </summary>


| Tag HTML5       | Deskripsi                                                     |
|-----------------|---------------------------------------------------------------|
| `<div>`         | Tag umum yang digunakan untuk mengelompokkan dan memformat elemen. |
| `<p>`           | Digunakan untuk menampilkan paragraf teks.                       |
| `<a>`           | Untuk membuat tautan atau hyperlink ke halaman lain.             |
| `<img>`         | Digunakan untuk menampilkan gambar pada halaman web.             |
| `<ul>` dan `<ol>`  | Untuk membuat daftar tak berurutan (unordered list) dan daftar terurut (ordered list). |
| `<li>`          | Digunakan dalam elemen `<ul>` dan `<ol>` untuk mendefinisikan item dalam daftar. |
| `<h1>`, `<h2>`, ... `<h6>` | Digunakan untuk menandai judul atau heading dengan tingkat kepentingan yang berbeda. |
| `<form>`        | Untuk membuat formulir yang memungkinkan pengguna mengirimkan data. |
| `<input>`       | Digunakan dalam elemen `<form>` untuk membuat berbagai jenis elemen input, seperti teks, email, dan lainnya. |
| `<button>`      | Untuk membuat tombol interaktif yang dapat digunakan untuk tindakan pengguna. |

</details>

<details>
<summary> 3. Jelaskan perbedaan antara margin dan padding. </summary>

**Margin** adalah jarak luar elemen: Margin adalah ruang di sekitar elemen HTML, di luar batas elemen itu sendiri. Margin adalah jarak antara elemen tersebut dengan elemen-elemen lain di sekitarnya.
Tidak berpengaruh pada latar belakang: Margin tidak memiliki latar belakang atau warna. Ini hanya mengatur jarak antara elemen-elemen.
Mempengaruhi tata letak keseluruhan: Margin dapat memengaruhi tata letak keseluruhan halaman dengan memengaruhi jarak antara elemen-elemen di dalamnya.
Nilai negatif diizinkan: Anda dapat mengatur margin dengan nilai negatif untuk menggeser elemen lebih dekat ke elemen lain.
Padding:

**Padding** adalah jarak di dalam elemen: Padding adalah ruang di dalam batas elemen HTML. Ini adalah jarak antara batas elemen dan kontennya sendiri.
Pengaruh pada latar belakang: Padding dapat memiliki latar belakang atau warna, sehingga memengaruhi bagian dalam elemen.
Mempengaruhi ukuran elemen: Padding memengaruhi ukuran total elemen. Misalnya, jika Anda memberikan padding pada sebuah kotak, ukuran kotak tersebut akan bertambah sesuai dengan padding yang ditentukan.
Nilai negatif jarang digunakan: Padding jarang diatur dengan nilai negatif, dan dalam banyak kasus, itu tidak dianjurkan karena dapat menghasilkan tampilan yang tidak diinginkan.
</details>
 

<details>
<summary> 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? </summary>

| Aspek                         | Bootstrap                                                | Tailwind CSS                                                   |
|-------------------------------|----------------------------------------------------------|-----------------------------------------------------------------|
| **Filosofi Desain**           | Lebih mengikuti desain yang telah ditentukan dengan banyak komponen siap pakai. | Lebih mendukung pendekatan "utility-first," memungkinkan penyesuaian yang lebih besar dan desain yang lebih bebas.  |
| **Kustomisasi**               | Terdapat opsi kustomisasi, tetapi perlu melewati proses yang lebih rumit. | Sangat fleksibel dan mudah dikustomisasi melalui pengaturan kelas CSS.    |
| **Kesulitan Penggunaan**      | Lebih mudah bagi pemula karena komponen-komponen sudah ada dan mudah digunakan. | Memiliki kurva belajar yang lebih tinggi karena Anda harus memahami kelas-kelas utility. |
| **Performa**                   | Lebih berat dibandingkan dengan Tailwind karena berisi lebih banyak CSS. | Lebih ringan karena hanya menggunakan apa yang diperlukan, sehingga biasanya lebih cepat. |
| **Komunitas dan Ekosistem**   | Memiliki komunitas yang besar dan banyak dukungan serta dokumentasi. | Meskipun komunitasnya tumbuh, masih lebih kecil daripada Bootstrap.  |
| **Proyek Skala Besar**         | Cocok untuk proyek besar dan kompleks yang memerlukan desain yang konsisten. | Cocok untuk proyek-proyek yang memerlukan kustomisasi desain yang ekstensif dan inovatif. |
| **Kecepatan Pengembangan**    | Dapat mempercepat pengembangan dengan komponen siap pakai. | Memerlukan lebih banyak penulisan kode tetapi lebih fleksibel dalam penyesuaian desain. |
| **Kapan Sebaiknya Digunakan** | Sebaiknya digunakan jika Anda ingin memulai dengan cepat dan perlu komponen-komponen yang sudah siap. | Sebaiknya digunakan jika Anda ingin kustomisasi desain yang tinggi dan memiliki kebutuhan yang sangat spesifik. |
</details>

<details>
<summary>  5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

1. **CSS Umum**:
    - Bagian CSS umum yang digunakan untuk mengatur berbagai aspek tampilan halaman web.

2. **Body Styling**:
    - Styling untuk elemen `<body>` yang mengatur font, margin, padding, latar belakang, dan ketinggian minimum halaman.

3. **Header Styling**:
    - Styling untuk elemen `<header>` yang mencakup warna latar belakang, warna teks, penjajaran teks, dan padding.

4. **Container Styling**:
    - Styling untuk elemen dengan kelas "container" yang mencakup lebar maksimum, margin, padding, penjajaran teks, tata letak grid dengan tiga kolom, dan jarak antar elemen.

5. **Pet Card Styling**:
    - Styling untuk elemen dengan kelas "pet-card" yang mencakup warna latar belakang, border, padding, sudut bulat, penjajaran teks, dan bayangan.

6. **Button Styling**:
    - Styling untuk elemen dengan kelas "btn" yang digunakan untuk tombol. Ini mencakup warna latar belakang, warna teks, padding, border, sudut bulat, kursor, dan margin atas.

7. **Heading Styling**:
    - Styling untuk elemen-elemen `<h1>`, `<h2>`, `<h3>`, `<h5>` yang mencakup ukuran font, warna teks, dan margin.

8. **Paragraph Styling**:
    - Styling untuk elemen `<p>` yang mencakup ukuran font.

9. **Image Styling**:
    - Styling untuk elemen `<img>` yang mencakup penampilan gambar dengan membatasi lebar maksimum dan menjaga aspek rasio.

10. **Table Styling**:
    - Styling untuk elemen `<table>` yang mencakup lebar, margin bawah, dan pengaturan border-collapse.

11. **Table Header Styling**:
    - Styling untuk elemen-elemen `<th>` dalam tabel yang mencakup warna latar belakang, warna teks, tebal huruf, penjajaran teks, dan padding.

12. **Table Data Styling**:
    - Styling untuk elemen-elemen `<td>` dalam tabel yang mencakup padding, border, dan penjajaran teks.

13. **Add Product Button Styling**:
    - Styling untuk tombol "Add New Product" yang mencakup penjajaran teks, margin atas, dan font tebal.

14. **Logout Button Styling**:
    - Styling untuk tombol "Logout" yang mencakup penjajaran teks, margin atas, dan font tebal.

15. **Background Color**:
    - `background-color` digunakan untuk mengatur warna latar belakang elemen, seperti header dan kartu hewan peliharaan.
    - Misalnya, `background-color: #751A60;` mengatur latar belakang dengan warna ungu tua.

16. **Font Color**:
    - `color` digunakan untuk mengatur warna teks dalam elemen, seperti header, teks harga, dan deskripsi produk.
    - Misalnya, `color: #fff;` mengatur warna teks menjadi putih.

17. **Warna Tombol**:
    - Warna tombol, seperti "Add New Product" dan "Logout," juga diatur dengan `background-color` dan `color`.
    - Misalnya, tombol "Add New Product" memiliki `background-color: #751A60;` dan `color: #fff;`, yang menghasilkan tombol dengan latar belakang ungu tua dan teks putih.

18. **Warna Header**:
    - Warna latar belakang header diatur dengan `background-color: #751A60;`, yang memberikan header latar belakang ungu tua.
    - Warna teks diatur dengan `color: #fff;`, yang memberikan teks pada header warna putih.

19. **Warna Judul Tabel**:
    - Warna latar belakang judul tabel (elemen `<th>`) diatur dengan `background-color: #751A60;`, yang menghasilkan latar belakang ungu tua.
    - Warna teks judul tabel diatur dengan `color: #fff;`, yang memberikan teks pada judul tabel warna putih.

20. **Warna Teks dalam Tabel**:
    - Warna teks dalam sel tabel (elemen `<td>`) diatur dengan `color: #751A60;`, yang memberikan teks warna ungu tua pada sel tabel.
</details>

</details>
</details>

