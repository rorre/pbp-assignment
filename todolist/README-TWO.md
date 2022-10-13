# Tugas 6

## Async vs Sync
Dalam pemrograman sinkronus, setiap perintah akan memblok eksekusi perintah selanjutnya hingga perintah yang
sedang dieksekusi selesai. Sedangkan pada pemrograman sinkronus, perintah-perintah lain dapat dijalankan
secara bersamaan dengan perintah yang sedang dieksekusi.

## Event-Driven Programming
Event-driven programming adalah suatu paradigma di mana alur yang dijalankan suatu program didasarkan atas *event*
atau perilaku yang dilakukan antar user dan client. Sehingga, di terjadi pengiriman "pesan" yaitu *event* yang
ingin diproses, lalu program akan memanggil perintah-perintah berdasarkan *event* yang didapat.

Pada Tugas 6, ini dilakukan dengan `onReady` document untuk inisialisasi, `onClick` untuk button form baru, serta
`onSuccess` yang dipanggil setelah pemanggilan AJAX berhasil.

## Penerapan Async Pada AJAX
Penerapan asyncronous programming pada AJAX terdapat pada fakta bahwa browser tidak perlu meng-*suspend* segala
operasi yang dilakukan selama request AJAX berlangsung. Browser akan terus berjalan seperti biasa, bahkan dapat
melaksanakan perintah lainnya di mana request tersebut berjalan di latar belakang. Oleh karena itu, AJAX dapat
digunakan untuk mengubah tampilan website berdasarkan hasil tanpa memerlukan *reload*.

Tidak hanya itu, AJAX juga menggunakan paradigma *Event-Driven Programming*, di mana setelah AJAX dilakukan,
dapat memanggil fungsi yang diberikan pada `onSuccess` dan memberi data hasil ke fungsi tersebut.

## Proses Pengerjaan
1. Membuat views untuk AJAX, dapat dilihat [di sini](https://github.com/rorre/pbp-assignment/blob/14cf526aa21f53dd883cb6a5bcf1486834d0eb25/todolist/views.py#L108-L143)
2. Menaruh routing di `urls.py`, dan mapping sesuai function, dapat dilihat [di sini](https://github.com/rorre/pbp-assignment/blob/14cf526aa21f53dd883cb6a5bcf1486834d0eb25/todolist/urls.py#L25-L28)
3. Rendering dirubah dari templating menjadi AJAX GET
    - Melakukan GET ke endpoint JSON
    - Memproses setiap entry, lalu membuat HTML untuk setiap card
    - Append pada container grid yang telah ditentukan
4. Membuat modal dengan DaisyUI, lalu menaruh form di dalam modal tersebut
5. Untuk tombol buat, di-hook dengan event `onClick` untuk melakukan AJAX POST
6. Setelah berhasil, tutup modal
7. Reset container todo dengan `.empty()`, lalu render kembali dengan no 3
8. Untuk bonus, saat merender card, select tombol delete dengan jquery, dan hook `onClick` dengan melakukan AJAX DELETE
9. Setelah AJAX DELETE selesai, lakukan kembali no 7
