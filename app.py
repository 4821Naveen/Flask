from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)


# MySQL configuration
db_config = {
    'host': ' sql11.freesqldatabase.com',
    'user': 'sql11671602',
    'password': '4fmyucg7Ar',
    'database': 'sql11671602'
}

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email_id = request.form['enter_email']
        mobile_number = request.form['mobile_number']
        describe_your_website = request.form['describe_your_website']

        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert user into the database
        cursor.execute("INSERT INTO users (username, email_id, mobile_number, describe_your_website) VALUES (%s ,%s ,%s ,%s )", (username, email_id, mobile_number, describe_your_website))
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