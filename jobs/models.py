from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
job_types = [
    (0, '技术类'),
    (1, '产品类'),
    (2, '运营类'),
    (3, '设计类')
]
job_cities = [
    (0, '北京'),
    (1, '南京'),
    (2, '广州'),
    (3, '深圳')
]
class Job(models.Model):
    job_type = models.SmallIntegerField(verbose_name='职位类型', choices=job_types, blank=False)
    job_name = models.CharField(verbose_name='职业名称', max_length=250, blank=False)
    job_city = models.SmallIntegerField(choices=job_cities, verbose_name="工作地点", blank=False)
    job_reponsibility = models.TextField(verbose_name='职位职责', max_length=1024)
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now)
