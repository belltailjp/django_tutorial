from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase
from polls.models import *

class QuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        q = Question(question_text = 'future', pub_date = timezone.now() + datetime.timedelta(days = 30))
        self.assertEqual(q.was_published_recently(), False)

