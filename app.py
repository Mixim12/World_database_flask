import os
from flask_bootstrap import Bootstrap
from flask import render_template
from .db import db

# App Initialization
from . import create_app 
app = create_app(os.getenv("CONFIG_MODE"))
app.config['SECRET_KEY'] = 'secret_key'

Bootstrap(app)

@app.route('/')
def index():
    return render_template('world_app/index.html')


from .Continents import urls
from .Countries import urls
from .Cities import urls 

if __name__ == "__main__":
    app.run()