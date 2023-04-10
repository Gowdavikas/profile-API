from django.urls import path

from profiles_api import views

urlpatterns = [
    path('apiView/', views.APIProject.as_view())
]
