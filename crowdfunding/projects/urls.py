from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns # function that does all of the busy work
from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects/<int:pk>/updates/', views.ProjectUpdatesList.as_view()),
    path('projects/<int:pk>/updates/edit/', views.ProjectUpdateDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)