from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/hello")
def hello():
    return "<h1>Hello, Flask!</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)