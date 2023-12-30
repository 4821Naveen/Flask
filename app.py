from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)


# MySQL configuration
db_config = {
    'host': 'sql8.freesqldatabase.com ',
    'user': 'sql8673726',
    'password': 'xWplLT4LMV',
    'database': 'sql8673726'
}

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        typegroup = request.form['typegroup']
        gender = request.form['genter']

        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert user into the database
        cursor.execute("INSERT INTO users (Name, Email, Mobile, Typegroup, Gender) VALUES (%s ,%s ,%s ,%s )", (name, email, mobile, typegroup, gender))
        conn.commit()

        # Close MySQL connection
        cursor.close()
        conn.close()

        return redirect(url_for('home'))

    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

#1oQ25KzvvqZwR2Bd