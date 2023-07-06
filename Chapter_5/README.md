# Studi Kasus Flask - Catatan

Berikut adalah contoh studi kasus menggunakan Flask dan Flask-SQLAlchemy untuk membuat aplikasi catatan sederhana:

```ruby
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()
    notes = Note.query.all()
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
```

## Deskripsi
Aplikasi ini menggunakan framework Flask dan ekstensi Flask-SQLAlchemy untuk membuat aplikasi catatan sederhana. Aplikasi ini memiliki halaman /notes yang memungkinkan pengguna untuk membuat catatan baru dan menampilkan daftar catatan yang ada.

## Penggunaan

1. Pastikan Anda telah menginstal Flask dan Flask-SQLAlchemy dengan menjalankan perintah pip install flask flask-sqlalchemy.

2. Simpan kode Flask di atas dalam file dengan nama app.py.

3. Jalankan perintah flask db init untuk menginisialisasi migrasi basis data (pastikan Anda telah menginstal Flask-Migrate terlebih dahulu).

4. Jalankan perintah flask db migrate untuk membuat file migrasi awal.

5. Jalankan perintah flask db upgrade untuk menerapkan migrasi ke basis data.

6. Buat file templates/notes.html dengan konten berikut:
```ruby
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>
<body>
    <h1>Notes</h1>

    <form action="/notes" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>

        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="5" required></textarea><br>

        <button type="submit">Save Note</button>
    </form>

    <hr>

    <h2>All Notes</h2>

    {% for note in notes %}
        <h3>{{ note.title }}</h3>
        <p>{{ note.content }}</p>
        <hr>
    {% endfor %}
</body>
</html>
```

7. Jalankan aplikasi dengan menjalankan perintah python app.py.

8. Akses URL http://localhost:5000/notes di web browser.

9. Anda akan melihat halaman catatan yang berisi formulir untuk membuat catatan baru dan daftar catatan yang sudah ada.

10. Isi formulir dengan judul dan isi catatan, kemudian klik tombol "Save".

11. Catatan baru akan ditambahkan ke daftar catatan yang sudah ada dan ditampilkan di halaman.


## Penjelasan
- from flask import Flask, render_template, request mengimpor kelas-kelas dan fungsi yang diperlukan dari modul Flask.
- from flask_sqlalchemy import SQLAlchemy mengimpor kelas SQLAlchemy dari ekstensi Flask-SQLAlchemy.
- app = Flask(__name__) membuat objek Flask dengan nama aplikasi yang sama dengan nama modul ini.
- app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db' mengatur URI database SQLite yang akan digunakan.
- db = SQLAlchemy(app) membuat objek SQLAlchemy yang akan digunakan untuk berinteraksi dengan basis data.
- class Note(db.Model) mendefinisikan model Note yang akan digunakan untuk representasi catatan dalam basis data.
- @app.route('/notes', methods=['GET', 'POST']) mendefinisikan route /notes yang akan digunakan untuk halaman catatan.
- def notes() adalah fungsi view untuk halaman catatan.
- Pada method POST, catatan baru akan dibuat berdasarkan data yang dikirimkan melalui formulir, dan kemudian ditambahkan ke basis data menggunakan SQLAlchemy.
- Pada method GET, semua catatan yang ada akan diambil dari basis data menggunakan SQLAlchemy dan ditampilkan di halaman menggunakan template notes.html.
- Dalam blok if __name__ == '__main__':, migrasi basis data dijalankan menggunakan Flask-Migrate untuk membuat tabel catatan dalam basis data.

<br />
Anda dapat mengadaptasi studi kasus ini dengan menambahkan fitur-fitur lain, seperti mengedit dan menghapus catatan, serta melengkapi dengan tampilan dan logika yang lebih kompleks sesuai dengan kebutuhan aplikasi catatan Anda.

