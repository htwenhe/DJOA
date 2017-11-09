from django.conf.urls import url
from django.views.decorators.cache import cache_page
from .views import *

app_name = 'oa'

'''
url(r'^$', views.IndexView.as_view(), name='index'),
# (?P<article_id>\d+)为一个组, 其中?P<article_di>中的article_id代表了该组的组名
url(r'^article/(?P<article_id>\d+)$', cache_page(60 * 15)(views.ArticleDetailView.as_view()), name='detail'),
url(r"^category/(?P<cate_id>\d+)$", views.CategoryView.as_view(), name='category'),
url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
url(r'^search/$', views.blog_search, name='search'),
url(r'^about_me/$', views.suggest_view, name='about_me'),
url(r'^tags/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
'''


urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^leave/$',leave),
    url(r'^leave/save/$', LeaveSave),
    url(r'^leave/lookup/(?P<pk>[0-9]+)/$', LeaveLookup),
    url(r'^leave/del/(?P<pk>[0-9]+)/$', LeaveDel),
    url(r'^leave/edit/(?P<pk>[0-9]+)/$', LeaveEdit),
    url(r'^leave/post_list_json/$', PostListJson.as_view(), name='post_list_json'),
    url(r'^leave/req_class_list_json/$', ReqClassListJson, name='req_class_list_json'),
    url(r'^leave/audit_person_json/$', AuditPersonJson, name='audit_person_json'),
    url(r'hello', hello, name='hello')
]