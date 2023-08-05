# _*_coding:utf-8_*_

from django.urls import re_path

# from django.urls import include
# from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from .apis import user_contact_book
from .apis import user_detail_info
from .apis import user_group
from .apis import user_info
from .apis import user_list
from .apis import user_login
from .apis import user_login_wechat
from .apis import user_password
from .apis import user_platform
from .apis import user_register

# 应用名称
app_name = 'xj_user'

# 应用路由
urlpatterns = [
    re_path(r'^platform/?$', user_platform.UserPlatform.as_view(), ),
    re_path(r'^register/?$', user_register.UserRegister.as_view(), ),
    re_path(r'^login/?$', user_login.UserLogin.as_view(), ),
    re_path(r'^login_wechat/?$', user_login_wechat.WechetLogin.as_view(), ),

    re_path(r'^list/?$', user_list.UserListAPIView.as_view(), ),  # 用户列表
    re_path(r'^info/?$', user_info.UserInfo.as_view(), ),

    re_path(r'^password/?$', user_password.UserPassword.as_view(), ),
    re_path(r'^contact_book/?$', user_contact_book.UserContactBook.as_view(), ),

    # 详细信息查询/新增/修改
    re_path(r'^list_detail/?$', user_detail_info.UserListDetail.as_view(), ),
    re_path(r'^detail/?$', user_detail_info.UserDetail.as_view(), ),
    # re_path(r'^detail_add/?$', user_detail_info.UserDetailAdd.as_view(), ),  # 用户必须存在才有信息编辑，所以这个接口是多余的
    re_path(r'^detail_edit/?$', user_detail_info.UserDetailEdit.as_view(), ),

    # 分组
    re_path(r'^group/?$', user_group.GroupAPIView.as_view(), ),
    re_path(r'^group_list/?$', user_group.GroupAPIView.list, ),

]
