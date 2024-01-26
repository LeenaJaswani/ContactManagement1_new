from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserInfoSerializer
# , ContactListSerializer
from .models import UserInfo

from django.shortcuts import render

from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.views.generic import TemplateView

class ContactViewPagination(PageNumberPagination):
 	queryset = UserInfo.objects.get_queryset().order_by('-id')
 	serializer_class = UserInfoSerializer
 	page_size=100
 	
class ContactViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('-id')
    serializer_class = UserInfoSerializer
    
   
    search_fields=['$Name','ContactNumber']
    
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
