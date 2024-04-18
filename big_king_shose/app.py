from flask import Flask
from flask_cors import CORS
from controllers.index import shose_blueprint

# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발# 신발  

app = Flask(__name__)
app.register_blueprint(shose_blueprint)

# 모든 도메인에서의 요청을 허용합니다.
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    print(app)
    app.run(debug=True)
