# Login-Webpage

This project is a Flask-based login page that includes user registration, authentication, and a profile page.

## Project Structure
```
flask-auth/
│
├── app/
│   ├── __init__.py
│   ├── models.py          # Database models (User)
│   ├── routes.py          # Routes and views
│   ├── forms.py           # WTForms for login/registration
│   ├── templates/         # Jinja2 templates
│   │   ├── base.html      # Base template
│   │   ├── login.html     # Login page
│   │   ├── register.html  # Registration page
│   │   └── profile.html   # Profile page (protected)
│   └── static/            # Static files (CSS, JS, images)
│
├── requirements.txt       # List of dependencies
└── run.py                 # Entry point to run the app
```

## Installation & Setup

### 1. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up the Database
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 4. Run the Server
```bash
python run.py
```

## Features
- User registration
- Login and logout functionality
- Profile page (accessible only to authenticated users)

## Project Link
GitHub: [Login-Webpage](https://github.com/Barndalion/Login-Webpage)

## Credits
Login icons: [riajulislam - Flaticon](https://www.flaticon.com/free-icons/login)

