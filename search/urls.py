from django.urls import path

from search.views import (
    SearchUsers, SearchHashtags, 
    SearchProjectBySlugAndDescription, 
    SearchProjectByUser, SearchProjectByHashtag
)

urlpatterns = [
    path('project/user/<str:query>/', SearchProjectByUser.as_view()),
    path('project/hashtag/<str:query>/', SearchProjectByHashtag.as_view()),
    path('project/<str:query>/', SearchProjectBySlugAndDescription.as_view()),

    #additional not required by the assignment just added them :)
    path('user/<str:query>/', SearchUsers.as_view()),
    path('hashtag/<str:query>/', SearchHashtags.as_view()),
]
