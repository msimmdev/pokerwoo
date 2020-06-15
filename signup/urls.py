from django.conf.urls import url
from signup import views

urlpatterns = [
    url('', views.signup, name='signup'),
]