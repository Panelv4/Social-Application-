# -*- coding: utf-8 -*-
"""
Hariom Physio Care — full website for Dr. Hariom Sharma (Physiotherapist)

Run:   python3 App.py          (serves on 0.0.0.0:8080)
Admin: /admin  (default login admin / admin123 — override with env vars)
"""

import os
import re
import sqlite3
import uuid
from datetime import date, datetime

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from clinic_data import (
    BLOG_POSTS,
    CLINIC,
    DOCTOR,
    FAQS,
    PROCESS_STEPS,
    SERVICES,
    STATS,
    TESTIMONIALS,
    TIME_SLOTS,
    WHY_CHOOSE,
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "clinic.db")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "hariom-physio-care-dev-secret-key")

ADMIN_USERNAME = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASS", "admin123")

APPOINTMENT_STATUSES = ("pending", "confirmed", "completed", "cancelled")


# ---------------------------------------------------------------- database

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS appointments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_code TEXT UNIQUE,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            service TEXT NOT NULL,
            appt_date TEXT NOT NULL,
            appt_time TEXT NOT NULL,
            notes TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            subject TEXT,
            body TEXT NOT NULL,
            is_read INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()


init_db()


# ---------------------------------------------------------------- helpers

def service_by_slug(slug):
    for s in SERVICES:
        if s["slug"] == slug:
            return s
    return None


def blog_by_slug(slug):
    for b in BLOG_POSTS:
        if b["slug"] == slug:
            return b
    return None


def phone_ok(value):
    digits = re.sub(r"\D", "", value or "")
    return 10 <= len(digits) <= 13


@app.context_processor
def inject_globals():
    return {
        "clinic": CLINIC,
        "doctor": DOCTOR,
        "current_year": datetime.now().year,
    }


# ---------------------------------------------------------------- pages

@app.route("/")
def home():
    return render_template(
        "index.html",
        services=SERVICES,
        stats=STATS,
        why=WHY_CHOOSE,
        steps=PROCESS_STEPS,
        testimonials=TESTIMONIALS,
        posts=BLOG_POSTS[:3],
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/services/<slug>")
def service_detail(slug):
    service = service_by_slug(slug)
    if not service:
        abort(404)
    related = [s for s in SERVICES if s["slug"] != slug][:3]
    return render_template(
        "service_detail.html",
        service=service,
        related=related,
        faqs=FAQS,
    )


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=BLOG_POSTS)


@app.route("/blog/<slug>")
def blog_post(slug):
    post = blog_by_slug(slug)
    if not post:
        abort(404)
    others = [b for b in BLOG_POSTS if b["slug"] != slug][:3]
    return render_template("blog_post.html", post=post, others=others)


# ---------------------------------------------------------------- appointments

@app.route("/book", methods=["GET", "POST"])
def book_appointment():
    form = dict(request.form) if request.method == "POST" else {}

    if request.method == "POST":
        errors = []
        name = (form.get("name") or "").strip()
        phone = (form.get("phone") or "").strip()
        email = (form.get("email") or "").strip()
        service = (form.get("service") or "").strip()
        appt_date = (form.get("date") or "").strip()
        appt_time = (form.get("time") or "").strip()
        notes = (form.get("notes") or "").strip()

        if not name:
            errors.append("Please enter your full name.")
        if not phone_ok(phone):
            errors.append("Please enter a valid phone number (at least 10 digits).")
        if email and ("@" not in email or "." not in email.split("@")[-1]):
            errors.append("Please enter a valid email address or leave it blank.")
        if service not in [s["name"] for s in SERVICES] + ["General Physiotherapy Consultation"]:
            errors.append("Please choose a service.")
        try:
            d = datetime.strptime(appt_date, "%Y-%m-%d").date()
            if d < date.today():
                errors.append("Appointment date cannot be in the past.")
        except ValueError:
            errors.append("Please choose a valid appointment date.")
        if appt_time not in TIME_SLOTS:
            errors.append("Please choose a preferred time slot.")

        if errors:
            for e in errors:
                flash(e, "error")
        else:
            ref = "HPC-" + uuid.uuid4().hex[:6].upper()
            conn = get_db()
            conn.execute(
                """
                INSERT INTO appointments(
                    ref_code, name, phone, email, service,
                    appt_date, appt_time, notes, status, created_at
                ) VALUES (?,?,?,?,?,?,?,?, 'pending', ?)
                """,
                (
                    ref,
                    name,
                    phone,
                    email,
                    service,
                    appt_date,
                    appt_time,
                    notes,
                    datetime.now().strftime("%Y-%m-%d %H:%M"),
                ),
            )
            conn.commit()
            conn.close()
            return render_template(
                "appointment_success.html",
                appt={
                    "ref_code": ref,
                    "name": name,
                    "phone": phone,
                    "service": service,
                    "appt_date": d.strftime("%d %B %Y"),
                    "appt_time": appt_time,
                },
            )

    return render_template(
        "appointment.html",
        services=SERVICES,
        time_slots=TIME_SLOTS,
        faqs=FAQS,
        form=form,
        selected_service=form.get("service") or request.args.get("service") or "",
        today_iso=date.today().isoformat(),
    )


