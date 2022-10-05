# Tugas 4

[Link](https://pbp22t2.herokuapp.com/todolist)

## Kegunaan CSRF Token

CSRF token digunakan untuk mencegah _Cross Site Request Forgery_, yaitu tindakan dimana penyerang membuat target melakukan
aksi yang tidak diinginkan orang tersebut terhadap website yang telah diautentikasi orang itu. Sebagai contoh, melakukan
transfer bank melalui routing `/transfer?target=129824332&amount=1000000`. Pada server yang tidak menggunakan proteksi CSRF,
apabila user meng-klik URL tersebut, akan langsung mentransfer ke target.

CSRF token bekerja dengan server mengirim token tersebut ke client, dan client harus mengirim kembali token tersebut sebagai
bagian dari request selanjutnya. Apabila token tidak ada atau tidak sesuai dengan apa yang dimiliki server, maka request
tersebut akan di-reject.

## Form Secara Manual

Form tidak wajib menggunakan `{{ form.as_table }}`. Form dapat dibuat secara manual, yaitu dengan membuat tag `<input>` dengan
attribute `name` dan `type` yang sesuai dengan form yang ada di code server Django.

## Alur Submisi

Saat user meng-klik submit, data dari form yang ada di client akan dikirim melalui request POST (atau GET, tergantung konfigurasi
tag `<form>`) ke server. Setelah itu, server akan memproses input yang diberikan melalui views yang ada, dan menyimpan data
menggunakan ORM dengan method `.save()` atau `Model.objects.create()`. Setelah itu, data yang sudah disimpan dapat diakses di dalam
views dengan memanggil melalui ORM model-nya (`Model.objects.filter(user=request.user).all()`), data tersebut ditaruh dalam context
rendering HTML, dan dapat diakses sebagai variable di dalam template HTML.

## Proses Pengerjaan

1. Membuat app baru dengan `python manage.py startapp todolist`
2. Menambahkan routing todolist ke `project_django/urls.py`
3. Membuat model `Task` di dalam `todolist/models.py`
4. Membuat fungsionalitas login, logout, dan register dengan bantuan `django.contrib.auth`
5. Membuat fungsionalitas list task dan create
6. Menambahkan routing otentikasi dan list task dan create ke `todolist/urls.py`
7. Mendeploy ke Heroku.

---

# Tugas 5

## Inline vs Internal vs External CSS

Aspek | Inline | Internal | External
------|--------|----------|---------
Lokasi | Dalam elemen dengan atrr `style` | Dalam HTML dengan tag `<style>` | Dalam file `.css` yang di-*import* dalam tag `<tag>`
Scope | Hanya elemen yang dipakai | Satu halaman | Setiap halaman yang memiliki import tersebut

Inline CSS memiliki kelebihan untuk melimit ke suatu elemen, namun tag tersebut akan terlihat sedikit berantakan karena style
dicampur dengan HTML. Internal CSS memiliki kelebihan yaitu dapat dilimit untuk suatu page tertentu, namun apabila terdapat beberapa
rule yang berulang untuk page lain, menjadi tidak efisien. Sedangkan external memiliki kelebihan untuk berbagi style ke beberapa page
sekaligus, namun untuk men-*debug* bisa sedikit membingungkan.

## Tag HTML5

> Tidak termasuk tag yang sudah ada sebelum HTML5 seperti `<div>`

Beberapa tag yang saya ketahui yaitu `<section>` yang menandakan suatu bagian dari halaman yang berbeda, `<main>` yang menandakan bahwa
bagian tersebut adalah bagian utama dari page tersebut, `<aside>` yang digunakan untuk menandakan bagian yang tidak berhubungan secara
langsung dengan konten utama, dan lain-lain. 

## Tipe-tipe CSS Selector
- `*` -- Universal selector, match semua elemen.
- `elementname` (contoh: `input`) -- Type selector, memilih suatu tag.
- `.classname` -- Class selector, memilih tag dengan class yang disebut
- `#idname` -- ID selector, memilih elemen yang memiliki ID tersebut

## Checklist
- Instalasi DaisyUI melalui CDN yang ada di [dokumentasi DaisyUI](https://daisyui.com/docs/cdn/)
- Melakukan perubahan menggunakan component yang sudah ada di dokumentasi DaisyUI serta layouting
  yang dapat dilakukan dengan Tailwind CSS.
- Untuk menjadi responsif, beberapa komponen memiliki class responsif yang didasarkan atas
  [sistem responsive design Tailwind CSS](https://tailwindcss.com/docs/responsive-design) yang menggunakan
  breakpoint.
- Untuk bonus, menggunakan [scale](https://tailwindcss.com/docs/scale) dan pseudoclass tailwind `hover:`
  dan menambah animasi dengan [transition](https://tailwindcss.com/docs/transition-property)

