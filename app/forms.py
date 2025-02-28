from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    email = EmailField('Email Address *', validators=[DataRequired(), Email()])  # 📧 Field for user's email
    password = PasswordField('Password *', validators=[DataRequired()])  # 🔒 Field for user's password
    submit = SubmitField('Login')  # 🚀 Submit button for logging in

class RegistrationForm(FlaskForm):
    username = StringField('Username *', validators=[DataRequired(), Length(min=5, max=20)])  # 👤 Field for choosing a username (must be between 5 and 20 characters)
    email = EmailField('Email Address *', validators=[Email(), DataRequired()])  # 📧 Email field with validation
    password = PasswordField('Password *', validators=[DataRequired()])  # 🔑 Password field (should be strong)
    password_confirm = PasswordField('Confirm Password *', validators=[DataRequired(), EqualTo('password')])  # 🔁 Confirmation field (must match the password)
    submit = SubmitField('Register')