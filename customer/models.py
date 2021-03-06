from django.db import models

# Create your models here.
from users.models import User
from utils import constants


class Nature(models.Model):
    """客户性质"""
    name = models.CharField('性质名称', max_length=22)

    class Meta:
        db_table = 'cus_nature'
        verbose_name = verbose_name_plural = "客户性质"

    def __str__(self):
        return self.name


class Industry(models.Model):
    """客户行业"""
    name = models.CharField('客户行业', max_length=22)

    class Meta:
        db_table = 'cus_industry'
        verbose_name = verbose_name_plural = '客户行业'

    def __str__(self):
        return self.name


class Customer(models.Model):
    """客户模型"""
    name = models.CharField('客户名称', max_length=64, unique=True)
    rank = models.SmallIntegerField('客户级别', choices=constants.RANK_ITEMS, default=constants.RANK_NORMAL)
    website = models.CharField('客户网址', max_length=255, blank=True, null=True)
    scale = models.SmallIntegerField('客户规模', choices=constants.SCALE_ITEMS, default=constants.SCALE_TEN)
    nature = models.ForeignKey(Nature, verbose_name='客户性质', blank=True, null=True)
    industry = models.ForeignKey(Industry, verbose_name='客户行业', blank=True, null=True)
    remarks = models.CharField('客户备注', max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='创建人', related_name='customer')
    # belong_user = models.ForeignKey(User, verbose_name='负责人', related_name='belong_user', blank=True, null=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    is_valid = models.BooleanField('是否有效', default=True)

    """客户的收货地址"""
    shop_province = models.CharField('收货省份', max_length=32, blank=True, null=True)
    shop_city = models.CharField('收货市区', max_length=32, blank=True, null=True)
    shop_area = models.CharField('收货区域', max_length=32, blank=True, null=True)
    shop_town = models.CharField('收货街道', max_length=32, blank=True, null=True)
    shop_address = models.CharField('收货详细地址', max_length=64, blank=True, null=True)
    shop_username = models.CharField('收货地收货人', max_length=32, blank=True, null=True)
    shop_phone = models.CharField('收货收货人电话', max_length=32, blank=True, null=True)

    """客户的发票地址"""
    invoice_province = models.CharField('发票省份', max_length=32, blank=True, null=True)
    invoice_city = models.CharField('发票市区', max_length=32, blank=True, null=True)
    invoice_area = models.CharField('发票区域', max_length=32, blank=True, null=True)
    invoice_town = models.CharField('发票街道', max_length=32, blank=True, null=True)
    invoice_address = models.CharField('发票详细地址', max_length=64, blank=True, null=True)
    invoice_username = models.CharField('发票地收货人', max_length=32, blank=True, null=True)
    invoice_phone = models.CharField('发票收货人电话', max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'customer'
        verbose_name = verbose_name_plural = "客户"
        ordering = ['created_at', 'rank']

    def __str__(self):
        return self.name
