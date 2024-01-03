import os

from flask import Flask

def create_app(test_config=None):
    #createand configure the app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'iflaskr.sqlite'),        
    )

    if test_config is None:
        #load the instance config, if it exists , when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple hello page
    @app.route('/hello')
    def hello():
        return "Hello, World!!!  How are you?"
    
    return app