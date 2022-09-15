# Assignment 2

Deployed URL: [Heroku](https://pbp22t2.herokuapp.com/katalog)

## Bagan Request-Response

![](https://i.imgur.com/gFEvMME.png)

Client mengirim request kepada server, lalu server meneruskan request tersebut ke Django. Django lalu mem-_parse_ URL yang diterima, lalu mencari _mapping_ URL ke _view function_ di file `urls.py`. _View function_ berada di `views.py` yang melakukan query ke database melewati models yang telah didefinisikan di `models.py`, lalu me-_render_ HTML berdasarkan template yang ada. Setelah render dilakukan, response dikirim kembali ke client.

## _Virtual Environment_

_Virtual environment_ digunakan untuk menjaga konsistensi dari _dependency_ yang ada di proyek tersebut, sehingga tidak terjadi bentrok antar satu proyek dengan proyek lainnya yang dapat menyebabkan error.

Aplikasi dapat berjalan tanpa menggunakan _virtual environment_, asalkan versi dari _dependency_ yang terinstall di _global environment_ dapat menjalankan aplikasi Django yang kita buat.

## Implementasi

### `views.py`

Di file ini, dibuat _function_ baru yang menerima argumen request `show_catalogs(request: HttpRequest)`. Di dalam _function_ tersebut mengambil semua data dari model yang di simpan dalam context, lalu di-render ke template HTML menggunakan _function_ `render()`.

### `urls.py`

Berdasarkan _function_ yang telah dibuat di `views.py` sebelumnya, _function_ tersebut di-_import_ lalu didefinisikan dalam list `urlpatterns`, yang berisi `[ path("", show_catalogs, name="show_catalogs") ]`

### `katalog.html`

File ini adalah file template HTML yang sudah disediakan, hanya cukup melengkapi. Berdasarkan _context_ yang sudah diberikan, dilakukan looping untuk semua item katalog dengan `{% for item in items %}`, dan menuliskan semua data dari suatu elemen (`<td>`) dalam satu row html untuk satu elemen (`<tr>`)

## Deployment

Untuk men-deploy, cukup menaruh `HEROKU_API_KEY` dari settings account dan `HEROKU_APP_NAME` di secrets GitHub Actions.
