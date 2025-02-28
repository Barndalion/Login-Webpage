from flask import Flask                  # 🚀 To create a basic Flask application
from flask_sqlalchemy import SQLAlchemy  # 🗄️ To manage the database (ORM for SQL databases)
from flask_bcrypt import Bcrypt          # 🔐 To encrypt data and passwords for security
from flask_login import LoginManager     # 🔑 To manage user authentication (login/logout)
from uuid import uuid4                   # 🔢 To generate unique keys (UUIDs)
import os                                # 🖥️ To interact with the operating system (e.g., environment variables)
from dotenv import load_dotenv           # 📂 To load environment variables from a .env file


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

load_dotenv()  # Upload .env file

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'  # SQLite DATABASE
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Route for LOGIN page

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

from app import routes