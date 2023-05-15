from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Preference
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define the function to generate clothing suggestions based on user preferences
def generate_clothing_suggestions(preferences):
    # Your implementation here
    pass

@app.route('/')
def index():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if user:
        # Get the user's preferences from the database
        preferences = Preference.query.filter_by(user_id=user_id).all()
        # Call the function to generate clothing suggestions based on user preferences
        clothing_suggestions = generate_clothing_suggestions(preferences)
        # Render the template with the suggestions
        return render_template('index.html', user=user, clothing_suggestions=clothing_suggestions)
    else:
        # If the user does not exist, redirect to the signup page
        return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Create a new user and add it to the database
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        # Redirect to the index page with the new user ID as a query parameter
        return redirect(url_for('index', user_id=user.id))
    else:
        # Render the signup template
        return render_template('signup.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if request.method == 'POST':
        # Get the user's preferences from the form and add them to the database
        category = request.form['category']
        color = request.form['color']
        preference = Preference(user_id=user_id, category=category, color=color)
        db.session.add(preference)
        db.session.commit()
        # Redirect to the index page with the user ID as a query parameter
        return redirect(url_for('index', user_id=user_id))
    else:
        # Render the preferences template with the user object
        return render_template('preferences.html', user=user)
