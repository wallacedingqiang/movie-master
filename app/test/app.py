import pymysql
from flask import Flask, jsonify, json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Hello World Wallace good morning  @1@3￥1232323!')     #（jsonify返回一个json格式的数据）


@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)



@app.route('/getData')
def get_data():
    db = pymysql.connect(host="119.45.202.96", user="xyz",
                         password="x123456", db="test", port=3306)
    cur = db.cursor()

    sql="SELECT * from student"
    cur.execute(sql)
    results = cur.fetchall()
    sq = []
    for row in results:
            data = {}
            data['id'] = str(row[0])
            data['name'] = row[2]
            #注意，要是数值类型要转成字符串类型，不然会报错
            data['school'] = row[3]
            sq.append(data)
    jsondatar = json.dumps(sq, ensure_ascii=False)
    #print(jsondatar)

    db.close()

    return jsonify(jsondatar)
    # return jsondatar


if __name__ == '__main__':
    app.run()
