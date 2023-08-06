# encoding: utf-8
"""
@project: djangoModel->user_permission_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 用户权限服务
@created_time: 2022/8/23 9:33
"""
from ..models import BaseInfo


class PermissionService():
    __user_dict = None
    __is_err = False
    __err_message = None

    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def user(self):
        """用户基础信息"""
        if self.__user_dict is None:
            self.__user_dict = BaseInfo.objects.filter(id=self.user_id).first().to_json()
        return self.__user_dict

    @property
    def err_message(self):
        return self.__err_message

    @err_message.setter
    def err_message(self, message):
        self.__is_err = True
        self.__err_message = message

    def is_valid(self):
        """
        判断是否存在异常
        :return Bool 存在异常True,不存在异常False
        """
        return self.__is_err

    def get_err_msg(self):
        """获取错误提示信息"""
        return self.err_message

    def permission_users(self, params=None):
        pass

    def is_allowable(self):
        """判断是否有操作全权限"""
        return True

    def permission_list(self, params=None):
        """获取当前用户的功能权限列表"""
        return None, None
