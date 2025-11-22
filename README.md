🧥 Rahata Store - Premium Hoodies Web App

Rahata Store adalah aplikasi web e-commerce sederhana namun fungsional yang dirancang khusus untuk penjualan produk fashion (Hoodie). Aplikasi ini dibangun menggunakan teknologi web standar (HTML, CSS, JavaScript) tanpa memerlukan backend server yang kompleks, memanfaatkan localStorage browser untuk penyimpanan data sementara.

Website ini memiliki tampilan responsif (mobile-friendly), fitur keranjang belanja, dan integrasi checkout langsung ke WhatsApp.

✨ Fitur Utama

🛒 Untuk Pengunjung (User)

Katalog Produk Interaktif: Tampilan grid produk yang rapi dengan label stok dan diskon (Sale).

Pencarian Real-time: Fitur pencarian produk tanpa reload halaman.

Detail Produk (Modal): Pop-up untuk melihat detail, memilih Ukuran (Size), dan Warna.

Logic Harga: Harga otomatis bertambah untuk ukuran XL (+10rb) dan XXL (+20rb).

Keranjang Belanja (Shopping Cart):

Menambah item ke keranjang.

Menghapus item.

Data keranjang tersimpan di browser (localStorage), jadi tidak hilang saat di-refresh.

WhatsApp Checkout: Pesanan diformat otomatis menjadi pesan teks rapi dan dikirim langsung ke WhatsApp admin.

Halaman Informatif: Home, Products, Sale, FAQ, dan About Us.

👨‍💻 Untuk Admin (Pengelola Toko)

Login Aman: Modal login tersembunyi untuk akses admin.

Manajemen Produk (CRUD):

Tambah Produk: Input nama, kategori, harga, stok, dan deskripsi.

Edit Harga & Sale: Mengatur harga normal dan harga diskon.

Manajemen Stok: Menambah atau mengurangi stok barang dengan mudah.

Hapus Produk: Menghapus produk dari katalog.

Indikator Stok: Produk otomatis ditandai "Sold Out" atau "Low Stock".

🛠️ Teknologi yang Digunakan

HTML5: Struktur semantik halaman.

CSS3: Styling modern dengan variabel CSS (:root), Flexbox, dan Grid Layout.

JavaScript (Vanilla): Logika aplikasi, manipulasi DOM, dan manajemen localStorage.

Font Awesome: Ikon antarmuka (CDN).

Google Fonts: Tipografi menggunakan font Inter.

🚀 Cara Menjalankan Project

Project ini bersifat Statis, artinya Anda tidak perlu menginstall Node.js, PHP, atau database server.

Clone Repository ini:

git clone [https://github.com/username-anda/rahata-store.git](https://github.com/username-anda/rahata-store.git)


Buka File:
Masuk ke folder project dan klik ganda file index.html untuk membukanya di browser (Chrome, Firefox, Edge, dll).

🔐 Kredensial Admin (Login)

Untuk mencoba fitur Admin, klik tombol ikon User/Orang di pojok kanan atas navbar (sebelah ikon tas belanja), lalu masukkan data berikut:

Username: admin

Password: mhmdrhn777

Catatan: Setelah login, tombol-tombol edit (Edit, +Stock, Sale, Delete) akan muncul di setiap kartu produk, dan panel "Add Product" akan muncul di halaman Products.

📂 Struktur Folder

rahata-store/
│
├── index.html          # File utama aplikasi (Semua logika ada di sini)
├── README.md           # Dokumentasi project
└── static/
    └── images/         # Folder untuk menyimpan gambar produk
        ├── logo-text.png
        ├── hoodie1.jpg
        ├── hoodie2.jpg
        └── ...


📝 Catatan Pengembang

Data produk disimpan sementara dalam variabel JavaScript. Jika Anda melakukan Hard Refresh atau membersihkan Cache browser, data produk akan kembali ke data awal (default). Untuk penggunaan jangka panjang, disarankan menghubungkan aplikasi ini ke database seperti Firebase atau MySQL.

Dibuat dengan ❤️ untuk Rahata Store.
