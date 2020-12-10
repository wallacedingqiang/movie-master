import requests
import json
import pymysql
import pysnooper


url1 = 'http://119.45.202.96:5000/getData'
url2 =  'http://119.45.202.96:5000/test_1.0'

class fund():

 @pysnooper.snoop()
 def insertdb(self):
  #读取接口插入数据库
  #链接数据库
  connection = pymysql.connect(
    host='localhost',
    user='root',
    password='d12345678',
    db='movie'
   )

  cursor = connection.cursor()

  sql = """INSERT INTO testsql(id, name, school) VALUES (%s, %s, %s)"""

  #读取接口
  r = requests.get(url1)
  movie_list = json.loads(r.text)
  print(movie_list)

  for movie in movie_list:
      cursor.execute(sql, tuple(movie.values()))
      print(tuple(movie.values()))

  connection.commit()
  connection.close()



 @pysnooper.snoop()
 def geturl(self):
  #接口参数
  data={'name':'wallace','age':'18'}
  response=requests.get(url2,params=data)
  #接口response的返回
  text = json.loads(response.text)
  print(text)


if __name__ == "__main__":
 fundtest=fund()
 fundtest.insertdb()
 fundtest.geturl()
