from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User, Group
#from rest_framework import serializers


# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=256, verbose_name=u"作者")
    title = models.CharField(max_length=256, verbose_name=u"标题")
    content = models.CharField(max_length=1024*8, verbose_name=u"内容")
    createdate=models.DateTimeField(u'时间', default=timezone.now)

    class Meta:
        db_table = 'article'
        verbose_name = '文章表'
        verbose_name_plural = "文章表"

    def __str__(self):
        return self.title




# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = "分类"


@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"



@python_2_unicode_compatible
class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """

    # 文章标题
    title = models.CharField(max_length=70,verbose_name=u"标题")

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(verbose_name=u"内容")

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(verbose_name=u"创建时间")
    modified_time = models.DateTimeField(verbose_name=u"修改时间")

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category, verbose_name=u"分类")
    tags = models.ManyToManyField(Tag, blank=True,verbose_name=u"标签")

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User,verbose_name=u"作者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = "文章表"



class UserInfo2(models.Model):
    """用户表"""
    user_name = models.CharField(max_length=20, unique=True, verbose_name=u"负责人")  # 负责人
    user_email = models.EmailField(null=True, blank=True, verbose_name=u"邮箱")  # 邮箱
    user_mobile = models.BigIntegerField(verbose_name=u"电话")  # 电话

    class Meta:
        db_table = 'user_info2'
        verbose_name = '用户表2'
        verbose_name_plural = "用户表2"

    def __str__(self):
        return self.user_name

class Leave_class(models.Model):
    name= models.CharField(max_length=256, verbose_name=u"名称")
    class Meta:
        db_table = 'leave_class'
        verbose_name = '请假类别'
        verbose_name_plural = "请假类别"

    def __str__(self):
        return self.name

class Leave(models.Model):
    """用户表"""
    req_name = models.CharField(max_length=256, verbose_name=u"申请人")
    req_date = models.DateTimeField(verbose_name=u"申请时间")
    depart_name = models.CharField(max_length=256,verbose_name=u"部门")
    position =  models.CharField(max_length=256,  verbose_name=u"职位")
    req_class =models.ForeignKey(Leave_class,verbose_name=u'请假类别')
    start_time=models.DateTimeField(verbose_name=u"开始时间")
    end_time=models.DateTimeField(verbose_name=u"结束时间")
    resion=models.CharField(max_length=256,  verbose_name=u"请假事由")
    file_url=models.CharField(max_length=256,  verbose_name=u"上传附件")
    #审批领导

    class Meta:
        db_table = 'leave'
        verbose_name = '请假'
        verbose_name_plural = "请假"

    def __str__(self):
        return self.req_name
'''
class LeaveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Leave
        fields = ('req_name', 'req_date', 'depart_name', 'position','resion')
'''
