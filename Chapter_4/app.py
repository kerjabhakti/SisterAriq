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