from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    # Dalam praktik nyata, data produk biasanya diambil dari database di sini
    # Namun untuk demo ini, data ditaruh di frontend (JavaScript) agar interaktif
    return render_template('index.html')

if __name__ == '__main__':
    # Jalankan aplikasi pada port 5000
    app.run(debug=True, port=5000)