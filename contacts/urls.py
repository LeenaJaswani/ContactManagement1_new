from django.urls import re_path
from contacts import views

from rest_framework import routers
from django.urls import path, include
from django.views.generic.base import TemplateView

from rest_framework import routers
router = routers.DefaultRouter()
router.register('contacts', views.ContactViewSet)
urlpatterns = [
re_path(r'^$', views.HomePageView.as_view()),
re_path(r'', include(router.urls)),
#  path('contacts/add_contact/', views.ContactViewSet.as_view({'post': 'add_contact'}), name='add_contact'),

]