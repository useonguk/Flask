from flask import Flask
from controllers.controller import rest_blueprint
app = Flask(__name__)

app.register_blueprint(rest_blueprint)

if __name__ == '__main__':
    app.run(debug=True)