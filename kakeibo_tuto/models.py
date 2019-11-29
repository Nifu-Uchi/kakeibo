from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = '分類'
        verbose_name_plural = '分類'
    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name

class Ranks(models.Model):
    class Meta:
        db_table = 'Ranks'
        verbose_name = '重要度'
        verbose_name_plural = '重要度'
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Suitoh(models.Model):
    class Meta:
        db_table = 'suitoh'
        verbose_name = '出納表'
        verbose_name_plural = '出納表'

    data = models.DateField(verbose_name="Date",default=datetime.now)
    cat = models.ForeignKey(Category, on_delete= models.PROTECT, verbose_name="分類")
    out_cost = models.IntegerField(verbose_name="支出")
    meimoku = models.CharField(verbose_name="名目", max_length=100)
    rank = models.ForeignKey(Ranks, on_delete= models.PROTECT, verbose_name="重要度")
    def __str__(self):
        return self.meimoku