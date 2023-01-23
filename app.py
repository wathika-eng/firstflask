#imports#
from flask import Flask, redirect, url_for
from flask import render_template

app = Flask('__name__')
a = False

##login page##
@app.route("/admin/login/")
def admin():
    return render_template('index.html')


##home##
@app.route("/")
def home():
    return render_template('index2.html')

#new user account#
@app.route("/user")
def user():
    
    return redirect(url_for("admin"))


#run flask#
if __name__ == '__main__':
    app.run()