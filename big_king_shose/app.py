from flask import Flask
from controllers.index import shose_blueprint
app = Flask(__name__)

app.register_blueprint(shose_blueprint)

if __name__ == '__main__':
    app.run(debug=True)