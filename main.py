# Import necessary libraries
import json
import os
import io
from flask import Flask,render_template, request, jsonify,flash,url_for,redirect,session,make_response

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired



# Initialize Flask application
app=Flask(__name__)

# Set Flask application configurations
app.config['SECRET_KEY']='david'

# Configuration to specify the static folder
app.static_folder = 'static'


# Define the homepage route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():

   # Render the homepage template for GET requests
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)