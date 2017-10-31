from django.db import models


class UserInfo(models.Model):
    """用户表"""
    user_name = models.CharField(max_length=20, unique=True, verbose_name=u"负责人")  # 负责人
    user_email = models.EmailField(null=True, blank=True, verbose_name=u"邮箱")  # 邮箱
    user_mobile = models.BigIntegerField(verbose_name=u"电话")  # 电话

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户表'
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.user_name
