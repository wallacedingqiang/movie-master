# _*_ coding: utf-8 _*_
__author__ = 'mtianyan'
__date__ = '2017/8/26 17:06'

from flask import Blueprint


#蓝图
admin = Blueprint("admin",__name__)

import app.admin.views