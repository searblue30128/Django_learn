from django.db import models
from django.db.models import *

# Create your models here.
# python manage.py createsuperuser
# admin    a12345678
BALANCE_TYPE = ((u"收入",u"收入"),(u"支出",u"支出"))

class Category(models.Model):
    # user =
    category = CharField(max_length=20)
    def __str__(self):
        return self.category

class Record(models.Model):
    # user =
    date         = DateField()
    description  = CharField(max_length=300)
    category     = ForeignKey(Category,on_delete=models.SET_NULL , null=True)
    cash         = IntegerField()
    balance_type = CharField(max_length=2 , choices = BALANCE_TYPE)
    def __str__(self):
        return self.description