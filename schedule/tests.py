from django.test import TestCase
from django.utils.dateparse import parse_datetime
import pytz
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from . import models
from . import serializers

# Create your tests here.

SESSIONS_URL = '/api/schedule/sessions/'

class SessionsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test@test.com', 'Din0Pope')
        self.client.force_authenticate(self.user)
    
    def test_retrieve_session(self):
        models.Session.objects.create(schedule_date=pytz.timezone('Europe/London').localize(parse_datetime('2021-01-01 19:30:00')), createdby_player='2', description='Test')
        models.Session.objects.create(schedule_date=pytz.timezone('Europe/London').localize(parse_datetime('2021-02-02 11:15:00')), createdby_player='3', description='Second Test')

        res = self.client.get(SESSIONS_URL)

        sessions = models.Session.objects.all()
        serializer = serializers.SessionSerializer(sessions, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)