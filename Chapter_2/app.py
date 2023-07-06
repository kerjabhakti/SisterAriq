from flask import Flask, render_template

app = Flask(__name__)

tasks = [ 'Task 1', 'Task 2', 'Task 3']

@app.route('/tasks')
def task_list():
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run()