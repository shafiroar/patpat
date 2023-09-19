
## TUGAS 3
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

