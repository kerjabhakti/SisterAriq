#Studi Kasus: Menyapa Pengguna dengan Flask

Ini adalah contoh sederhana menggunakan Flask untuk membuat API yang menyapa pengguna berdasarkan nama yang diberikan.

##Langkah-langkah

1. Pastikan Anda telah menginstal Flask dengan menjalankan perintah pip install flask.

2. Buat file app.py dan salin kode berikut:

```ruby
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
        return f"Hello, {name}!"

if __name__ == '__main__':
    app.run()
```

3. Jalankan aplikasi Flask dengan menjalankan perintah python app.py.

4. Buka browser dan akses URL http://localhost:5000/hello/ariqrafikusumah (ganti "ariqrafikusumah" dengan nama pengguna lainnya). Anda akan melihat pesan "Hello, ariqrafikusumah!" atau "Hello, [nama pengguna]!".

##Penjelasan
- Pertama, kita mengimpor modul Flask dari paket flask.
- Selanjutnya, kita membuat objek Flask dengan menggunakan Flask(__name__). __name__ adalah variabel khusus yang digunakan oleh Python untuk mengidentifikasi nama modul saat ini.
- Kami mendefinisikan rute /hello/<name> dengan menggunakan dekorator @app.route(). Ini berarti rute tersebut akan menangani permintaan GET yang mengarah ke /hello/<name>, di mana <name> adalah parameter dinamis yang akan kita gunakan untuk menyapa pengguna.
- Fungsi hello(name) akan dijalankan ketika permintaan diterima ke rute /hello/<name>. Fungsi ini mengambil parameter name yang diberikan dalam URL dan mengembalikan pesan sapaan dengan menggunakan f-string.
- Terakhir, kita menjalankan aplikasi Flask dengan menggunakan app.run() jika file app.py dijalankan langsung.
<br />
Dengan mengikuti langkah-langkah di atas, Anda dapat membuat API sederhana yang menyapa pengguna berdasarkan nama yang diberikan melalui URL. Anda dapat mengganti pesan sapaan atau menambahkan fungsionalitas lain sesuai kebutuhan Anda.