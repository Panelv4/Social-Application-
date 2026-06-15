from flask import Flask, render_template, request, redirect, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO
import sqlite3
import os
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

socketio = SocketIO(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp4", "mov"}

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# ---------------- DATABASE ----------------

conn = sqlite3.connect("database.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    content TEXT,
    media TEXT,
    created_at TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS likes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    user TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    user TEXT,
    text TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS follows(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    follower TEXT,
    following TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sparks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    media TEXT,
    created_at TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    receiver TEXT,
    message TEXT,
    created_at TEXT
)
""")

conn.commit()

# ---------------- HOME ----------------

@app.route("/")
def home():

    user = session.get("user")

    posts = cur.execute(
        "SELECT * FROM posts ORDER BY id DESC"
    ).fetchall()

    enriched = []
    comments = {}

    for p in posts:
        likes = cur.execute(
            "SELECT COUNT(*) FROM likes WHERE post_id=?",
            (p[0],)
        ).fetchone()[0]

        enriched.append(
            (p[0], p[1], p[2], p[3], likes)
        )

        comments[p[0]] = cur.execute(
            "SELECT user,text FROM comments WHERE post_id=?",
            (p[0],)
        ).fetchall()

    return render_template(
        "index.html",
        user=user,
        posts=enriched,
        comments=comments
    )

# ---------------- AUTH ----------------

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    try:
        cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (
                username,
                generate_password_hash(password)
            )
        )
        conn.commit()

    except:
        pass

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    row = cur.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    ).fetchone()

    if row and check_password_hash(row[0], password):
        session["user"] = username

    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- POSTS ----------------

@app.route("/post", methods=["POST"])
def post():

    if "user" not in session:
        return redirect("/")

    content = request.form.get("content", "")
    file = request.files.get("media")

    filename = None

    if file and allowed_file(file.filename):
        filename = (
            str(uuid.uuid4()) + "_" +
            secure_filename(file.filename)
        )

        file.save(
            os.path.join(
                UPLOAD_FOLDER,
                filename
            )
        )

    cur.execute(
        """
        INSERT INTO posts(
            user,
            content,
            media,
            created_at
        )
        VALUES(?,?,?,?)
        """,
        (
            session["user"],
            content,
            filename,
            str(datetime.now())
        )
    )

    conn.commit()

    return redirect("/")

# ---------------- LIKE ----------------

@app.route("/like/<int:pid>")
def like(pid):

    if "user" not in session:
        return redirect("/")

    existing = cur.execute(
        """
        SELECT *
        FROM likes
        WHERE post_id=? AND user=?
        """,
        (
            pid,
            session["user"]
        )
    ).fetchone()

    if not existing:
        cur.execute(
            """
            INSERT INTO likes(
                post_id,
                user
            )
            VALUES(?,?)
            """,
            (
                pid,
                session["user"]
            )
        )

        conn.commit()

    return redirect("/")

# ---------------- COMMENT ----------------

@app.route(
    "/comment/<int:pid>",
    methods=["POST"]
)
def comment(pid):

    if "user" not in session:
        return redirect("/")

    text = request.form["text"]

    cur.execute(
        """
        INSERT INTO comments(
            post_id,
            user,
            text
        )
        VALUES(?,?,?)
        """,
        (
            pid,
            session["user"],
            text
        )
    )

    conn.commit()

    return redirect("/")

# ---------------- FOLLOW ----------------

@app.route("/follow/<username>")
def follow(username):

    if "user" not in session:
        return redirect("/")

    me = session["user"]

    if me != username:

        exists = cur.execute(
            """
            SELECT *
            FROM follows
            WHERE follower=?
            AND following=?
            """,
            (
                me,
                username
            )
        ).fetchone()

        if not exists:

            cur.execute(
                """
                INSERT INTO follows(
                    follower,
                    following
                )
                VALUES(?,?)
                """,
                (
                    me,
                    username
                )
            )

            conn.commit()

    return redirect("/")

# ---------------- PROFILE ----------------

@app.route("/u/<username>")
def profile(username):

    posts = cur.execute(
        """
        SELECT *
        FROM posts
        WHERE user=?
        ORDER BY id DESC
        """,
        (username,)
    ).fetchall()

    followers = cur.execute(
        """
        SELECT COUNT(*)
        FROM follows
        WHERE following=?
        """,
        (username,)
    ).fetchone()[0]

    following = cur.execute(
        """
        SELECT COUNT(*)
        FROM follows
        WHERE follower=?
        """,
        (username,)
    ).fetchone()[0]

    return render_template(
        "profile.html",
        profile_user=username,
        posts=posts,
        followers=followers,
        following=following
    )

# ---------------- UPLOADS ----------------

@app.route("/uploads/<path:name>")
def uploads(name):
    return send_from_directory(
        UPLOAD_FOLDER,
        name
    )

if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=8080,
        debug=True
      )
