# Studi Kasus Flask - Task List

Berikut adalah contoh studi kasus menggunakan Flask untuk membuat daftar tugas sederhana dengan menggunakan template:

```ruby
from flask import Flask, render_template

app = Flask(__name__)

tasks = [ 'Task 1', 'Task 2', 'Task 3']

@app.route('/tasks')
def task_list():
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
```
## Deskripsi

Aplikasi ini menggunakan framework Flask untuk membuat route /tasks yang akan menampilkan daftar tugas yang telah ditentukan sebelumnya. Template tasks.html digunakan untuk merender tampilan daftar tugas.

## Penggunaan

1. Pastikan Anda telah menginstal Flask dengan menjalankan perintah pip install flask.

2. Buat file templates/tasks.html dengan konten berikut:

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
3. Simpan kode Flask di atas dalam file dengan nama app.py.

4. Jalankan aplikasi dengan menjalankan perintah python app.py.

5. Akses URL http://localhost:5000/tasks di web browser.

6. Anda akan melihat halaman web yang menampilkan daftar tugas seperti yang telah ditentukan dalam variabel tasks.

## Penjelasan

- from flask import Flask, render_template mengimpor kelas Flask dan fungsi render_template dari modul Flask.
- app = Flask(__name__) membuat objek Flask dengan nama aplikasi yang sama dengan nama modul ini.
- tasks = ['Task 1', 'Task 2', 'Task 3'] mendefinisikan daftar tugas yang akan ditampilkan.
- @app.route('/tasks') adalah dekorator yang mendefinisikan route /tasks.
- def task_list(): adalah fungsi view yang akan dijalankan ketika route /tasks diakses.
- return render_template('tasks.html', tasks=tasks) merender template tasks.html dengan mengirimkan data tasks ke dalam template.
- if __name__ == '__main__': memastikan bahwa server web hanya dijalankan jika file ini dijalankan langsung, bukan diimpor sebagai modul.
- app.run() menjalankan server web untuk melayani permintaan HTTP.

<br />
Template tasks.html melalui daftar tasks dan menampilkan setiap elemen dalam elemen ```ruby <li>``` dalam elemen ```ruby <ul>```.