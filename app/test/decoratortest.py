from decorator import decorator
#
# def wx_jwt_auth_token_parse_http(func):
#     """
#     客户端用户身份验证装饰器
#     :param func:
#     :return:
#     """
#     def _func(func, self, *args, **kwargs):
#         user_id=123456
#         kwargs.update(user_id=user_id)
#         return func(self, *args, **kwargs)
#     return decorator(_func, func)
#
#
#
# @wx_jwt_auth_token_parse_http
# def foo(self, **kwargs):
#     user_id = kwargs.get('user_id')
#     print('I am foo.')
#     print('goodby, %s' % user_id)


def wx_jwt_auth_token_parse_http(func):
    def _func(func, *args, **kwargs):
        print('hello, %s' % func.__name__)
        func()
        print('goodby, %s' % func.__name__)
    return decorator(_func, func)


@wx_jwt_auth_token_parse_http
def foo():
    print('I am foo.')


foo()