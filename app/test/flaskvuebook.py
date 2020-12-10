"""
测试Flask
"""

import pymysql
from flask import Flask, jsonify,request,json
from flask_cors import CORS
import uuid

# 配置参数,开启debug模式,json转换中文不使用unicode
DEBUG = True
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)

# 开启CORS,解决跨域调用问题
CORS(app, resources={r'/*': {'origins': '*'}})
# 也可以简单直接写CORS(app)




# BOOKS = [
# #     {
# #         'title': 'On the Road',
# #         'author': 'Jack Kerouac',
# #         'read': True
# #     },
# #     {
# #         'title': 'Harry Potter and the Philosopher\'s Stone',
# #         'author': 'J. K. Rowling',
# #         'read': False
# #     },
# #     {
# #         'title': 'Green Eggs and Ham',
# #         'author': 'Dr. Seuss',
# #         'read': True
# #     }
# # ]


import uuid
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]



# 配置路由
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Hello Wallace!中文!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



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

    print(sq)
    #jsondatar = json.dumps(sq, ensure_ascii=False)
    #print(jsondatar)

    db.close()

    #return jsonify(jsondatar)
    # return jsondatar

    return jsonify({
        'status': 'success',
        'stulist': sq
    })





if __name__ == "__main__":
    app.run()
