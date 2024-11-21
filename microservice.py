from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'this_is_my_app'  # Replace with a secure secret key

users_db = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists in the "database" and password matches
        if username in users_db and users_db[username] == password:
            session['username'] = username
            return render_template('welcome.html', message="Welcome back!")
        else:
            return "Invalid login input, please try again."

    return render_template('login_page.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user already exists
        if username in users_db:
            return "Username already exists. Please choose another."
        else:
            # Save the user in the "database"
            users_db[username] = password
            session['username'] = username
            return render_template('welcome.html', message="Welcome new user!")

    return render_template('signup_page.html')

if __name__ == '__main__':
    app.run(debug=True)
