from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'


class Good(models.Model):
    name = models.CharField(max_length=10, verbose_name='小分类名')
    madedate = models.DateTimeField(auto_now_add=True, verbose_name='生产时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', related_name='goods')


class Sgood(models.Model):
    name = models.CharField(max_length=10, verbose_name='商品名')
    madedate = models.DateTimeField(auto_now_add=True, verbose_name='生产时间')
    desc = models.CharField(max_length=10, verbose_name='描述')
    price = models.IntegerField(default=188, verbose_name='价格')
    view = models.IntegerField(default=0, verbose_name='浏览量')
    img=models.ImageField()
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='小分类', related_name='sgoods')


class User(AbstractUser):
    name = models.CharField(max_length=10, verbose_name='用户名')
    telphone = models.CharField(max_length=11, verbose_name='手机号')
    email = models.EmailField(default='1969563601@qq.com')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ManyToManyField(Good, verbose_name='商品')

    def __str__(self):
        return self.user.name


class GoodImg(models.Model):
    img = models.ImageField(upload_to='goodimg')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='所属商品', related_name='imgs')


class Advantage(models.Model):
    img = models.ImageField(upload_to='advanimg')


class Label(models.Model):
    name = models.CharField(max_length=6)


class Tool(models.Model):
    title = models.CharField(max_length=10)


class Toolimg(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='toolimg')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, verbose_name='所属标题', related_name='toolimg')


class Personaly(models.Model):
    name = models.CharField(max_length=10)
    num = models.IntegerField(default=0)
