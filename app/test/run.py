from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
#CORS允许前后端跨域访问
# 指定了静态和模板文件夹来用前端包指向 /dist 文件夹，在根文件夹中运行 Flask 服务
app = Flask(__name__,
    static_folder ="./frontend/dist/static",
    template_folder ="./frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

#以下是api模板
#在后端生成随机数
@app.route('/api/random')
def random_number():
    response = {
    'randomNumber': randint(1, 100)
    }
    return jsonify(response)


if __name__=="__main__":
    app.run(debug = True)
