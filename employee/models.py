from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.html import mark_safe
# Create your models here.

GENDER_STATUS = (
    ('Male','Male'),
    ('Female','Female')
)


class Employee(models.Model):
    photo = models.ImageField(upload_to='document',blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)
    address = models.CharField(max_length=500, blank=True, null=True, unique=True)
    email = models.CharField(max_length=500, blank=True, null=True, unique=True)
    gender = models.TextField(choices=GENDER_STATUS, default='', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    mobile = models.BigIntegerField(unique=True, blank=True, null=True)
    status = models.NullBooleanField(default=True)
    credit = models.FloatField(blank=True, null=True,default=0.0)
    created_at = models.DateTimeField(blank=True, null=True, default=now)
    type = models.ForeignKey('EmployeeType', models.DO_NOTHING, blank=True, null=True)
    product = models.ManyToManyField('Product', blank=True, null=True)
    meta_data = JSONField(blank=True, null=True)
    production_user = ArrayField(models.CharField(max_length=500, blank=True, null=True), null=True, blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.photo))
        else:
            return mark_safe('<img src="/media/document/default.jpg" width="50" height="50" />')

    image_tag.short_description = 'Image'


class EmployeeType(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name