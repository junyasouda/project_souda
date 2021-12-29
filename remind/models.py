from django.db import models
from django.utils import timezone #djangoでは、datetime.nowのかわりに、timezzone.nowで現在時刻を取得する


class Task(models.Model):
    subject = models.CharField('項目',max_length=255)
    contents = models.TextField('内容',max_length=255)
    date = models.DateField('日付',default=timezone.now)
    name = models.CharField('担当者',max_length=30)

    def __str__(self):
        return self.subject