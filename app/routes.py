from flask import render_template, url_for, redirect, flash    # 🖼️ For rendering templates & handling redirects
from app import app, db, bcrypt                                # 🔧 Importing app, database, and password hashing
from app.forms import LoginForm, RegistrationForm              # 📄 Importing form classes
from app.models import User                                    # 👤 Importing User model
from flask_login import login_user, current_user, logout_user  # 🔐 Handling user authentication

# 🏠 Home route
@app.route('/')
def home():
    return render_template('home.html')

# 🔐 Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 🚀 If user is already logged in, redirect to profile
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    form = LoginForm()  # 📄 Create an instance of LoginForm
    
    if form.validate_on_submit():  # ✅ If form is submitted and valid
        user = User.query.filter_by(email=form.email.data).first()  # 🔎 Find user by email
        
        # 🔑 Check if user exists and password is correct
        if user and user.check_password(form.password.data):
            login_user(user)  # 🔓 Log the user in
            flash(f'Welcome {user.username}!', 'success')  # 🎉 Flash success message
            return redirect(url_for('profile'))  # ➡️ Redirect to profile
        
        else:
            flash('Login failed. Check your email and password.', 'danger')  # ⚠️ Error message
    
    return render_template('login.html', form=form)  # 🖼️ Render login page with form

# 📝 Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # 🚀 If user is already logged in, redirect to profile
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    form = RegistrationForm()  # 📄 Create an instance of RegistrationForm
    
    if form.validate_on_submit():  # ✅ If form is submitted and valid
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # 🔐 Hash password
        
        # 👤 Create new user object
        user = User(username=form.username.data,
                    email=form.email.data,
                    password_hash=hashed_password)
        
        db.session.add(user)  # 💾 Add user to database
        db.session.commit()  # 📌 Save changes
        
        flash('Your account has been created! You can now log in.', 'success')  # 🎉 Success message
        return redirect(url_for('login'))  # ➡️ Redirect to login page
    
    return render_template('register.html', form=form)  # 🖼️ Render register page with form

# 👤 Profile route
@app.route('/profile')
def profile():
    if not current_user.is_authenticated:  # ❌ If user is not logged in, redirect to login
        return redirect(url_for('login'))
    
    return render_template('profile.html')  # 🖼️ Render profile page

# 🚪 Logout route
@app.route('/logout')
def logout():
    logout_user()  # 🔓 Log the user out
    return redirect(url_for('home'))  # 🔄 Redirect to home page
