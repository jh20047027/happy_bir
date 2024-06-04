from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store username and password
user_credentials = {
    'admin': '123',  # Example credentials, replace with your own
    'user1': '123456',
    # Add more username-password pairs as needed
}

@app.route('/')
def index():
    return render_template('1.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['account']
    password = request.form['pwd']

    # Check if the username exists and the password is correct
    if username in user_credentials and user_credentials[username] == password:
        # Authentication successful, redirect to success page
        return redirect(url_for('success'))
    else:
        # Authentication failed, redirect back to login page with error message
        return redirect(url_for('index', error='Invalid username or password'))

@app.route('/success')
def success():
    return "Login successful!"  # You can render a success page here if you want

if __name__ == '__main__':
    app.run(debug=True)
