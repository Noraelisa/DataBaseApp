from flask import Flask
from os import getenv

app = Flask(__name__, template_folder='template')
app.secret_key = getenv("SECRET_KEY")

import routes