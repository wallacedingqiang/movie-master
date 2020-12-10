# from flask import render_template, flash, redirect, url_for, session, request
#
# from app import db, app
# from app.test.forms import LoginFrom
# from . import test
# from ..admin.forms import TagForm
# from ..models import Admin, Adminlog, User, Tag
#
#
# @test.route("/logintest/", methods=["GET", "POST"])
# # @app.route('/logintest')
# def login():
#     form=LoginFrom()
#
#     if form.validate_on_submit():
#         data = form.data
#         admin = Admin.query.filter_by(name=data["username"]).first()
#         print((data["username"]))
#         print(data["password"])
#         if not admin.check_pwd(data["password"]):
#             flash("密码错误!", "err")
#             return redirect(url_for("test.login"))
#         # 如果是正确的，就要定义session的会话进行保存。
#         session["admin"] = data["username"]
#         session["admin_id"] = admin.id
#         print(admin.id)
#         adminlog = Adminlog(
#             admin_id=admin.id,
#             ip=request.remote_addr,
#         )
#         db.session.add(adminlog)
#         db.session.commit()
#         # return redirect(request.args.get("next") or url_for("test.tag_list_test"))
#         return redirect(request.args.get("next") or url_for("admin.tag_add_test"))
#         # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
#         # return redirect('/index')
#     return render_template('test/login.html', title='标签录入', form=form)
#     # render_template第一个参数传入页面，然后根据后面的参数渲染模板
#
#
# @test.route("/tag/test/edit/<int:id>", methods=["GET", "POST"])
# # @admin_login_req
# # @admin_auth
# def tag_edit_test(id=None):
#     """
#     标签编辑
#     """
#     form = TagForm()
#     form.submit.label.text = "修改"
#     print(id)
#     tag = Tag.query.get_or_404(id)
#     if form.validate_on_submit():
#         data = form.data
#         tag_count = Tag.query.filter_by(name=data["name"]).count()
#         # 说明已经有这个标签了,此时向添加一个与其他标签重名的标签。
#         if tag.name != data["name"] and tag_count == 1:
#             flash("标签已存在", "err")
#             return redirect(url_for("test.tag_edit_test", id=tag.id))
#         tag.name = data["name"]
#         db.session.add(tag)
#         db.session.commit()
#         flash("标签修改成功", "ok")
#         redirect(url_for("test.tag_edit_test", id=tag.id))
#     return render_template("test/tag_edit_test.html", form=form, tag=tag)
#
#
# @test.route("/tag/test/list/<int:page>/", methods=["GET"])
# # @admin_login_req
# # @admin_auth
# def tag_list_test(page=None):
#     """
#     标签列表
#     """
#     if page is None:
#         page = 1
#     page_data = Tag.query.order_by(
#         Tag.addtime.desc()
#     ).paginate(page=page, per_page=10)
#     return render_template("test/tag_list_test.html", page_data=page_data)
#
#
# @test.route("/tag/test/del/<int:id>/", methods=["GET"])
# # @admin_login_req
# # @admin_auth
# def tag_del_test(id=None):
#     """
#     标签删除
#     """
#     # filter_by在查不到或多个的时候并不会报错，get会报错。
#     tag = Tag.query.filter_by(id=id).first_or_404()
#     print(tag.name)
#     print(tag.id)
#     db.session.delete(tag)
#     db.session.commit()
#     flash("标签<<{0}>>删除成功".format(tag.name), "ok")
#     return redirect(url_for("test.tag_list_test", page=1))



from flask import render_template, flash, redirect, url_for, session, request

from app import db, app
from app.test.forms import LoginFrom
from . import test
from ..admin.forms import TagForm
from ..models import Admin, Adminlog, User, Tag, Oplog



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
        return redirect(request.args.get("next") or url_for("test.tag_add_test"))
        # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # return redirect('/index')
    return render_template('test/login.html', title='标签录入', form=form)
    # render_template第一个参数传入页面，然后根据后面的参数渲染模板





@test.route("/tag/listtest/", methods=["GET"])
# @admin_login_req
# @admin_auth
def tag_list_test(page=None):
    """
    标签列表
    """
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("test/tag_list_test.html", page_data=page_data)





@test.route("/tag/addtest/", methods=["GET", "POST"])
# @admin_login_req
# @admin_auth
def tag_add_test():
    """
    标签添加
    """
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["name"]).count()
        # 说明已经有这个标签了
        if tag == 1:
            flash("标签已存在", "err")
            return redirect(url_for("test.tag_add_test"))
        tag = Tag(
            name=data["name"]
        )
        db.session.add(tag)
        db.session.commit()
        oplog = Oplog(
            admin_id=session["admin_id"],
            ip=request.remote_addr,
            reason="添加标签%s" % data["name"]
        )
        db.session.add(oplog)
        db.session.commit()
        flash("标签添加成功", "ok")
        redirect(url_for("test.tag_add_test"))
    return render_template("test/tag_add_test.html", form=form)


@test.route("/tag/edit/<int:id>", methods=["GET", "POST"])
# @admin_login_req
# @admin_auth
def tag_edit_test(id=None):
    """
    标签编辑
    """
    form = TagForm()
    form.submit.label.text = "修改"
    print(id)
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data["name"]).count()
        # 说明已经有这个标签了,此时向添加一个与其他标签重名的标签。
        if tag.name != data["name"] and tag_count == 1:
            flash("标签已存在", "err")
            return redirect(url_for("test.tag_edit_test", id=tag.id))
        tag.name = data["name"]
        db.session.add(tag)
        db.session.commit()
        flash("标签修改成功", "ok")
        redirect(url_for("test.tag_edit_test", id=tag.id))
    return render_template("test/tag_edit_test.html", form=form, tag=tag)