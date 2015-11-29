import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "%s (%s)" % (self.question_text, self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 256)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return "%d: %s (vote: %d)" % (self.question.id, self.choice_text, self.votes)

