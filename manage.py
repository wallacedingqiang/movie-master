# _*_ coding: utf-8 _*_
__author__ = 'mtianyan'
__date__ = '2017/8/26 17:05'


from app import app, db
import sys
import os
from flask_script import Manager
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\admin'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\home'))
from app.models import Role, Admin

manage = Manager(app)

if __name__ == "__main__":
    manage.run()

    # 向角色表（role）添加数据
    # db.create_all()
    # # role = Role(
    # #     name="超级管理员",
    # #     auths=""
    # # )
    # # db.session.add(role)
    # # db.session.commit()
    #
    # from werkzeug.security import generate_password_hash
    #
    # admin = Admin(
    #     name="taogangshow",
    #     pwd=generate_password_hash("hellomovie"),
    #     is_super=0,
    #     role_id=9
    # )
    # db.session.add(admin)
    # db.session.commit()