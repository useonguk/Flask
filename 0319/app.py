from flask import Flask, Blueprint
from flask_cors import CORS
from controllers.controller import school_blueprint

app = Flask(__name__)

# CORS 설정
CORS(app)   

# Blueprint 등록
app.register_blueprint(school_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
