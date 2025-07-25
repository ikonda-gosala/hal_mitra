from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'halmtra_secret_key'

# ---- register page ----
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists. Please choose a different one."

    return render_template('register.html')

# ---- login page ----
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid Credentials'

    return render_template('login.html')



# ---- Dashboard ----
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# --- result ----
@app.route('/result', methods=['GET', 'POST'])
def result():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        land_number = request.form.get('land_number')
        land_type = request.form.get('land_type')

        conn = sqlite3.connect('soil_data.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT land_number, country, land_type, crop, season, water_capacity FROM soil_info WHERE land_number=? AND land_type=?",
            (land_number, land_type)
        )
        data = cursor.fetchone()
        conn.close()

        if data:
            land_number, country, land_type, crop, season, water_capacity = data
            return render_template('result.html', land_number=land_number,country=country,land_type=land_type, crop=crop, season=season, water_capacity=water_capacity)
        else:
            return "No data found for the given input."

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


    
if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)
