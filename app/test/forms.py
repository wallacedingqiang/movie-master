from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired


class LoginFrom(FlaskForm):
    # username=StringField('usernametest',validators=[DataRequired()])

    username = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # 注释此处显示forms报错errors信息
            # "required": "required"
        }
    )


    password=PasswordField('password',validators=[DataRequired()])
    remember_me=BooleanField('Remember me')
    submit=SubmitField('点击跳转')


    ''':arg
    在这里可以看出导入的FlaskForm作为LoginForm的父类，导入的StringField、PasswordField,分别有着参数Username、Password，
    后面的参数validators则表明了验证规则，BooleanField则定义了一个Checkbox类型的，若加上default='checked'默认勾选此框，
    而SubmitField则创建了一个submit按钮，导入的DataRequired是用来进行验证必填项的，也就是不填User和password会产生报错
    '''

