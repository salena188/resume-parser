from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Announcement
from .serializers import AnnouncementSerializer

class AnnouncementListCreateView(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer