from flask import Blueprint, render_template, redirect, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form#['']
    print(data)
    return render_template('login.html')



@auth.route('/logout')
def logout():
    return 'logout'



@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 2 characters', category= 'error')

        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters', category= 'error')

        elif password1 != password2:
            flash('Password don not match.', category= 'error')


        elif len(password1) < 4:
            flash('Password must be greater than 3 characters', category= 'error')

        else:
            # add user to data base
            flash('Account Created!', category= 'success')

    return render_template('sign_up.html')