from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.MemberListCreate.as_view(), name='MemberListCreate'),
    path('api/<int:pk>/', views.MemberRetrieveUpdateDestroy.as_view(), name='MemberRetrieveUpdateDestroy'),
]