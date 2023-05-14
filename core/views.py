from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Hashtag
from .serializers import ProjectCreateSerializer, HashtagSerializer

# Create your views here.

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


class HashtagViewset(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

