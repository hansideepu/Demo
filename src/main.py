from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return f"Login successful, Hello {user}"
    else:
        user = request.args.get('nm')
        return f"Login successful, Hello {user}"


if __name__ == "__main__":
    app.run()
