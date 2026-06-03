from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()

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
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
     (username, email, password)
    )

    conn.commit()
    conn.close()
    
    return f"Mr/Miss {username} your registered successfully ✅"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
    )

    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login Successful ✅"
    else:
        return "Invalid Username or Password ❌"
    
if __name__ == '__main__':
    app.run(debug=True)