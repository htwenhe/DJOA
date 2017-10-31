from django import template
from django.template import Library
from django.utils import six
from django.utils.safestring import mark_safe
from ..models import *
#from xadmin.util import static, vendor as util_vendor

register = Library()

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
