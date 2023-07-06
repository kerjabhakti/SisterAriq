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