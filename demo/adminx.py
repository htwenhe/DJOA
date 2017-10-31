from .models import UserInfo
import xadmin


class UserInfoAdmin(object):
    list_display = ('user_name', 'user_email', 'user_mobile')
    list_bookmarks = [{
        "title": "存在邮箱",
        "query": {"user_email__contains": '@'},
        "order": ("-user_name",),
        "cols": ('user_name', 'user_email', 'user_mobile'),
    }]


xadmin.site.register(UserInfo, UserInfoAdmin)
