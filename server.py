from flask import Flask, render_template, request, redirect
from user import Users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_user.html')

@app.route('/create', methods=['POST'])
def create():
    users_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.save(users_data)
    return redirect('/users')

@app.route('/users')
def users():
    all_users = Users.get_all()
    return render_template('users.html', all_users=all_users)


if __name__ == "__main__":
    app.run(debug=True)