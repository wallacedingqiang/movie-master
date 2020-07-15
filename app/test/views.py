from flask import render_template, flash, redirect, url_for, session, request

from app import db, app
from app.test.forms import LoginFrom
from . import test
from ..models import Admin, Adminlog,User


@test.route("/logintest/", methods=["GET", "POST"])
# @app.route('/logintest')
def login():
    form=LoginFrom()

    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["username"]).first()
        print((data["username"]))
        print(data["password"])
        if not admin.check_pwd(data["password"]):
            flash("密码错误!", "err")
            return redirect(url_for("admin.login"))
        # 如果是正确的，就要定义session的会话进行保存。
        session["admin"] = data["username"]
        session["admin_id"] = admin.id
        print(admin.id)
        adminlog = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr,
        )
        db.session.add(adminlog)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("admin.tag_add_test"))
        # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # return redirect('/index')
    return render_template('test/login.html', title='标签录入', form=form)
    # render_template第一个参数传入页面，然后根据后面的参数渲染模板



