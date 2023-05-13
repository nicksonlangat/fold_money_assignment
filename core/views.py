from rest_framework import viewsets
from .models import Project, Hashtag
from .serializers import ProjectSerializer, HashtagSerializer

# Create your views here.

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class HashtagViewset(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

