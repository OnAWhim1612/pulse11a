from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, static_url_path='/static', static_folder='static')



@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/u_login')
def u_login():
    return render_template('u_login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/friends/mositmaker')
def moistmaker():
    return render_template('friends/moistmaker.html')

@app.route('/friends/quiz1')
def quiz1():
    return render_template('friends/quiz1.html')

@app.route('/bbt/bbtquiz1')
def bbtquiz1():
    return render_template('bbt/bbbtquiz1.html')

@app.route('/bbt/bbtquiz2')
def bbtquiz2():
    return render_template('bbt/bbtquiz2.html')

if __name__ == '__main__':
    app.run(debug=True)

