# captcha-service

# Django CAPTCHA Service

A simple Django-based CAPTCHA service designed to secure a web-based application by preventing automated attacks. This project demonstrates the generation, integration, and verification of CAPTCHA using Django and Python.

---

## Features

- Dynamic CAPTCHA image generation using Python and Pillow.
- Secure validation of CAPTCHA with Django sessions.
- User-friendly web interface for CAPTCHA input and validation.
- Modular design for easy extension and integration.

---

## Project Overview

The project contains the following components:

captcha_project/
├── captcha_app/
│   ├── migrations/
│   ├── templates/
│   │   └── captcha_app/
│   │       └── index.html         # HTML template for CAPTCHA form
│   ├── static/
│   │   └── captcha_images/        # Folder for generated CAPTCHA images
│   ├── forms.py                   # Django forms for CAPTCHA input
│   ├── utils.py                   # CAPTCHA generation logic
│   ├── views.py                   # Views for CAPTCHA rendering and verification
│   ├── urls.py                    # URL patterns for the app
│   └── __init__.py                # App initialization file
├── captcha_project/
│   ├── settings.py                # Main project settings
│   ├── urls.py                    # Root URL configurations
│   ├── wsgi.py                    # WSGI entry point
│   └── asgi.py                    # ASGI entry point (optional)
├── templates/
│   └── base.html                  # Optional base template (if used globally)
├── static/
│   ├── css/                       # CSS files (optional)
│   ├── js/                        # JavaScript files (optional)
│   └── captcha_images/            # Dynamically generated CAPTCHA images
├── db.sqlite3                     # SQLite database file (auto-generated after migrations)
├── manage.py                      # Django management script
└── README.md                      # Project documentation
