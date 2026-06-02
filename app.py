from flask import Flask, render_template, request


app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    users[username] = {
    "email": email,
    "password": password
}
    
    return f"Mr/Miss {username} your registered successfully ✅"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]["password"] == password:
        return "Login Successful ✅"
    else:
        return "Invalid Username or Password ❌"
    
if __name__ == '__main__':
    app.run(debug=True)