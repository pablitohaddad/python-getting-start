import os

from flask import Flask

# Application Factory
def create_app(test_config=None):
    #Crio uma instância do Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        #Sobrescreve as configs do config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Seta algumas configurações padrões que o app vai usar, o dev ali e database.
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app