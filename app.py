from flask import Flask, render_template

app = Flask("__name__", template_folder='templates')

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/writings")
def quem():
    return render_template("writings.html")

@app.route("/pictures")
def contato():
    return render_template("pictures.html")

if __name__ == "__main__":
    app.run(debug=True)