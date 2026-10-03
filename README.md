# Hariom Physio Care — Physiotherapy Website

A complete, production-style website for **Dr. Hariom Sharma (BPT, MPT Orthopaedics) — Physiotherapist**,
built with **Flask + SQLite** and a fully custom responsive front-end (no CSS framework).

## Features

- **Home** — hero with clinic highlights, stats, about preview, 8 services, "why choose us",
  4-step recovery process, auto-rotating patient testimonials, blog preview and call-to-action bands.
- **About** — doctor biography, qualifications & certifications, career highlights, treatment philosophy.
- **Services** — 8 specialised service pages (orthopedic, sports injury, neurological, post-surgical,
  manual therapy, electrotherapy, home visits, posture & ergonomics) with benefits and FAQs.
- **Online Appointment Booking** — validated booking form (name / phone / service / date / time slot)
  that stores requests in SQLite and returns a reference code (e.g. `HPC-A1B2C3`) on a confirmation page.
- **Blog / Health Library** — 4 physiotherapist-written articles with article pages and author card.
- **Contact** — enquiry form, clinic info cards and embedded OpenStreetMap.
- **Admin Dashboard** (`/admin`, default login `admin` / `admin123`) — view appointment requests,
  update their status (pending / confirmed / completed / cancelled), and read/delete contact messages.
- Floating **WhatsApp** button, click-to-call links, sticky navbar, mobile menu,
  scroll-reveal animations, custom 404 page.

## Run it

```bash
bash run.sh           # installs Flask if missing, serves http://0.0.0.0:8080
```

or manually:

```bash
pip install -r Requirements.txt
python3 App.py        # serves http://0.0.0.0:8080
```

Then open the live preview or `http://localhost:8080`.

## Configuration

| What | Where |
|---|---|
| Phone, WhatsApp, email, address, hours, city | `clinic_data.py` → `CLINIC` |
| Doctor bio, qualifications, highlights | `clinic_data.py` → `DOCTOR` |
| Services, testimonials, blog posts, FAQs, time slots | `clinic_data.py` |
| Secret key | env `SECRET_KEY` |
| Admin credentials | env `ADMIN_USER` / `ADMIN_PASS` (default `admin` / `admin123`) |
| Port | env `PORT` (default `8080`) |

All website content is data-driven from `clinic_data.py` — edit the text there and the pages update
automatically; no template changes needed.

## Project structure

```
App.py                  # Flask application: routing, validation, SQLite, admin
clinic_data.py          # ALL website content (doctor, clinic, services, blog, testimonials)
templates/              # Jinja2 pages (base layout, macros/icons, pages, admin)
static/css/style.css    # complete design system (responsive: desktop / tablet / mobile)
static/js/main.js       # nav, scroll reveal, testimonial slider, flash dismissal
static/img/             # hero, doctor portrait, clinic interior
clinic.db               # created at first run (appointments + messages) — git-ignored
```

## Customising for go-live

The phone number, WhatsApp number, email, address, registration line and map embed in
`clinic_data.py` are realistic **placeholders** — replace them with Dr. Sharma's real contact
details before publishing. Social links live in `CLINIC["social"]`.

> Note: this repository previously contained a non-functional Flask social-app scaffold
> (no templates). It was replaced by this website; the original code remains in Git history
> at commit `e4d6029`.
