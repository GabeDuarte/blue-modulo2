from flask import Flask
app= Flask(__name__)


@app.route("/")
def home():
    return f"Hello, Gabriel {(284-22)}"
    


if __name__ == "__main__":
    app.run(debug=True)