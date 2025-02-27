from AuthBarn import Action
from flask import Flask, render_template,request,url_for,redirect

instance = Action(_dev_mode = False)
instance.add_user("Darell Barnes","lionel12$","Admin")
app = Flask(__name__)

@app.route('/')
def logic():
    return render_template("home.html")


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        log = instance.login(username,password)

        if log == True:
            return render_template("login.html", message ="Logged successfuly, No User Page Yet")
        else:
            return render_template("login.html", message = log['message'])
    return render_template("login.html")
    
@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        log = instance.register(username,password)

        if log == True:
            return render_template("login.html", message = "Successfully Registered")
        else:
            return render_template("register.html", message = log['message'])
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)