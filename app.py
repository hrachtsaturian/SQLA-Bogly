"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'


debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()

# **GET */ :*** Redirect to list of users. (We’ll fix this in a later step).
@app.route('/')
def home():
    return redirect('/users')

# **GET */users :*** Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form.
@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# **GET */users/new :*** Show an add form for users
@app.route('/users/new')
def show_add_form():
    return render_template('user_form.html')

# **POST */users/new :*** Process the add form, adding a new user and going back to ***/users***
@app.route('/users/new', methods=['POST'])
def add_new_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    image_url = request.form.get('image_url')

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

# **GET */users/[user-id] :***Show information about the given user. Have a button to get to their edit page, and to delete the user.
@app.route('/users/<int:user_id>')
def show_user_detail(user_id):

    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

# **GET */users/[user-id]/edit :*** Show the edit page for a user. Have a cancel button that returns to the detail page for a user, and a save button that updates the user.
@app.route('/users/<int:user_id>/edit')
def show_user_edit_form(user_id):

    user = User.query.get_or_404(user_id)
    return render_template('user_edit.html', user=user)


# **POST */users/[user-id]/edit :***Process the edit form, returning the user to the ***/users*** page.
@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    image_url = request.form.get('image_url')

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

# **POST */users/[user-id]/delete :*** Delete the user.
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

    







