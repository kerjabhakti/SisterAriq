#  Studi Kasus Flask - Login dan Daftar Tugas

Berikut adalah contoh studi kasus menggunakan Flask untuk membuat fitur login pengguna dan daftar tugas:

```ruby
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] ='secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
tasks = [ 'Task 1', 'Task 2', 'Task 3']

class User(UserMixin):
    def __init__ (self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'POST':
        user_id = request.form['user_id']
        #proses auth pengguna
        user = User(user_id)
        login_user(user)
        return redirect(url_for('task_list'))
    return render_template('login.html')

@app.route('/tasks')
@login_required

def task_list():
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    login_manager.init_app(app)
    app.run()
```

## Deskripsi

Aplikasi ini menggunakan framework Flask dan ekstensi Flask-Login untuk membuat fitur login pengguna dan daftar tugas sederhana. Aplikasi ini memiliki halaman login yang mengizinkan pengguna untuk memasukkan ID pengguna, dan halaman daftar tugas yang hanya dapat diakses oleh pengguna yang sudah login.

## Penggunaan

1. Pastikan Anda telah menginstal Flask dan Flask-Login dengan menjalankan perintah pip install flask flask-login.

2. Simpan kode Flask di atas dalam file dengan nama app.py.

3. Buat file templates/login.html dengan konten berikut:
```ruby
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login</title>
  </head>
  <body>
    <h1>Login</h1>
    <form method="POST" action="/login">
      <label for="user_id">User ID:</label>
      <input type="text" name="user_id" id="user_id" required /><br /><br />

      <input type="submit" value="Login" />
    </form>
  </body>
</html>
```
4. Buat file templates/tasks.html dengan konten berikut:
```ruby
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Task</title>
  </head>
  <body>
    <h1>Task List</h1>
    <ul>
    {% for task in tasks %}
      {{task}}
    {% endfor %}
    </ul>
  </body>
</html>
```

5. Jalankan aplikasi dengan menjalankan perintah python app.py.

6. Akses URL http://localhost:5000/login di web browser.

7. Anda akan melihat halaman login yang berisi form untuk memasukkan ID pengguna.

8. Masukkan ID pengguna apa pun dan klik tombol "Login".

9. Anda akan diarahkan ke halaman daftar tugas yang menampilkan tugas-tugas yang ada.

## Penjelasan

- from flask import Flask, render_template, request, redirect, url_for mengimpor kelas-kelas dan fungsi yang diperlukan dari modul Flask.
- from flask_login import LoginManager, login_required, login_user, UserMixin mengimpor kelas-kelas dan fungsi yang diperlukan dari ekstensi Flask-Login.
- app = Flask(__name__) membuat objek Flask dengan nama aplikasi yang sama dengan nama modul ini.
- app.config['SECRET_KEY'] = 'secret_key' mengatur kunci rahasia yang digunakan oleh Flask-Login.
- login_manager = LoginManager(app) membuat objek LoginManager yang digunakan untuk mengelola login pengguna.
- login_manager.login_view = 'login' mengatur route yang akan digunakan untuk halaman login.
- tasks = ['Task 1', 'Task 2', 'Task 3'] adalah daftar tugas yang akan ditampilkan di halaman daftar tugas.
- class User(UserMixin) mendefinisikan kelas User yang mewarisi dari UserMixin untuk mengimplementasikan metode-metode yang diperlukan oleh Flask-Login.
- @login_manager.user_loader adalah decorator yang mendefinisikan fungsi load_user untuk memuat pengguna berdasarkan ID pengguna.
- @app.route('/login', methods=['GET', 'POST']) mendefinisikan route /login yang akan digunakan untuk halaman login.
- @app.route('/tasks') mendefinisikan route /tasks yang akan digunakan untuk halaman daftar tugas.
- @login_required adalah decorator yang memastikan hanya pengguna yang sudah login yang dapat mengakses halaman daftar tugas.
- def login() adalah fungsi view untuk halaman login.
- def task_list() adalah fungsi view untuk halaman daftar tugas.
- if __name__ == '__main__': memastikan bahwa server web hanya dijalankan jika file ini dijalankanlangsung, bukan diimpor sebagai modul.

<br />
Template login.html berisi form login sederhana yang meminta pengguna memasukkan ID pengguna. Ketika formulir dikirimkan, data akan dikirim ke route /login untuk diproses.
<br />
Template tasks.html menampilkan daftar tugas yang diberikan dalam variabel tasks. Template menggunakan perulangan {% for task in tasks %} untuk mengulang setiap tugas dalam daftar dan menampilkannya dalam elemen <li>.
<br />
Dalam aplikasi ini, tidak ada proses autentikasi yang sebenarnya. Pengguna hanya perlu memasukkan ID pengguna apa pun untuk masuk dan melihat daftar tugas.
<br />
Anda dapat mengadaptasi studi kasus ini dengan menambahkan logika autentikasi sesuai dengan kebutuhan aplikasi Anda, seperti memeriksa ID pengguna dan kata sandi yang valid dari basis data atau sumber data lainnya.