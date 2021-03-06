# Author:  DINDIN Meryll
# Date:    03 Octobre 2019
# Project: aster-website

# General usage import
import os
import json
import warnings
import requests

# Flask-relative import
from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import Flask
from flask import jsonify
from flask import Response
from flask import render_template

# Flask extensions
from wtforms import Form 
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms import validators
from wtforms import SubmitField
from wtforms import ValidationError
from flask_mail import Mail
from flask_mail import Message