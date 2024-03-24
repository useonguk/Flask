from flask import Flask
from controllers.controller import school_blueprint
app = Flask(__name__)

app.register_blueprint(school_blueprint)

if __name__ == '__main__':
    app.run(debug=True)