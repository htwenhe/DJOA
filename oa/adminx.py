from .models import *
import xadmin

'''
class ArticleAdmin(object):
    list_display = ('author', 'title', 'createdate')
    list_bookmarks = [{
        "order": ("-createdate",),
        "cols": ('author', 'title', 'createdate'),
    }]


xadmin.site.register(Article, ArticleAdmin)
'''


class PostAdmin(object):
    list_display = ('title', 'author', 'modified_time','category')
    list_bookmarks = [{
        "title": "按日期排序",
        "query": {"1": '1'},
        "order": ("-created_time",),
        "cols": ('author', 'title', 'created_time'),
    }]


class UserInfo2Admin(object):
    list_display = ('user_name', 'user_email', 'user_mobile')
    list_bookmarks = [{
        "title": "存在邮箱",
        "query": {"user_email__contains": '@'},
        "order": ("-user_name",),
        "cols": ('user_name', 'user_email', 'user_mobile'),
    }]


class CategoryAdmin(object):
    pass
    #list_display = ('name')


class TagAdmin(object):
    pass
    #list_display = ('name')

#xadmin.site.register(UserInfo2, UserInfo2Admin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