# ---------------------------------------------------------------- contact

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        body = (request.form.get("message") or "").strip()
        email = (request.form.get("email") or "").strip()
        phone = (request.form.get("phone") or "").strip()
        subject = (request.form.get("subject") or "").strip() or "General enquiry"

        if not name or not body:
            flash("Please provide your name and a message.", "error")
        else:
            conn = get_db()
            conn.execute(
                """
                INSERT INTO messages(name, email, phone, subject, body, created_at)
                VALUES (?,?,?,?,?,?)
                """,
                (name, email, phone, subject, body,
                 datetime.now().strftime("%Y-%m-%d %H:%M")),
            )
            conn.commit()
            conn.close()
            flash(
                "Thank you! Your message has been received — the clinic will "
                "reply within one working day.",
                "success",
            )
            return redirect(url_for("contact"))

    return render_template("contact.html")


# ---------------------------------------------------------------- admin

def admin_required(fn):
    from functools import wraps

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("admin"):
            flash("Please log in to access the admin dashboard.", "info")
            return redirect(url_for("admin_login"))
        return fn(*args, **kwargs)

    return wrapper


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        u = (request.form.get("username") or "").strip()
        p = request.form.get("password") or ""
        if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
            session["admin"] = True
            flash("Welcome back, Dr. Sharma.", "success")
            return redirect(url_for("admin_dashboard"))
        flash("Invalid username or password.", "error")
    if session.get("admin"):
        return redirect(url_for("admin_dashboard"))
    return render_template("admin/login.html")


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("admin_login"))


@app.route("/admin")
@admin_required
def admin_dashboard():
    conn = get_db()
    appts = conn.execute(
        "SELECT * FROM appointments ORDER BY appt_date ASC, id DESC"
    ).fetchall()
    msgs = conn.execute(
        "SELECT * FROM messages ORDER BY id DESC"
    ).fetchall()
    conn.close()

    today = date.today().isoformat()
    stats = {
        "total": len(appts),
        "pending": sum(1 for a in appts if a["status"] == "pending"),
        "today": sum(1 for a in appts if a["appt_date"] == today and a["status"] != "cancelled"),
        "messages": sum(1 for m in msgs if not m["is_read"]),
    }
    return render_template(
        "admin/dashboard.html",
        appts=appts,
        msgs=msgs,
        stats=stats,
        statuses=APPOINTMENT_STATUSES,
    )


@app.route("/admin/appointment/<int:aid>/status", methods=["POST"])
@admin_required
def admin_update_status(aid):
    status = request.form.get("status")
    if status in APPOINTMENT_STATUSES:
        conn = get_db()
        conn.execute(
            "UPDATE appointments SET status=? WHERE id=?", (status, aid)
        )
        conn.commit()
        conn.close()
        flash(f"Appointment #{aid} marked as {status}.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/message/<int:mid>/read", methods=["POST"])
@admin_required
def admin_toggle_read(mid):
    conn = get_db()
    conn.execute("UPDATE messages SET is_read = 1 - is_read WHERE id=?", (mid,))
    conn.commit()
    conn.close()
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/message/<int:mid>/delete", methods=["POST"])
@admin_required
def admin_delete_message(mid):
    conn = get_db()
    conn.execute("DELETE FROM messages WHERE id=?", (mid,))
    conn.commit()
    conn.close()
    flash("Message deleted.", "info")
    return redirect(url_for("admin_dashboard"))


# ---------------------------------------------------------------- errors

@app.errorhandler(404)
def page_not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False,
    )
