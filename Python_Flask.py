from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello")
def hello():
    return "<h1>Hello, Flask!</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)