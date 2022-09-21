# Tugas 3

Deployed app: https://pbp22t2.herokuapp.com

- HTML: https://pbp22t2.herokuapp.com/mywatchlist/html
- XML: https://pbp22t2.herokuapp.com/mywatchlist/xml
- JSON: https://pbp22t2.herokuapp.com/mywatchlist/json

## XML vs HTML vs JSON

- XML dan HTML adalah markup language, sedangkan JSON notasi objek.
- HTML digunakan untuk menampilkan dokumen di browser, sedangkan XML dan JSON digunakan untuk data.
- XML dan HTML relatif lebih berat daripada JSON.
- XML dan HTML dapat diakses menggunakan DOM, sedangkan JSON diakses seperti key-value pair.

## Mengapa diperlukan data delivery?

Data delivery diperlukan sebab suatu aplikasi perlu melakukan pertukaran data dengan server. Sebab seringkali
data yang diberikan bersifat dinamis, yaitu dapat berubah dengan waktu karena terdapat pengguna yang mengganti
data tersebut (baik melalui server atau aplikasi tersebut). Dengan data delivery ini, data yang diberikan
selalu mencerminkan dengan data terbaru yang ada di server.

## Implementation

1. Membuat project baru dengan command `python manage.py startapp mywatchlist`.
2. Menambahkan aplikasi yang dibuat ke `project_django/settings.py`

```
INSTALLED_APPS = [
    ...
    'mywatchlist',
]
```

3. [Membuat model data di `mywatchlist/models.py`](https://github.com/rorre/pbp-assignment/commit/b44d3ef09eb2eaa4951c7b75b057a30023ac987f)
4. [Menambahkan data di dalam folder fixtures](https://github.com/rorre/pbp-assignment/commit/fad6f4b0f870953c256f618d6185dcad39aad148)
5. [Menambahkan logic views](https://github.com/rorre/pbp-assignment/commit/8072bea88fa959082b26bd4468c4b9ea09406726) serta [path ke views](https://github.com/rorre/pbp-assignment/blob/main/mywatchlist/urls.py)
6. [Membuat data migration](https://github.com/rorre/pbp-assignment/commit/81032992c46c78dcef0bf04f802de6feeb93eccc) dengan `python manage.py makemigrations` dan melakukan migration dengan `python manage.py migrate`
7. Meload data dengan `python manage.py loaddata initial_watchlist.json`
8. [Meng-update Procfile untuk load fixture](https://github.com/rorre/pbp-assignment/commit/072a0ca3d2dae735c1ea392bd11dfaec61f6145e)

## Postman

### HTML

![](https://i.imgur.com/j75sZn4.png)

### JSON

![](https://i.imgur.com/QsRZRfA.png)

### XML

![](https://i.imgur.com/sQSWgxu.png)
