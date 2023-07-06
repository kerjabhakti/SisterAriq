# Studi Kasus Flask - Manajemen Tugas (Task Management)

Berikut adalah contoh studi kasus menggunakan Flask untuk membuat RESTful API untuk manajemen tugas (task management):

```ruby
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    "Task 1",
    "Task 2",
    "Task 3"
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    task = request.json['task']
    tasks.append(task)
    return jsonify({'message': 'Task created'})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task = request.json['task']
    tasks[task_id] = new_task
    return jsonify({'message': 'Task updated'})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    del tasks[task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run()
```

## Deskripsi

Aplikasi ini menggunakan framework Flask untuk membuat RESTful API untuk manajemen tugas. Aplikasi ini memiliki beberapa endpoint yang memungkinkan pengguna untuk mengambil, membuat, memperbarui, dan menghapus tugas.

- Endpoint /api/tasks dengan metode GET digunakan untuk mengambil daftar tugas yang ada.
- Endpoint /api/tasks dengan metode POST digunakan untuk membuat tugas baru.
- Endpoint /api/tasks/<task_id> dengan metode PUT digunakan untuk memperbarui tugas yang sudah ada berdasarkan ID tugas.
- Endpoint /api/tasks/<task_id> dengan metode DELETE digunakan untuk menghapus tugas yang sudah ada berdasarkan ID tugas.

## Penggunaan

1. Pastikan Anda telah menginstal Flask dengan menjalankan perintah pip install flask.
2. Simpan kode Flask di atas dalam file dengan nama app.py.
3. Jalankan aplikasi dengan menjalankan perintah python app.py.
4. Aplikasi akan berjalan dan menyediakan API untuk manajemen tugas.
5. Anda dapat mengakses endpoint-endpoint berikut untuk berinteraksi dengan aplikasi:

- GET /api/tasks: Mengambil daftar tugas yang ada.
- POST /api/tasks: Membuat tugas baru.
- PUT /api/tasks/<task_id>: Memperbarui tugas yang ada berdasarkan ID tugas.
- DELETE /api/tasks/<task_id>: Menghapus tugas yang ada berdasarkan ID tugas.
  <br />
  Anda dapat menggunakan Postman atau alat sejenis untuk menguji dan berinteraksi dengan API tersebut.

## Penjelasan

- from flask import Flask, jsonify, request mengimpor kelas-kelas dan fungsi yang diperlukan dari modul Flask.
- app = Flask(**name**) membuat objek Flask dengan nama aplikasi yang sama dengan nama modul ini.
- tasks = [...] adalah daftar tugas sederhana yang akan digunakan sebagai sumber data.
- @app.route('/api/tasks', methods=['GET']) mendefinisikan route /api/tasks dengan metode GET.
- Fungsi get_tasks() akan dijalankan ketika route /api/tasks diakses dengan metode GET. Fungsi ini akan mengembalikan daftar tugas dalam format JSON.
- @app.route('/api/tasks', methods=['POST']) mendefinisikan route /api/tasks dengan metode POST.
- Fungsi create_task() akan dijalankan ketika route /api/tasks diakses dengan metode POST. Fungsi ini akan membuat tugas baru berdasarkan data yang dikirimkan melalui request JSON.
- @app.route('/api/tasks/<int:task_id>', methods=['PUT']) mendefinisikan route /api/tasks/<task_id> dengan metode PUT.
- Fungsi update_task() akan dijalankan ketika route /api/tasks/<task_id> diakses dengan metode PUT. Fungsi ini akan memperbarui tugas yang ada berdasarkan ID tugas yang diberikan.
- @app.route('/api/tasks/<int:task_id>', methods=['DELETE']) mendefinisikan route /api/tasks/<task_id> dengan metode DELETE.
- Fungsi delete_task() akan dijalankan ketika route /api/tasks/<task_id> diakses dengan metode DELETE. Fungsi ini akan menghapus tugas yang ada berdasarkan ID tugas yang diberikan.

<br />
Anda dapat mengadaptasi studi kasus ini dengan menambahkan validasi, penyimpanan data ke basis data, atau logika bisnis tambahan sesuai dengan kebutuhan aplikasi manajemen tugas Anda.
