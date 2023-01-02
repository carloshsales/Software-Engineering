from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "index"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = "world"):
    str = f"<h1> Hello {name}!</h1>"
    return str


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "Login success!"
    # if request.method == 'GET':
    #     return "Login page"
    return render_template("index.html")



if __name__ == "__main__":
    app.run()