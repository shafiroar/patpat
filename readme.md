## Nama    : Shafira Nurrohmah
## NPM     : 2206030035
## Kelas   : PBP C
## Link Aplikasi : https://patpat.adaptable.app/main/

## **Daftar Isi**
- [Tugas 2](#Tugas2)
- [Tugas 3](#Tugas3)

## Tugas2 

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

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
Jawab: 

<img src="/image/graphs.jpg">

Penjelasan:

Anggap saja ada seorang klien yang melakukan tindakan tertentu di sebuah situs yang menggunakan Django. Saat itu, peramban klien akan mengirimkan permintaan HTTP ke server situs tersebut, dan permintaan ini akan ditangani oleh berkas `urls.py` untuk mencari pola URL yang diminta oleh klien. Setelah itu, framework Django akan menggunakan berkas `views.py` untuk melakukan pemrosesan dan operasi logika terhadap data yang terdapat dalam berkas `models.py`. Setelah proses pemrosesan data selesai, berkas `views.py` akan mengirimkan berkas HTML yang terdapat dalam direktori `templates` kepada klien. Selanjutnya, peramban klien akan melakukan proses penyusunan ulang (rendering) berkas HTML ini sebagai tanggapan HTTP yang diterimanya.
 
### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment dalam pengembangan aplikasi web berbasis Django karena:
1. Isolasi Dependensi: Virtual environment memungkinkan kita untuk mengisolasi dependensi dan paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah dependensi.
2. Manajemen Versi Python: Dengan virtual environment, kita dapat menggunakan versi Python yang berbeda untuk setiap proyek, memberikan fleksibilitas dalam penggunaan versi Python yang sesuai.
3. Keamanan Proyek: Penggunaan virtual environment menjaga keamanan proyek dengan menghindari perubahan paket sistem Python yang dapat memengaruhi stabilitas atau keamanan sistem.
4. Portabilitas: Virtual environment memungkinkan proyek Python untuk tetap portabel, mudah dibagi dengan orang lain, atau dipindahkan ke server lain tanpa masalah.
Meskipun mungkin memungkinkan untuk membuat aplikasi web Django tanpa virtual environment, sebaiknya selalu menggunakan virtual environment untuk menjaga kebersihan, keamanan, dan manajemen dependensi yang efisien dalam pengembangan aplikasi Python.


### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

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

## Tugas3 
### 1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?

| Perbedaan         |  `POST`                                           | `GET`                                                 |
|-------------------|---------------------------------------------------|-------------------------------------------------------|
| Metode HTTP       | Mengirim data dengan metode POST.                 | Mengirim data dengan metode GET.                      |
| Tampilan URL      | Data tidak tampil dalam URL.                      | Data ditampilkan dalam URL.                           |
| Keamanan          | Lebih aman untuk mengirim data sensitif.          | Kurang aman karena data terlihat dalam URL.           |
| Panjang Data      | Tidak terbatas pada panjang data yang dikirim.    | Terbatas pada panjang URL maksimum                    |
| Cacheable         | Data biasanya tidak di-cache.                     | Data dapat di-cache (oleh proxy server atau browser). |
| Penggunaan        | Mengirim data yang akan diproses oleh server.     | Digunakan untuk mengambil data dari server.           |
| Contoh Penggunaan | Formulir login, pengeposan data sensitif.         | Pengambilan data dari URL (misalnya, pencarian).      |

### 2. Apa perbedaan utama antara `XML`, `JSON`, dan `HTML` dalam konteks pengiriman data?

| Perbedaan Utama      | XML                          | JSON                            | HTML                                |
|----------------------|------------------------------|---------------------------------|-------------------------------------|
| Struktur Data        | Menggunakan markup hierarkis  | Berbasis key-value pairs       | Berbasis tag dan elemen             |
| Kemampuan Pemrosesan | Tidak selalu mudah diproses oleh mesin dan manusia | Mudah diproses oleh mesin dan manusia | Dirancang untuk ditampilkan di browser |

### 3. Mengapa `JSON` sering digunakan dalam pertukaran data antara aplikasi web modern?

**JSON (JavaScript Object Notation)** sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki sejumlah keunggulan dan karakteristik yang sangat cocok untuk kebutuhan ini:

**Ringkas dan Mudah Dibaca:** JSON menggunakan format teks yang ringkas dan mudah dibaca oleh manusia. Ini membuatnya mudah untuk dipahami dan dianalisis, baik oleh pengembang maupun oleh mesin.

**Bahasa-Agnostik:** JSON adalah format data yang bahasa-agnostik, artinya dapat digunakan dalam berbagai bahasa pemrograman. Ini memungkinkan berbagai aplikasi yang ditulis dalam bahasa yang berbeda untuk berkomunikasi dengan mudah.

**Kemampuan Pemrosesan Mudah:** JSON dapat dengan mudah diproses oleh mesin, termasuk JavaScript di sisi klien dan bahasa pemrograman lain di sisi server. Ini membuatnya ideal untuk pertukaran data antara klien dan server dalam aplikasi web.

**Struktur Data yang Fleksibel:** JSON mendukung struktur data yang fleksibel. Anda dapat menggunakan objek dan array bersarang untuk merepresentasikan data yang kompleks dan terstruktur dengan baik.

**Dukungan untuk Tipe Data Standar:** JSON mendukung tipe data standar seperti string, angka, boolean, array, dan objek. Ini mencakup hampir semua jenis data yang umum digunakan dalam aplikasi web.


### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

## INPUT FORM
### Langkah 1: Buat Struktur `Form` 
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

### Langkah 2: Tambahkan fungsi `Views` 
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

### Langkah 3: Perbaikin fungsi `show_main` 
- Perbarui fungsi `show_main` dalam `views.py` untuk menampilkan data produk yang ada dengan melanjutkan dari tugas sebelumnya.

### Langkah 4: Tambahkan URL
- Buka berkas `urls.py` dalam direktori `main` dan tambahkan URL untuk akses fungsi `create_product`.
```python
path('create-product', create_product, name='create_product'),
```
### Langkah 5: Buat Form HTML
- Buat berkas `create_product.html` dalam direktori `main/templates` dan tambahkan kode form HTML.
```python
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

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

## Langkah 6: Tampilkan Data pada Halaman Utama
Perbarui berkas `main.html` dalam direktori `main/templates` untuk menampilkan data produk dalam bentuk tabel dan tombol "Add New Product" yang akan mengarahkan ke halaman form.

## 5 FUNGSI VIEWS
Berikut adalah langkah-langkah singkat untuk menjawab pertanyaan tentang cara menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID dalam Django:

### Mengembalikan Data dalam Format HTML

1. Buat fungsi view yang mengambil data produk dalam format HTML.
2. Tambahkan URL untuk mengakses fungsi tersebut.

### Mengembalikan Data dalam Format XML

1. Buat fungsi view yang mengambil data produk dalam format XML.
2. Gunakan serializer untuk mengonversi data ke dalam format XML.
3. Tambahkan URL untuk mengakses fungsi tersebut.

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

### Mengembalikan Data dalam Format JSON

1. Buat fungsi view yang mengambil data produk dalam format JSON.
2. Gunakan serializer untuk mengonversi data ke dalam format JSON.
3. Tambahkan URL untuk mengakses fungsi tersebut.

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Mengembalikan Data dalam Format XML by ID

1. Buat fungsi view yang mengambil data produk berdasarkan ID dalam format XML.
2. Gunakan serializer untuk mengonversi data ke dalam format XML.
3. Tambahkan URL dengan parameter ID untuk mengakses fungsi tersebut.

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

### Mengembalikan Data dalam Format JSON by ID

1. Buat fungsi view yang mengambil data produk berdasarkan ID dalam format JSON.
2. Gunakan serializer untuk mengonversi data ke dalam format JSON.
3. Tambahkan URL dengan parameter ID untuk mengakses fungsi tersebut.

```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Setelah mengikuti langkah-langkah ini, Anda akan memiliki lima fungsi views yang dapat digunakan untuk melihat objek yang sudah ditambahkan dalam berbagai format (HTML, XML, JSON) serta berdasarkan ID dalam format XML dan JSON. Pastikan untuk menambahkan URL yang sesuai agar Anda dapat mengakses fungsi-fungsi tersebut.

## MEMBUAT ROUTING URL
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

##S SCREENSHOT POSTMAN
## 1. HTML
<img src="/image/1.jpg">

## 2. XML
<img src="/image/2.jpg">

## 3. JSON
<img src="/image/3.jpg">

## 4. XML BY ID
<img src="/image/4.jpg">

## 5. JSON BY ID
<img src="/image/5.jpg">

