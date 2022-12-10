from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # check for restrictions
        if len(email) < 4:
            flash('Email Address Must Be Greater Than 3 Characters.', category='error')
        elif len(nickname) < 2:
            flash('Nickname Must Be Greater Than 1 Character.', category='error')
        elif password1 != password2:
            flash('Passwords Do Not Match.', category='error')
        elif len(password1) < 7:
            flash('Password Must Be At Least 7 Characters.', category='error')
        else:
            # add user to database
            flash('Account Created!', category='success')

    return render_template("signup.html")
