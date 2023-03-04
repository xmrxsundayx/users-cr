from flask import Flask, render_template, request, redirect
from user import Users

app = Flask(__name__)

@app.route('/users')
def users():
    all_users = Users.get_all()
    return render_template('users.html', all_users=all_users)

@app.route('/users/new')
def add_user():
    return render_template('add_user.html')

@app.route('/users/<int:id>')
def view_user(id):
    data = {'id': id}
    v_user = Users.get_user(data)
    return render_template('view.html', v_user=v_user)

@app.route('/create', methods=['POST'])
def create():
    users_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.save(users_data)
    return redirect('/users')

@app.route('/users/<int:id>/edit')
def edit_form(id):
    data = {'id': id} 
    return render_template('edit.html', user = Users.get_user(data))


@app.route('/users/edit',methods=['POST'])
def edit():
    updated_user = request.form['id']
    Users.edit(request.form)
    return redirect(f'/users/{updated_user}')

@app.route('/users/<int:id>/delete')
def delete(id):
    data = {'id': id}
    Users.delete(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
