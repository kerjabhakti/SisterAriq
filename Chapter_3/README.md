# Studi Kasus Flask - Pendaftaran Pengguna

Berikut adalah contoh studi kasus menggunakan Flask untuk membuat fitur pendaftaran pengguna sederhana:

```ruby
from flask import Flask, render_template , request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #PROSES PENDAFTARAN 
        return f"Terimakasih atas pendaftaran, {username}!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
```

## Deskripsi

Aplikasi ini menggunakan framework Flask untuk membuat route /register yang mengizinkan pengguna untuk mendaftar dengan mengirimkan formulir dengan username dan password. Jika metode yang digunakan adalah POST, aplikasi akan melakukan proses pendaftaran pengguna dan menampilkan pesan terima kasih. Jika metode yang digunakan adalah GET, aplikasi akan merender template register.html yang berisi formulir pendaftaran.

## Penggunaan

1. Pastikan Anda telah menginstal Flask dengan menjalankan perintah pip install flask.

2. Buat file template/register.html dengan konten berikut:

```ruby
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Register</title>
  </head>
  <body>
    <h1>Registration Form</h1>
    <form method="POST" action="/register">
      <label for="username">Username:</label>
      <input type="text" name="username" id="username" required /><br /><br />

      <label for="password">Password:</label>
      <input
        type="password"
        name="password"
        id="password"
        required
      /><br /><br />

      <input type="submit" value="Register" />
    </form>
  </body>
</html>
```

3. Simpan kode Flask di atas dalam file dengan nama app.py.

4. Jalankan aplikasi dengan menjalankan perintah python app.py.

5. Akses URL http://localhost:5000/register di web browser.

6. Anda akan melihat halaman web yang berisi formulir pendaftaran pengguna.

7. Isi formulir dengan username dan password, lalu klik tombol "Register".

8. Anda akan melihat halaman yang menampilkan pesan terima kasih atas pendaftaran.

## Penjelasan

- from flask import Flask, render_template, request mengimpor kelas Flask, render_template, dan request dari modul Flask.
- app = Flask(__name__) membuat objek Flask dengan nama aplikasi yang sama dengan nama modul ini.
- @app.route('/register', methods=['GET', 'POST']) adalah dekorator yang mendefinisikan route /register dengan metode GET dan POST.
- def register(): adalah fungsi view yang akan dijalankan ketika route /register diakses.
- if request.method == 'POST': adalah kondisi untuk memeriksa apakah metode yang digunakan adalah POST.
- username = request.form['username'] dan password = request.form['password'] digunakan untuk mengambil nilai username dan password yang dikirimkan melalui formulir.
- return f"Terimakasih atas pendaftaran, {username}!" adalah pernyataan yang mengembalikan pesan terima kasih kepada pengguna setelah proses pendaftaran.
- return render_template('register.html') merender template register.html jika metode yang digunakan adalah GET.
- if __name__ == '__main__': memastikan bahwa server web hanya dijalankan jika file ini dijalankan langsung, bukan diimpor sebagai modul.
- app.run() menjalankan server web untuk melayani permintaan HTTP.

<br />

Template register.html berisi formulir pendaftaran pengguna dengan dua input fields untuk username dan password. Ketika formulir dikirimkan, data akan dikirim ke route /register dengan metode POST untuk diproses.