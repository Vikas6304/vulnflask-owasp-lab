from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "vulnerable_secret_key"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        user = db.execute(query).fetchone()

        if user:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/labs")
def labs():
    return render_template("labs.html")

@app.route("/labs/a01")
def a01_lab():
    return render_template("a01.html")

@app.route("/labs/a03")
def a03_lab():
    return render_template("a03.html")

@app.route("/labs/a07")
def a07_lab():
    return render_template("a07.html")

@app.route("/labs/a05")
def a05_lab():
    return render_template("a05.html")

@app.route("/misconfig-error")
def misconfig_error():
    # Intentional error to expose stack trace
    return 1 / 0


if __name__ == "__main__":
    app.run(debug=True)
