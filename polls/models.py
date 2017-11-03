from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='内容')
    pub_date = models.DateTimeField(verbose_name='发布日期')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.boolean = True
    was_published_recently.short_description = "最近添加"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='问题')
    choice_text = models.CharField(max_length=200, verbose_name='内容')
    votes = models.IntegerField(default=0, verbose_name='投票数')

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    name = models.CharField(max_length=128)

    messages = models.ManyToManyField('Person', through='Message')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Message(models.Model):
    source = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sources')
    destination = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='destinations')
    content = models.CharField(max_length=400)



class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return "%s -> %s [%s]" % (self.person, self.group, self.date_joined)
