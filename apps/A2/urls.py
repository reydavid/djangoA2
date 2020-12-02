from django.urls import path
from apps.A2 import views

app_name = "A2"

urlpatterns = [
    path('',views.current_datetime)
]